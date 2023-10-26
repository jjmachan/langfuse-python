# This file was auto-generated by Fern from our API Definition.

import typing

import httpx


class BaseClientWrapper:
    def __init__(
        self,
        *,
        x_langfuse_sdk_name: typing.Optional[str] = None,
        x_langfuse_sdk_version: typing.Optional[str] = None,
        x_langfuse_public_key: typing.Optional[str] = None,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        base_url: str
    ):
        self._x_langfuse_sdk_name = x_langfuse_sdk_name
        self._x_langfuse_sdk_version = x_langfuse_sdk_version
        self._x_langfuse_public_key = x_langfuse_public_key
        self._username = username
        self._password = password
        self._base_url = base_url

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {"X-Fern-Language": "Python"}
        headers["Authorization"] = httpx.BasicAuth(self._get_username(), self._get_password())._auth_header
        if self._x_langfuse_sdk_name is not None:
            headers["X-Langfuse-Sdk-Name"] = self._x_langfuse_sdk_name
        if self._x_langfuse_sdk_version is not None:
            headers["X-Langfuse-Sdk-Version"] = self._x_langfuse_sdk_version
        if self._x_langfuse_public_key is not None:
            headers["X-Langfuse-Public-Key"] = self._x_langfuse_public_key
        return headers

    def _get_username(self) -> str:
        if isinstance(self._username, str):
            return self._username
        else:
            return self._username()

    def _get_password(self) -> str:
        if isinstance(self._password, str):
            return self._password
        else:
            return self._password()

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        x_langfuse_sdk_name: typing.Optional[str] = None,
        x_langfuse_sdk_version: typing.Optional[str] = None,
        x_langfuse_public_key: typing.Optional[str] = None,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        httpx_client: httpx.Client
    ):
        super().__init__(
            x_langfuse_sdk_name=x_langfuse_sdk_name,
            x_langfuse_sdk_version=x_langfuse_sdk_version,
            x_langfuse_public_key=x_langfuse_public_key,
            username=username,
            password=password,
            base_url=base_url,
        )
        self.httpx_client = httpx_client


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        x_langfuse_sdk_name: typing.Optional[str] = None,
        x_langfuse_sdk_version: typing.Optional[str] = None,
        x_langfuse_public_key: typing.Optional[str] = None,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        httpx_client: httpx.AsyncClient
    ):
        super().__init__(
            x_langfuse_sdk_name=x_langfuse_sdk_name,
            x_langfuse_sdk_version=x_langfuse_sdk_version,
            x_langfuse_public_key=x_langfuse_public_key,
            username=username,
            password=password,
            base_url=base_url,
        )
        self.httpx_client = httpx_client
