from __future__ import annotations

import concurrent
import difflib
import re
import threading
import traceback
import os
import time
import urllib.parse
import uuid
import warnings
from concurrent.futures import Future
from datetime import timedelta
from enum import Enum
from pathlib import Path
from typing import Callable, Generator, Any, Union, List, Dict, Optional, Literal
import ast
import inspect
import numpy as np

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"

from huggingface_hub import SpaceStage
from huggingface_hub.utils import (
    build_hf_headers,
)

from gradio_client import utils

from importlib.metadata import distribution, PackageNotFoundError

from pydantic import BaseModel


class ReturnType(BaseModel):
    reply: str | list[str] | None
    prompt_raw: str | None = None
    actual_llm: str | None = None
    text_context_list: list[str] | None = []
    input_tokens: int = 0
    output_tokens: int = 0
    tokens_per_second: float = 0.0
    time_to_first_token: float = 0.0


try:
    assert distribution("gradio_client") is not None
    have_gradio_client = True
    from packaging import version

    client_version = distribution("gradio_client").version
    is_gradio_client_version7plus = version.parse(client_version) >= version.parse(
        "0.7.0"
    )
except (PackageNotFoundError, AssertionError):
    have_gradio_client = False
    is_gradio_client_version7plus = False

from gradio_client.client import Job, DEFAULT_TEMP_DIR, Endpoint
from gradio_client import Client


def check_job(job, timeout=0.0, raise_exception=True, verbose=False):
    try:
        e = job.exception(timeout=timeout)
    except concurrent.futures.TimeoutError:
        # not enough time to determine
        if verbose:
            print("not enough time to determine job status: %s" % timeout)
        e = None
    if e:
        # raise before complain about empty response if some error hit
        if raise_exception:
            raise RuntimeError(traceback.format_exception(e))
        else:
            return e


# Local copy of minimal version from h2oGPT server
class LangChainAction(Enum):
    """LangChain action"""

    QUERY = "Query"
    SUMMARIZE_MAP = "Summarize"
    EXTRACT = "Extract"


pre_prompt_query0 = "Pay attention and remember the information below, which will help to answer the question or imperative after the context ends."
prompt_query0 = "According to only the information in the document sources provided within the context above: "

pre_prompt_summary0 = """"""
prompt_summary0 = "Using only the information in the document sources above, write a condensed and concise well-structured Markdown summary of key results."

pre_prompt_extraction0 = (
    """In order to extract information, pay attention to the following text."""
)
prompt_extraction0 = (
    "Using only the information in the document sources above, extract "
)

hyde_llm_prompt0 = "Answer this question with vibrant details in order for some NLP embedding model to use that answer as better query than original question: "


class GradioClient(Client):
    """
    Parent class of gradio client
    To handle automatically refreshing client if detect gradio server changed
    """

    def reset_session(self) -> None:
        self.session_hash = str(uuid.uuid4())
        if hasattr(self, "include_heartbeat") and self.include_heartbeat:
            self._refresh_heartbeat.set()

    def __init__(
        self,
        src: str,
        hf_token: str | None = None,
        max_workers: int = 40,
        serialize: bool | None = None,  # TODO: remove in 1.0
        output_dir: str
        | Path = DEFAULT_TEMP_DIR,  # Maybe this can be combined with `download_files` in 1.0
        verbose: bool = False,
        auth: tuple[str, str] | None = None,
        *,
        headers: dict[str, str] | None = None,
        upload_files: bool = True,  # TODO: remove and hardcode to False in 1.0
        download_files: bool = True,  # TODO: consider setting to False in 1.0
        _skip_components: bool = True,  # internal parameter to skip values certain components (e.g. State) that do not need to be displayed to users.
        ssl_verify: bool = True,
        h2ogpt_key: str = None,
        persist: bool = False,
        check_hash: bool = True,
        check_model_name: bool = False,
        include_heartbeat: bool = False,
    ):
        """
        Parameters:
            Base Class parameters
            +
            h2ogpt_key: h2oGPT key to gain access to the server
            persist: whether to persist the state, so repeated calls are aware of the prior user session
                     This allows the scratch MyData to be reused, etc.
                     This also maintains the chat_conversation history
            check_hash: whether to check git hash for consistency between server and client to ensure API always up to date
            check_model_name: whether to check the model name here (adds delays), or just let server fail (faster)
        """
        if serialize is None:
            # else converts inputs arbitrarily and outputs mutate
            # False keeps as-is and is normal for h2oGPT
            serialize = False
        self.args = tuple([src])
        self.kwargs = dict(
            hf_token=hf_token,
            max_workers=max_workers,
            serialize=serialize,
            output_dir=output_dir,
            verbose=verbose,
            h2ogpt_key=h2ogpt_key,
            persist=persist,
            check_hash=check_hash,
            check_model_name=check_model_name,
            include_heartbeat=include_heartbeat,
        )
        if is_gradio_client_version7plus:
            # 4.18.0:
            # self.kwargs.update(dict(auth=auth, upload_files=upload_files, download_files=download_files))
            # 4.17.0:
            # self.kwargs.update(dict(auth=auth))
            # 4.24.0:
            self._skip_components = _skip_components
            self.ssl_verify = ssl_verify
            self.kwargs.update(
                dict(
                    auth=auth,
                    upload_files=upload_files,
                    download_files=download_files,
                    ssl_verify=ssl_verify,
                )
            )

        self.verbose = verbose
        self.hf_token = hf_token
        if serialize is not None:
            warnings.warn(
                "The `serialize` parameter is deprecated and will be removed. Please use the equivalent `upload_files` parameter instead."
            )
            upload_files = serialize
        self.serialize = serialize
        self.upload_files = upload_files
        self.download_files = download_files
        self.space_id = None
        self.cookies: dict[str, str] = {}
        if is_gradio_client_version7plus:
            self.output_dir = (
                str(output_dir) if isinstance(output_dir, Path) else output_dir
            )
        else:
            self.output_dir = output_dir
        self.max_workers = max_workers
        self.src = src
        self.auth = auth
        self.headers = headers

        self.config = None
        self.h2ogpt_key = h2ogpt_key
        self.persist = persist
        self.check_hash = check_hash
        self.check_model_name = check_model_name
        self.include_heartbeat = include_heartbeat

        self.chat_conversation = []  # internal for persist=True
        self.server_hash = None  # internal

    def __repr__(self):
        if self.config:
            return self.view_api(print_info=False, return_format="str")
        return "Not setup for %s" % self.src

    def __str__(self):
        if self.config:
            return self.view_api(print_info=False, return_format="str")
        return "Not setup for %s" % self.src

    def setup(self):
        src = self.src

        headers0 = self.headers
        self.headers = build_hf_headers(
            token=self.hf_token,
            library_name="gradio_client",
            library_version=utils.__version__,
        )
        if headers0:
            self.headers.update(headers0)
        if (
            "authorization" in self.headers
            and self.headers["authorization"] == "Bearer "
        ):
            self.headers["authorization"] = "Bearer hf_xx"
        if src.startswith("http://") or src.startswith("https://"):
            _src = src if src.endswith("/") else src + "/"
        else:
            _src = self._space_name_to_src(src)
            if _src is None:
                raise ValueError(
                    f"Could not find Space: {src}. If it is a private Space, please provide an hf_token."
                )
            self.space_id = src
        self.src = _src
        state = self._get_space_state()
        if state == SpaceStage.BUILDING:
            if self.verbose:
                print("Space is still building. Please wait...")
            while self._get_space_state() == SpaceStage.BUILDING:
                time.sleep(2)  # so we don't get rate limited by the API
                pass
        if state in utils.INVALID_RUNTIME:
            raise ValueError(
                f"The current space is in the invalid state: {state}. "
                "Please contact the owner to fix this."
            )
        if self.verbose:
            print(f"Loaded as API: {self.src} ✔")

        if is_gradio_client_version7plus:
            if self.auth is not None:
                self._login(self.auth)

        self.config = self._get_config()
        self.api_url = urllib.parse.urljoin(self.src, utils.API_URL)
        if is_gradio_client_version7plus:
            self.protocol: Literal[
                "ws", "sse", "sse_v1", "sse_v2", "sse_v2.1"
            ] = self.config.get("protocol", "ws")
            self.sse_url = urllib.parse.urljoin(
                self.src, utils.SSE_URL_V0 if self.protocol == "sse" else utils.SSE_URL
            )
            if hasattr(utils, "HEARTBEAT_URL") and self.include_heartbeat:
                self.heartbeat_url = urllib.parse.urljoin(self.src, utils.HEARTBEAT_URL)
            else:
                self.heartbeat_url = None
            self.sse_data_url = urllib.parse.urljoin(
                self.src,
                utils.SSE_DATA_URL_V0 if self.protocol == "sse" else utils.SSE_DATA_URL,
            )
        self.ws_url = urllib.parse.urljoin(
            self.src.replace("http", "ws", 1), utils.WS_URL
        )
        self.upload_url = urllib.parse.urljoin(self.src, utils.UPLOAD_URL)
        self.reset_url = urllib.parse.urljoin(self.src, utils.RESET_URL)
        if is_gradio_client_version7plus:
            self.app_version = version.parse(self.config.get("version", "2.0"))
            self._info = self._get_api_info()
        self.session_hash = str(uuid.uuid4())

        self.get_endpoints(self)

        # Disable telemetry by setting the env variable HF_HUB_DISABLE_TELEMETRY=1
        # threading.Thread(target=self._telemetry_thread, daemon=True).start()
        if (
            is_gradio_client_version7plus
            and hasattr(utils, "HEARTBEAT_URL")
            and self.include_heartbeat
        ):
            self._refresh_heartbeat = threading.Event()
            self._kill_heartbeat = threading.Event()

            self.heartbeat = threading.Thread(
                target=self._stream_heartbeat, daemon=True
            )
            self.heartbeat.start()

        self.server_hash = self.get_server_hash()

        return self

    @staticmethod
    def get_endpoints(client, verbose=False):
        t0 = time.time()
        # Create a pool of threads to handle the requests
        client.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=client.max_workers
        )
        if is_gradio_client_version7plus:
            from gradio_client.client import EndpointV3Compatibility

            endpoint_class = (
                Endpoint
                if client.protocol.startswith("sse")
                else EndpointV3Compatibility
            )
        else:
            endpoint_class = Endpoint

        if is_gradio_client_version7plus:
            client.endpoints = [
                endpoint_class(client, fn_index, dependency, client.protocol)
                for fn_index, dependency in enumerate(client.config["dependencies"])
            ]
        else:
            client.endpoints = [
                endpoint_class(client, fn_index, dependency)
                for fn_index, dependency in enumerate(client.config["dependencies"])
            ]
        if is_gradio_client_version7plus:
            client.stream_open = False
            client.streaming_future = None
            from gradio_client.utils import Message

            client.pending_messages_per_event = {}
            client.pending_event_ids = set()
        if verbose:
            print("duration endpoints: %s" % (time.time() - t0), flush=True)

    @staticmethod
    def is_full_git_hash(s):
        # This regex checks for exactly 40 hexadecimal characters.
        return bool(re.fullmatch(r"[0-9a-f]{40}", s))

    def get_server_hash(self):
        """
        Get server hash using super without any refresh action triggered
        Returns: git hash of gradio server
        """
        t0 = time.time()
        if self.config is None:
            self.setup()
        t1 = time.time()
        ret = "GET_GITHASH_UNSET"
        try:
            if self.check_hash:
                ret = super().submit(api_name="/system_hash").result()
                assert self.is_full_git_hash(ret), f"ret is not a full git hash: {ret}"
            return ret
        finally:
            if self.verbose:
                print(
                    "duration server_hash: %s full time: %s system_hash time: %s"
                    % (ret, time.time() - t0, time.time() - t1),
                    flush=True,
                )

    def refresh_client_if_should(self):
        if self.config is None:
            self.setup()
        # get current hash in order to update api_name -> fn_index map in case gradio server changed
        # FIXME: Could add cli api as hash
        server_hash = self.get_server_hash()
        if self.server_hash != server_hash:
            if self.verbose:
                print(
                    "server hash changed: %s %s" % (self.server_hash, server_hash),
                    flush=True,
                )
            if self.server_hash is not None and self.persist:
                if self.verbose:
                    print(
                        "Failed to persist due to server hash change, only kept chat_conversation not user session hash",
                        flush=True,
                    )
            # risky to persist if hash changed
            self.refresh_client()
            self.server_hash = server_hash

    def refresh_client(self):
        """
        Ensure every client call is independent
        Also ensure map between api_name and fn_index is updated in case server changed (e.g. restarted with new code)
        Returns:
        """
        if self.config is None:
            self.setup()

        kwargs = self.kwargs.copy()
        kwargs.pop("h2ogpt_key", None)
        kwargs.pop("persist", None)
        kwargs.pop("check_hash", None)
        kwargs.pop("check_model_name", None)
        kwargs.pop("include_heartbeat", None)
        ntrials = 3
        client = None
        for trial in range(0, ntrials):
            try:
                client = Client(*self.args, **kwargs)
                break
            except ValueError as e:
                if trial >= ntrials:
                    raise
                else:
                    if self.verbose:
                        print("Trying refresh %d/%d %s" % (trial, ntrials - 1, str(e)))
                    trial += 1
                    time.sleep(10)
        if client is None:
            raise RuntimeError("Failed to get new client")
        session_hash0 = self.session_hash if self.persist else None
        for k, v in client.__dict__.items():
            setattr(self, k, v)
        if session_hash0:
            # keep same system hash in case server API only changed and not restarted
            self.session_hash = session_hash0
        if self.verbose:
            print("Hit refresh_client(): %s %s" % (self.session_hash, session_hash0))
        # ensure server hash also updated
        self.server_hash = self.get_server_hash()

    def clone(self):
        if self.config is None:
            self.setup()
        client = GradioClient("")
        for k, v in self.__dict__.items():
            setattr(client, k, v)
        client.reset_session()

        self.get_endpoints(client)

        # transfer internals in case used
        client.server_hash = self.server_hash
        client.chat_conversation = self.chat_conversation
        return client

    def submit(
        self,
        *args,
        api_name: str | None = None,
        fn_index: int | None = None,
        result_callbacks: Callable | list[Callable] | None = None,
        exception_handling=True,  # new_stream = True, can make False, doesn't matter.
    ) -> Job:
        if self.config is None:
            self.setup()
        # Note predict calls submit
        try:
            self.refresh_client_if_should()
            job = super().submit(*args, api_name=api_name, fn_index=fn_index)
        except Exception as e:
            print("Hit e=%s\n\n%s" % (str(e), traceback.format_exc()), flush=True)
            # force reconfig in case only that
            self.refresh_client()
            job = super().submit(*args, api_name=api_name, fn_index=fn_index)

        if exception_handling:  # for debugging if causes issues
            # see if immediately failed
            e = check_job(job, timeout=0.01, raise_exception=False)
            if e is not None:
                print(
                    "GR job failed: %s %s"
                    % (str(e), "".join(traceback.format_tb(e.__traceback__))),
                    flush=True,
                )
                # force reconfig in case only that
                self.refresh_client()
                job = super().submit(*args, api_name=api_name, fn_index=fn_index)
                e2 = check_job(job, timeout=0.1, raise_exception=False)
                if e2 is not None:
                    print(
                        "GR job failed again: %s\n%s"
                        % (str(e2), "".join(traceback.format_tb(e2.__traceback__))),
                        flush=True,
                    )

        return job

    def question(self, instruction, *args, **kwargs) -> str:
        """
        Prompt LLM (direct to LLM with instruct prompting required for instruct models) and get response
        """
        kwargs["instruction"] = kwargs.get("instruction", instruction)
        kwargs["langchain_action"] = LangChainAction.QUERY.value
        kwargs["langchain_mode"] = "LLM"
        ret = ""
        for ret1 in self.query_or_summarize_or_extract(*args, **kwargs):
            ret = ret1.reply
        return ret

    def question_stream(self, instruction, *args, **kwargs) -> str:
        """
        Prompt LLM (direct to LLM with instruct prompting required for instruct models) and get response
        """
        kwargs["instruction"] = kwargs.get("instruction", instruction)
        kwargs["langchain_action"] = LangChainAction.QUERY.value
        kwargs["langchain_mode"] = "LLM"
        ret = yield from self.query_or_summarize_or_extract(*args, **kwargs)
        return ret

    def query(self, query, *args, **kwargs) -> str:
        """
        Search for documents matching a query, then ask that query to LLM with those documents
        """
        kwargs["instruction"] = kwargs.get("instruction", query)
        kwargs["langchain_action"] = LangChainAction.QUERY.value
        ret = ""
        for ret1 in self.query_or_summarize_or_extract(*args, **kwargs):
            ret = ret1.reply
        return ret

    def query_stream(
        self, query, *args, **kwargs
    ) -> Generator[tuple[str | list[str], list[str]], None, None]:
        """
        Search for documents matching a query, then ask that query to LLM with those documents
        """
        kwargs["instruction"] = kwargs.get("instruction", query)
        kwargs["langchain_action"] = LangChainAction.QUERY.value
        ret = yield from self.query_or_summarize_or_extract(*args, **kwargs)
        return ret

    def summarize(self, *args, query=None, focus=None, **kwargs) -> str:
        """
        Search for documents matching a focus, then ask a query to LLM with those documents
        If focus "" or None, no similarity search is done and all documents (up to top_k_docs) are used
        """
        kwargs["prompt_summary"] = kwargs.get(
            "prompt_summary", query or prompt_summary0
        )
        kwargs["instruction"] = kwargs.get("instruction", focus)
        kwargs["langchain_action"] = LangChainAction.SUMMARIZE_MAP.value
        ret = ""
        for ret1 in self.query_or_summarize_or_extract(*args, **kwargs):
            ret = ret1.reply
        return ret

    def summarize_stream(self, *args, query=None, focus=None, **kwargs) -> str:
        """
        Search for documents matching a focus, then ask a query to LLM with those documents
        If focus "" or None, no similarity search is done and all documents (up to top_k_docs) are used
        """
        kwargs["prompt_summary"] = kwargs.get(
            "prompt_summary", query or prompt_summary0
        )
        kwargs["instruction"] = kwargs.get("instruction", focus)
        kwargs["langchain_action"] = LangChainAction.SUMMARIZE_MAP.value
        ret = yield from self.query_or_summarize_or_extract(*args, **kwargs)
        return ret

    def extract(self, *args, query=None, focus=None, **kwargs) -> list[str]:
        """
        Search for documents matching a focus, then ask a query to LLM with those documents
        If focus "" or None, no similarity search is done and all documents (up to top_k_docs) are used
        """
        kwargs["prompt_extraction"] = kwargs.get(
            "prompt_extraction", query or prompt_extraction0
        )
        kwargs["instruction"] = kwargs.get("instruction", focus)
        kwargs["langchain_action"] = LangChainAction.EXTRACT.value
        ret = ""
        for ret1 in self.query_or_summarize_or_extract(*args, **kwargs):
            ret = ret1.reply
        return ret

    def extract_stream(self, *args, query=None, focus=None, **kwargs) -> list[str]:
        """
        Search for documents matching a focus, then ask a query to LLM with those documents
        If focus "" or None, no similarity search is done and all documents (up to top_k_docs) are used
        """
        kwargs["prompt_extraction"] = kwargs.get(
            "prompt_extraction", query or prompt_extraction0
        )
        kwargs["instruction"] = kwargs.get("instruction", focus)
        kwargs["langchain_action"] = LangChainAction.EXTRACT.value
        ret = yield from self.query_or_summarize_or_extract(*args, **kwargs)
        return ret

    def get_client_kwargs(self, **kwargs):
        client_kwargs = {}
        try:
            from src.evaluate_params import eval_func_param_names
        except ModuleNotFoundError:
            from .src.evaluate_params import eval_func_param_names

        for k in eval_func_param_names:
            if k in kwargs:
                client_kwargs[k] = kwargs[k]

        if os.getenv("HARD_ASSERTS"):
            fun_kwargs = {
                k: v.default
                for k, v in dict(
                    inspect.signature(self.query_or_summarize_or_extract).parameters
                ).items()
            }
            diff = set(eval_func_param_names).difference(fun_kwargs)
            assert len(diff) == 0, (
                "Add query_or_summarize_or_extract entries: %s" % diff
            )

            extra_query_params = [
                "file",
                "bad_error_string",
                "print_info",
                "asserts",
                "url",
                "prompt_extraction",
                "model",
                "text",
                "print_error",
                "pre_prompt_extraction",
                "embed",
                "print_warning",
                "sanitize_llm",
            ]
            diff = set(fun_kwargs).difference(
                eval_func_param_names + extra_query_params
            )
            assert len(diff) == 0, "Add eval_func_params entries: %s" % diff

        return client_kwargs

    def get_query_kwargs(self, **kwargs):
        fun_dict = dict(
            inspect.signature(self.query_or_summarize_or_extract).parameters
        ).items()
        fun_kwargs = {k: kwargs.get(k, v.default) for k, v in fun_dict}

        return fun_kwargs

    def query_or_summarize_or_extract(
        self,
        print_error=print,
        print_info=print,
        print_warning=print,
        bad_error_string=None,
        sanitize_llm=None,
        h2ogpt_key: str = None,
        instruction: str = "",
        text: list[str] | str | None = None,
        file: list[str] | str | None = None,
        url: list[str] | str | None = None,
        embed: bool = True,
        chunk: bool = True,
        chunk_size: int = 512,
        langchain_mode: str = None,
        langchain_action: str | None = None,
        langchain_agents: List[str] = [],
        top_k_docs: int = 10,
        document_choice: Union[str, List[str]] = "All",
        document_subset: str = "Relevant",
        document_source_substrings: Union[str, List[str]] = [],
        document_source_substrings_op: str = "and",
        document_content_substrings: Union[str, List[str]] = [],
        document_content_substrings_op: str = "and",
        system_prompt: str | None = "",
        pre_prompt_query: str | None = pre_prompt_query0,
        prompt_query: str | None = prompt_query0,
        pre_prompt_summary: str | None = pre_prompt_summary0,
        prompt_summary: str | None = prompt_summary0,
        pre_prompt_extraction: str | None = pre_prompt_extraction0,
        prompt_extraction: str | None = prompt_extraction0,
        hyde_llm_prompt: str | None = hyde_llm_prompt0,
        user_prompt_for_fake_system_prompt: str = None,
        json_object_prompt: str = None,
        json_object_prompt_simpler: str = None,
        json_code_prompt: str = None,
        json_code_prompt_if_no_schema: str = None,
        json_schema_instruction: str = None,
        model: str | int | None = None,
        stream_output: bool = False,
        do_sample: bool = False,
        seed: int | None = 0,
        temperature: float = 0.0,
        top_p: float = 1.0,
        top_k: int = 40,
        repetition_penalty: float = 1.07,
        penalty_alpha: float = 0.0,
        max_time: int = 360,
        max_new_tokens: int = 1024,
        add_search_to_context: bool = False,
        chat_conversation: list[tuple[str, str]] | None = None,
        text_context_list: list[str] | None = None,
        docs_ordering_type: str | None = None,
        min_max_new_tokens: int = 512,
        max_input_tokens: int = -1,
        max_total_input_tokens: int = -1,
        docs_token_handling: str = "split_or_merge",
        docs_joiner: str = "\n\n",
        hyde_level: int = 0,
        hyde_template: str = None,
        hyde_show_only_final: bool = True,
        doc_json_mode: bool = False,
        metadata_in_context: list = [],
        image_file: Union[str, list] = None,
        image_control: str = None,
        response_format: str = "text",
        guided_json: Union[str, dict] = "",
        guided_regex: str = "",
        guided_choice: str = "",
        guided_grammar: str = "",
        guided_whitespace_pattern: str = None,
        prompt_type: Union[int, str] = None,
        prompt_dict: Dict = None,
        jq_schema=".[]",
        llava_prompt: str = "auto",
        image_audio_loaders: list = None,
        url_loaders: list = None,
        pdf_loaders: list = None,
        extract_frames: int = 10,
        add_chat_history_to_context: bool = True,
        chatbot_role: str = "None",  # "Female AI Assistant",
        speaker: str = "None",  # "SLT (female)",
        tts_language: str = "autodetect",
        tts_speed: float = 1.0,
        visible_image_models: List[str] = [],
        visible_models: Union[str, int, list] = None,
        # don't use the below (no doc string stuff) block
        num_return_sequences: int = None,
        chat: bool = True,
        min_new_tokens: int = None,
        early_stopping: Union[bool, str] = None,
        iinput: str = "",
        iinput_nochat: str = "",
        instruction_nochat: str = "",
        context: str = "",
        num_beams: int = 1,
        asserts: bool = False,
    ) -> Generator[ReturnType, None, None]:
        """
        Query or Summarize or Extract using h2oGPT
        Args:
            instruction: Query for LLM chat.  Used for similarity search

            For query, prompt template is:
              "{pre_prompt_query}
                \"\"\"
                {content}
                \"\"\"
                {prompt_query}{instruction}"
             If added to summarization, prompt template is
              "{pre_prompt_summary}
                \"\"\"
                {content}
                \"\"\"
                Focusing on {instruction}, {prompt_summary}"
            text: textual content or list of such contents
            file: a local file to upload or files to upload
            url: a url to give or urls to use
            embed: whether to embed content uploaded

            :param langchain_mode: "LLM" to talk to LLM with no docs, "MyData" for personal docs, "UserData" for shared docs, etc.
            :param langchain_action: Action to take, "Query" or "Summarize" or "Extract"
            :param langchain_agents: Which agents to use, if any
            :param top_k_docs: number of document parts.
                        When doing query, number of chunks
                        When doing summarization, not related to vectorDB chunks that are not used
                        E.g. if PDF, then number of pages
            :param chunk: whether to chunk sources for document Q/A
            :param chunk_size: Size in characters of chunks
            :param document_choice: Which documents ("All" means all) -- need to use upload_api API call to get server's name if want to select
            :param document_subset: Type of query, see src/gen.py
            :param document_source_substrings: See gen.py
            :param document_source_substrings_op: See gen.py
            :param document_content_substrings: See gen.py
            :param document_content_substrings_op: See gen.py

            :param system_prompt: pass system prompt to models that support it.
              If 'auto' or None, then use automatic version
              If '', then use no system prompt (default)
            :param pre_prompt_query: Prompt that comes before document part
            :param prompt_query: Prompt that comes after document part
            :param pre_prompt_summary: Prompt that comes before document part
               None makes h2oGPT internally use its defaults
               E.g. "In order to write a concise single-paragraph or bulleted list summary, pay attention to the following text"
            :param prompt_summary: Prompt that comes after document part
              None makes h2oGPT internally use its defaults
              E.g. "Using only the text above, write a condensed and concise summary of key results (preferably as bullet points):\n"
            i.e. for some internal document part fstring, the template looks like:
                template = "%s
                \"\"\"
                %s
                \"\"\"
                %s" % (pre_prompt_summary, fstring, prompt_summary)
            :param hyde_llm_prompt: hyde prompt for first step when using LLM

            :param user_prompt_for_fake_system_prompt: user part of pre-conversation if LLM doesn't handle system prompt
            :param json_object_prompt: prompt for getting LLM to do JSON object
            :param json_object_prompt_simpler: simpler of "" for MistralAI
            :param json_code_prompt: prompt for getting LLm to do JSON in code block
            :param json_code_prompt_if_no_schema: prompt for getting LLM to do JSON in code block if no schema
            :param json_schema_instruction: prompt for LLM to use schema

            :param h2ogpt_key: Access Key to h2oGPT server (if not already set in client at init time)
            :param model: base_model name or integer index of model_lock on h2oGPT server
                            None results in use of first (0th index) model in server
                   to get list of models do client.list_models()
            :param pre_prompt_extraction: Same as pre_prompt_summary but for when doing extraction
            :param prompt_extraction: Same as prompt_summary but for when doing extraction
            :param do_sample: see src/gen.py
            :param seed: see src/gen.py
            :param temperature: see src/gen.py
            :param top_p: see src/gen.py
            :param top_k: see src/gen.py
            :param repetition_penalty: see src/gen.py
            :param penalty_alpha: see src/gen.py
            :param max_new_tokens: see src/gen.py
            :param min_max_new_tokens: see src/gen.py
            :param max_input_tokens: see src/gen.py
            :param max_total_input_tokens: see src/gen.py
            :param stream_output: Whether to stream output
            :param max_time: how long to take

            :param add_search_to_context: Whether to do web search and add results to context
            :param chat_conversation: List of tuples for (human, bot) conversation that will be pre-appended to an (instruction, None) case for a query
            :param text_context_list: List of strings to add to context for non-database version of document Q/A for faster handling via API etc.
               Forces LangChain code path and uses as many entries in list as possible given max_seq_len, with first assumed to be most relevant and to go near prompt.
            :param docs_ordering_type: By default uses 'reverse_ucurve_sort' for optimal retrieval
            :param max_input_tokens: Max input tokens to place into model context for each LLM call
                                     -1 means auto, fully fill context for query, and fill by original document chunk for summarization
                                     >=0 means use that to limit context filling to that many tokens
            :param max_total_input_tokens: like max_input_tokens but instead of per LLM call, applies across all LLM calls for single summarization/extraction action
            :param max_new_tokens: Maximum new tokens
            :param min_max_new_tokens: minimum value for max_new_tokens when auto-adjusting for content of prompt, docs, etc.

            :param docs_token_handling: 'chunk' means fill context with top_k_docs (limited by max_input_tokens or model_max_len) chunks for query
                                                                             or top_k_docs original document chunks summarization
                                        None or 'split_or_merge' means same as 'chunk' for query, while for summarization merges documents to fill up to max_input_tokens or model_max_len tokens
            :param docs_joiner: string to join lists of text when doing split_or_merge.  None means '\n\n'
            :param hyde_level: 0-3 for HYDE.
                        0 uses just query to find similarity with docs
                        1 uses query + pure LLM response to find similarity with docs
                        2: uses query + LLM response using docs to find similarity with docs
                        3+: etc.
            :param hyde_template: see src/gen.py
            :param hyde_show_only_final: see src/gen.py
            :param doc_json_mode: see src/gen.py
            :param metadata_in_context: see src/gen.py

            :param image_file: Initial image for UI (or actual image for CLI) Vision Q/A.  Or list of images for some models
            :param image_control: Initial image for UI Image Control

            :param response_format: text or json_object or json_code
            # https://github.com/vllm-project/vllm/blob/a3c226e7eb19b976a937e745f3867eb05f809278/vllm/entrypoints/openai/protocol.py#L117-L135
            :param guided_json:
            :param guided_regex:
            :param guided_choice:
            :param guided_grammar:
            :param guided_whitespace_pattern:

            :param prompt_type: type of prompt, usually matched to fine-tuned model or plain for foundational model
            :param prompt_dict: If prompt_type=custom, then expects (some) items returned by get_prompt(..., return_dict=True)

            :param jq_schema: control json loader
                   By default '.[]' ingests everything in brute-force way, but better to match your schema
                   See: https://python.langchain.com/docs/modules/data_connection/document_loaders/json#using-jsonloader

            :param extract_frames: How many unique frames to extract from video (if 0, then just do audio if audio type file as well)

            :param llava_prompt: Prompt passed to LLaVa for querying the image

            :param image_audio_loaders: which loaders to use for image and audio parsing (None means default)
            :param url_loaders: which loaders to use for url parsing (None means default)
            :param pdf_loaders: which loaders to use for pdf parsing (None means default)

            :param add_chat_history_to_context: Include chat context when performing action
                   Not supported when using CLI mode

            :param chatbot_role: Default role for coqui models.  If 'None', then don't by default speak when launching h2oGPT for coqui model choice.
            :param speaker: Default speaker for microsoft models  If 'None', then don't by default speak when launching h2oGPT for microsoft model choice.
            :param tts_language: Default language for coqui models
            :param tts_speed: Default speed of TTS, < 1.0 (needs rubberband) for slower than normal, > 1.0 for faster.  Tries to keep fixed pitch.

            :param visible_image_models: Which image gen models to include
            :param visible_models: Which models in model_lock list to show by default
                   Takes integers of position in model_lock (model_states) list or strings of base_model names
                   Ignored if model_lock not used
                   For nochat API, this is single item within a list for model by name or by index in model_lock
                                        If None, then just use first model in model_lock list
                                        If model_lock not set, use model selected by CLI --base_model etc.
                   Note that unlike h2ogpt_key, this visible_models only applies to this running h2oGPT server,
                      and the value is not used to access the inference server.
                      If need a visible_models for an inference server, then use --model_lock and group together.

            :param asserts: whether to do asserts to ensure handling is correct

        Returns: summary/answer: str or extraction List[str]

        """
        if self.config is None:
            self.setup()
        if self.persist:
            client = self
        else:
            client = self.clone()
        h2ogpt_key = h2ogpt_key or self.h2ogpt_key
        client.h2ogpt_key = h2ogpt_key

        if model is not None and visible_models is None:
            visible_models = model
        self.check_model(model)

        # chunking not used here
        # MyData specifies scratch space, only persisted for this individual client call
        langchain_mode = langchain_mode or "MyData"
        loaders = tuple([None, None, None, None, None, None])
        doc_options = tuple([langchain_mode, chunk, chunk_size, embed])
        asserts |= bool(os.getenv("HARD_ASSERTS", False))
        if (
            text
            and isinstance(text, list)
            and not file
            and not url
            and not text_context_list
        ):
            # then can do optimized text-only path
            text_context_list = text
            text = None

        res = []
        if text:
            t0 = time.time()
            res = client.predict(
                text, *doc_options, *loaders, h2ogpt_key, api_name="/add_text"
            )
            t1 = time.time()
            print_info("upload text: %s" % str(timedelta(seconds=t1 - t0)))
            if asserts:
                assert res[0] is None
                assert res[1] == langchain_mode
                assert "user_paste" in res[2]
                assert res[3] == ""
        if file:
            # upload file(s).  Can be list or single file
            # after below call, "file" replaced with remote location of file
            _, file = client.predict(file, api_name="/upload_api")

            res = client.predict(
                file, *doc_options, *loaders, h2ogpt_key, api_name="/add_file_api"
            )
            if asserts:
                assert res[0] is None
                assert res[1] == langchain_mode
                assert os.path.basename(file) in res[2]
                assert res[3] == ""
        if url:
            res = client.predict(
                url, *doc_options, *loaders, h2ogpt_key, api_name="/add_url"
            )
            if asserts:
                assert res[0] is None
                assert res[1] == langchain_mode
                assert url in res[2]
                assert res[3] == ""
                assert res[4]  # should have file name or something similar
        if res and not res[4] and "Exception" in res[2]:
            print_error("Exception: %s" % res[2])

        # ask for summary, need to use same client if using MyData
        api_name = "/submit_nochat_api"  # NOTE: like submit_nochat but stable API for string dict passing

        pre_prompt_summary = (
            pre_prompt_summary
            if langchain_action == LangChainAction.SUMMARIZE_MAP.value
            else pre_prompt_extraction
        )
        prompt_summary = (
            prompt_summary
            if langchain_action == LangChainAction.SUMMARIZE_MAP.value
            else prompt_extraction
        )

        chat_conversation = (
            chat_conversation if chat_conversation else self.chat_conversation.copy()
        )

        locals_for_client = locals().copy()
        locals_for_client.pop("self", None)
        client_kwargs = self.get_client_kwargs(**locals_for_client)

        # in case server changed, update in case clone()
        self.server_hash = client.server_hash

        # ensure can fill conversation
        self.chat_conversation.append((instruction, None))

        # get result
        actual_llm = None
        response = ""
        texts_out = []
        trials = 3
        t0 = time.time()
        time_to_first_token = None
        t_taken_s = None
        for trial in range(trials):
            t0 = time.time()
            try:
                if not stream_output:
                    res = client.predict(
                        str(dict(client_kwargs)),
                        api_name=api_name,
                    )
                    if time_to_first_token is None:
                        time_to_first_token = time.time() - t0
                    t_taken_s = time.time() - t0
                    # in case server changed, update in case clone()
                    self.server_hash = client.server_hash
                    res_dict = ast.literal_eval(res)
                    response = res_dict["response"]
                    if langchain_action != LangChainAction.EXTRACT.value:
                        response = response.strip()
                    else:
                        response = [r.strip() for r in ast.literal_eval(response)]
                    sources = res_dict["sources"]
                    scores_out = [x["score"] for x in sources]
                    texts_out = [x["content"] for x in sources]
                    prompt_raw = res_dict.get("prompt_raw", "")

                    try:
                        actual_llm = res_dict["save_dict"]["display_name"]  # fast path
                    except Exception as e:
                        print_warning(
                            f"Unable to access save_dict to get actual_llm: {str(e)}"
                        )
                        actual_llm = (
                            sanitize_llm(visible_models)
                            if sanitize_llm is not None
                            else visible_models
                        )

                    try:
                        extra_dict = res_dict["save_dict"]["extra_dict"]
                        input_tokens = extra_dict["num_prompt_tokens"]
                        output_tokens = extra_dict["ntokens"]
                        tokens_per_second = np.round(
                            extra_dict["tokens_persecond"], decimals=3
                        )
                    except:
                        if os.getenv("HARD_ASSERTS"):
                            raise
                        input_tokens = output_tokens = tokens_per_second = 0
                    if asserts:
                        if text and not file and not url:
                            assert any(
                                text[:cutoff] == texts_out
                                for cutoff in range(len(text))
                            )
                        assert len(texts_out) == len(scores_out)

                    yield ReturnType(
                        reply=response,
                        text_context_list=texts_out,
                        prompt_raw=prompt_raw,
                        actual_llm=actual_llm,
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        tokens_per_second=tokens_per_second,
                        time_to_first_token=time_to_first_token,
                    )

                    self.chat_conversation[-1] = (instruction, response)
                else:
                    job = client.submit(str(dict(client_kwargs)), api_name=api_name)
                    text0 = ""
                    while not job.done():
                        e = check_job(job, timeout=0, raise_exception=False)
                        if e is not None:
                            break
                        outputs_list = job.outputs().copy()
                        if outputs_list:
                            res = outputs_list[-1]
                            res_dict = ast.literal_eval(res)
                            response = res_dict["response"]  # keeps growing
                            prompt_raw = res_dict.get(
                                "prompt_raw", ""
                            )  # only filled at end
                            text_chunk = response[len(text0) :]  # only keep new stuff
                            if not text_chunk:
                                time.sleep(0.001)
                                continue
                            text0 = response
                            assert text_chunk, "must yield non-empty string"
                            if time_to_first_token is None:
                                time_to_first_token = time.time() - t0
                            yield ReturnType(reply=text_chunk)  # streaming part
                        time.sleep(0.005)

                    # Get final response (if anything left), but also get the actual references (texts_out), above is empty.
                    res_all = job.outputs().copy()
                    success = job.communicator.job.latest_status.success
                    timeout = 0.1 if success else 10
                    if len(res_all) > 0:
                        try:
                            check_job(job, timeout=timeout, raise_exception=True)
                        except (
                            Exception
                        ) as e:  # FIXME - except TimeoutError once h2ogpt raises that.
                            if "Abrupt termination of communication" in str(e):
                                actual_llm = (
                                    sanitize_llm(visible_models)
                                    if sanitize_llm is not None
                                    else visible_models
                                )
                                t_taken = "%.4f" % (time.time() - t0)
                                raise TimeoutError(
                                    f"LLM {actual_llm} timed out after {t_taken} seconds."
                                )
                            else:
                                raise

                        res = res_all[-1]
                        res_dict = ast.literal_eval(res)
                        response = res_dict["response"]
                        sources = res_dict["sources"]
                        prompt_raw = res_dict["prompt_raw"]
                        texts_out = [x["content"] for x in sources]
                        t_taken_s = time.time() - t0
                        t_taken = "%.4f" % t_taken_s

                        assert prompt_raw, "must have prompt_raw for final response"
                        if langchain_action != LangChainAction.EXTRACT.value:
                            text_chunk = response.strip()
                        else:
                            text_chunk = [r.strip() for r in ast.literal_eval(response)]

                        if not text_chunk:
                            actual_llm = (
                                sanitize_llm(visible_models)
                                if sanitize_llm is not None
                                else visible_models
                            )
                            raise TimeoutError(
                                f"No output from LLM {actual_llm} after {t_taken} seconds."
                            )

                        try:
                            extra_dict = res_dict["save_dict"]["extra_dict"]
                            input_tokens = extra_dict["num_prompt_tokens"]
                            output_tokens = extra_dict["ntokens"]
                            tokens_per_second = np.round(
                                extra_dict["tokens_persecond"], decimals=3
                            )
                        except:
                            if os.getenv("HARD_ASSERTS"):
                                raise
                            input_tokens = output_tokens = tokens_per_second = 0

                        try:
                            actual_llm = res_dict["save_dict"][
                                "display_name"
                            ]  # fast path
                        except Exception as e:
                            print_warning(
                                f"Unable to access save_dict to get actual_llm: {str(e)}"
                            )
                            actual_llm = (
                                sanitize_llm(visible_models)
                                if sanitize_llm is not None
                                else visible_models
                            )

                        if text_context_list:
                            assert texts_out, "No texts_out 1"

                        if time_to_first_token is None:
                            time_to_first_token = time.time() - t0
                        yield ReturnType(
                            reply=text_chunk,
                            text_context_list=texts_out,
                            prompt_raw=prompt_raw,
                            actual_llm=actual_llm,
                            input_tokens=input_tokens,
                            output_tokens=output_tokens,
                            tokens_per_second=tokens_per_second,
                            time_to_first_token=time_to_first_token,
                        )

                        self.chat_conversation[-1] = (
                            instruction,
                            text_chunk,
                        )
                    else:
                        assert not success
                        check_job(job, timeout=2.0 * timeout, raise_exception=True)
                break
            except Exception as e:
                print_error(
                    "h2oGPT predict failed: %s %s"
                    % (str(e), "".join(traceback.format_tb(e.__traceback__))),
                )
                if "invalid model" in str(e).lower():
                    raise
                if bad_error_string and bad_error_string in str(e):
                    # no need to do 3 trials if have disallowed stuff, unlikely that LLM will change its mind
                    raise
                if trial == trials - 1:
                    print_error("trying again failed: %s" % trial)
                    raise
                else:
                    # both Anthopic and openai gives this kind of error, but h2oGPT only has retries for OpenAI
                    if "Overloaded" in str(traceback.format_tb(e.__traceback__)):
                        sleep_time = 30 + 2 ** (trial + 1)
                    else:
                        sleep_time = 1 * trial
                    print_warning(
                        "trying again: %s in %s seconds" % (trial, sleep_time)
                    )
                    time.sleep(sleep_time)
            finally:
                # in case server changed, update in case clone()
                self.server_hash = client.server_hash

        t1 = time.time()
        print_info(
            dict(
                api="submit_nochat_api",
                streaming=stream_output,
                texts_in=len(text or []) + len(text_context_list or []),
                texts_out=len(texts_out),
                images=len(image_file)
                if isinstance(image_file, list)
                else 1
                if image_file
                else 0,
                response_time=str(timedelta(seconds=t1 - t0)),
                response_len=len(response),
                llm=visible_models,
                actual_llm=actual_llm,
            )
        )

    def check_model(self, model):
        if model != 0 and self.check_model_name:
            valid_llms = self.list_models()
            if (
                isinstance(model, int)
                and model >= len(valid_llms)
                or isinstance(model, str)
                and model not in valid_llms
            ):
                did_you_mean = ""
                if isinstance(model, str):
                    alt = difflib.get_close_matches(model, valid_llms, 1)
                    if alt:
                        did_you_mean = f"\nDid you mean {repr(alt[0])}?"
                raise RuntimeError(
                    f"Invalid llm: {repr(model)}, must be either an integer between "
                    f"0 and {len(valid_llms) - 1} or one of the following values: {valid_llms}.{did_you_mean}"
                )

    def get_models_full(self) -> list[dict[str, Any]]:
        """
        Full model info in list if dict
        """
        if self.config is None:
            self.setup()
        return ast.literal_eval(self.predict(api_name="/model_names"))

    def list_models(self) -> list[str]:
        """
        Model names available from endpoint
        """
        if self.config is None:
            self.setup()
        return [
            x["display_name"]
            for x in ast.literal_eval(self.predict(api_name="/model_names"))
        ]

    def simple_stream(
        self,
        client_kwargs={},
        api_name="/submit_nochat_api",
        prompt="",
        prompter=None,
        sanitize_bot_response=False,
        max_time=300,
        is_public=False,
        raise_exception=True,
        verbose=False,
    ):
        job = self.submit(str(dict(client_kwargs)), api_name=api_name)
        sources = []
        res_dict = dict(
            response="",
            sources=sources,
            save_dict={},
            llm_answers={},
            response_no_refs="",
            sources_str="",
            prompt_raw="",
        )
        yield res_dict
        text = ""
        text0 = ""
        strex = ""
        tgen0 = time.time()
        while not job.done():
            e = check_job(job, timeout=0, raise_exception=False)
            if e is not None:
                break
            outputs_list = job.outputs().copy()
            if outputs_list:
                res = outputs_list[-1]
                res_dict = ast.literal_eval(res)
                text = res_dict["response"]
                prompt_and_text = prompt + text
                if prompter:
                    response = prompter.get_response(
                        prompt_and_text,
                        prompt=prompt,
                        sanitize_bot_response=sanitize_bot_response,
                    )
                else:
                    response = text
                text_chunk = response[len(text0) :]
                if not text_chunk:
                    # just need some sleep for threads to switch
                    time.sleep(0.001)
                    continue
                # save old
                text0 = response
                res_dict.update(
                    dict(
                        response=response,
                        sources=sources,
                        error=strex,
                        response_no_refs=response,
                    )
                )
                yield res_dict
                if time.time() - tgen0 > max_time:
                    if verbose:
                        print(
                            "Took too long for Gradio: %s" % (time.time() - tgen0),
                            flush=True,
                        )
                    break
            time.sleep(0.005)
        # ensure get last output to avoid race
        res_all = job.outputs().copy()
        success = job.communicator.job.latest_status.success
        timeout = 0.1 if success else 10
        if len(res_all) > 0:
            # don't raise unless nochat API for now
            e = check_job(job, timeout=timeout, raise_exception=True)
            if e is not None:
                strex = "".join(traceback.format_tb(e.__traceback__))

            res = res_all[-1]
            res_dict = ast.literal_eval(res)
            text = res_dict["response"]
            sources = res_dict.get("sources")
            if sources is None:
                # then communication terminated, keep what have, but send error
                if is_public:
                    raise ValueError("Abrupt termination of communication")
                else:
                    raise ValueError("Abrupt termination of communication: %s" % strex)
        else:
            # if got no answer at all, probably something bad, always raise exception
            # UI will still put exception in Chat History under chat exceptions
            e = check_job(job, timeout=2.0 * timeout, raise_exception=True)
            # go with old text if last call didn't work
            if e is not None:
                stre = str(e)
                strex = "".join(traceback.format_tb(e.__traceback__))
            else:
                stre = ""
                strex = ""

            print(
                "Bad final response:%s %s %s: %s %s"
                % (res_all, prompt, text, stre, strex),
                flush=True,
            )
        prompt_and_text = prompt + text
        if prompter:
            response = prompter.get_response(
                prompt_and_text,
                prompt=prompt,
                sanitize_bot_response=sanitize_bot_response,
            )
        else:
            response = text
        res_dict.update(
            dict(
                response=response,
                sources=sources,
                error=strex,
                response_no_refs=response,
            )
        )
        yield res_dict
        return res_dict

    def stream(
        self,
        client_kwargs={},
        api_name="/submit_nochat_api",
        prompt="",
        prompter=None,
        sanitize_bot_response=False,
        max_time=None,
        is_public=False,
        raise_exception=True,
        verbose=False,
    ):
        strex = ""
        e = None
        res_dict = {}
        try:
            res_dict = yield from self._stream(
                client_kwargs,
                api_name=api_name,
                prompt=prompt,
                prompter=prompter,
                sanitize_bot_response=sanitize_bot_response,
                max_time=max_time,
                verbose=verbose,
            )
        except Exception as e:
            strex = "".join(traceback.format_tb(e.__traceback__))
            # check validity of final results and check for timeout
            # NOTE: server may have more before its timeout, and res_all will have more if waited a bit
            if raise_exception:
                raise

        if "timeout" in res_dict["save_dict"]["extra_dict"]:
            timeout_time = res_dict["save_dict"]["extra_dict"]["timeout"]
            raise TimeoutError(
                "Timeout from local after %s %s"
                % (timeout_time, ": " + strex if e else "")
            )

        # won't have sources if timed out
        if res_dict.get("sources") is None:
            # then communication terminated, keep what have, but send error
            if is_public:
                raise ValueError("Abrupt termination of communication")
            else:
                raise ValueError("Abrupt termination of communication: %s" % strex)
        return res_dict

    def _stream(
        self,
        client_kwargs,
        api_name="/submit_nochat_api",
        prompt="",
        prompter=None,
        sanitize_bot_response=False,
        max_time=None,
        verbose=False,
    ):
        job = self.submit(str(dict(client_kwargs)), api_name=api_name)

        text = ""
        sources = []
        save_dict = {}
        save_dict["extra_dict"] = {}
        res_dict = dict(
            response=text,
            sources=sources,
            save_dict=save_dict,
            llm_answers={},
            response_no_refs=text,
            sources_str="",
            prompt_raw="",
        )
        yield res_dict

        text0 = ""
        tgen0 = time.time()
        n = 0
        for res in job:
            res_dict, text0 = yield from self.yield_res(
                res,
                res_dict,
                prompt,
                prompter,
                sanitize_bot_response,
                max_time,
                text0,
                tgen0,
                verbose,
            )
            n += 1
            if "timeout" in res_dict["save_dict"]["extra_dict"]:
                break
        # final res
        outputs = job.outputs().copy()
        all_n = len(outputs)
        for nn in range(n, all_n):
            res = outputs[nn]
            res_dict, text0 = yield from self.yield_res(
                res,
                res_dict,
                prompt,
                prompter,
                sanitize_bot_response,
                max_time,
                text0,
                tgen0,
                verbose,
            )
        return res_dict

    @staticmethod
    def yield_res(
        res,
        res_dict,
        prompt,
        prompter,
        sanitize_bot_response,
        max_time,
        text0,
        tgen0,
        verbose,
    ):
        do_yield = True
        res_dict_server = ast.literal_eval(res)
        # yield what have
        text = res_dict_server["response"]
        if text is None:
            print("text None", flush=True)
            text = ""
        if prompter:
            response = prompter.get_response(
                prompt + text,
                prompt=prompt,
                sanitize_bot_response=sanitize_bot_response,
            )
        else:
            response = text
        text_chunk = response[len(text0) :]
        if not text_chunk:
            # just need some sleep for threads to switch
            time.sleep(0.001)
            do_yield = False
        # save old
        text0 = response
        res_dict.update(res_dict_server)
        res_dict.update(dict(response=response, response_no_refs=response))

        timeout_time_other = (
            res_dict.get("save_dict", {}).get("extra_dict", {}).get("timeout")
        )
        if timeout_time_other:
            if verbose:
                print(
                    "Took too long for other Gradio: %s" % (time.time() - tgen0),
                    flush=True,
                )
            return res_dict, text0

        timeout_time = time.time() - tgen0
        if max_time is not None and timeout_time > max_time:
            if "save_dict" not in res_dict:
                res_dict["save_dict"] = {}
            if "extra_dict" not in res_dict["save_dict"]:
                res_dict["save_dict"]["extra_dict"] = {}
            res_dict["save_dict"]["extra_dict"]["timeout"] = timeout_time
            yield res_dict
            if verbose:
                print(
                    "Took too long for Gradio: %s" % (time.time() - tgen0), flush=True
                )
            return res_dict, text0
        if do_yield:
            yield res_dict
            time.sleep(0.005)
        return res_dict, text0
