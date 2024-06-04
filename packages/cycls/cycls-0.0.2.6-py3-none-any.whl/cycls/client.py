from __future__ import annotations
from inspect import signature, Parameter, _empty
from typing import Callable, Any
from datetime import datetime
from functools import wraps

from socketio import AsyncClient, Client  # type: ignore[import-untyped]
import asyncio
import re

from .UI import Text, Image
from .configuration import AppConfiguration
from .typings import (
    InputTypeHint,
    AsyncContext,
    SyncContext,
    ConversationID,
    ConversationSession,
    Response,
    Message,
    MessageContent,
)
from .static import HANDLER_PATTERN, CYCLS_URL


class BaseApp:
    key: str
    app_config: AppConfiguration

    def __init__(
        self,
        secret: str,
        handler: str,
        name: str | None = None,
        image: str | None = None,
        welcome: str | None = None,
        suggestions: list[str] | None = None,
        **kwargs,
    ):
        self.key = secret
        app_handler = self.__extract_handler_name(handler)
        self.app_config = AppConfiguration(
            handler=app_handler,
            name=name,
            image=image,
            introduction=welcome,
            suggestions=suggestions,
        )
        self.server_url = kwargs.get("cycls_url", CYCLS_URL)

    def _process_response(self, response):
        if isinstance(response, Response):
            return response
        elif isinstance(response, Text) or isinstance(response, Image):
            return Response(messages=[response])
        elif isinstance(response, list):
            return Response(messages=response)
        return Response(messages=[response])

    def _parameter_type_hint(self, param: Parameter) -> InputTypeHint:
        hint = param.annotation
        mapping = {
            _empty: InputTypeHint.EMPTY,
            Message: InputTypeHint.MESSAGE,
            ConversationSession: InputTypeHint.SESSION,
            ConversationID: InputTypeHint.CONVERSATION_ID,
            AsyncContext: InputTypeHint.FULL,
            MessageContent: InputTypeHint.MESSAGE_CONTENT,
        }
        if output := mapping.get(hint):
            return output
        else:
            raise Exception("")

    def _get_parameter_value(
        self, hint: InputTypeHint, obj: AsyncContext | SyncContext
    ) -> Any:
        if hint == InputTypeHint.MESSAGE_CONTENT:
            return obj.message.content
        elif hint == InputTypeHint.SESSION:
            return obj
        elif hint == InputTypeHint.CONVERSATION_ID:
            return obj.id
        elif hint == InputTypeHint.MESSAGE:
            return obj.message
        elif hint == InputTypeHint.USER:
            return None
        elif hint == InputTypeHint.EMPTY or hint == InputTypeHint.FULL:
            return obj

    def process_handler_input(
        self, func: Callable, message: AsyncContext | SyncContext
    ):
        kwargs = {}
        for key, value in signature(func).parameters.items():
            type_hint = self._parameter_type_hint(value)
            kwargs[key] = self._get_parameter_value(hint=type_hint, obj=message)
        return kwargs

    def __extract_handler_name(self, handler: str) -> str:
        name = re.search(rf"^\@({HANDLER_PATTERN})$", handler.strip().lower())
        if not name:
            raise Exception(
                "Your app handler has to start with @ and composed only of letters, numbers and '-'"
            )
        return re.sub(r"_", "-", name.group(1))

    def connection_log(self, data):
        print(
            f"{datetime.now()}: HANDLER|{data.get('handler')} -> {data.get('message')}. STATUS: {data.get('status')}"
        )


class App(BaseApp):
    def __init__(
        self,
        secret: str,
        handler: str,
        name: str | None = None,
        image: str | None = None,
        welcome: str | None = None,
        suggestions: list[str] | None = None,
        **kwargs,
    ):
        super().__init__(
            secret=secret,
            handler=handler,
            name=name,
            image=image,
            welcome=welcome,
            suggestions=suggestions,
            **kwargs,
        )
        self.sio = Client(
            reconnection_attempts=0,
            reconnection_delay=1,
            reconnection_delay_max=25,
        )
        self.sio.on("connect")(self.re_connect)
        self.sio.on("connection_log")(self.connection_log)

    def re_connect(self):
        self.sio.emit("connect_app", data=self.app_config.model_dump(mode="json"))

    def _run(self):
        headers = {
            "x-dev-secret": self.key,
        }
        self.sio.connect(
            self.server_url,
            headers=headers,
            transports=["websocket"],
            socketio_path="/app-socket/socket.io",
        )
        self.sio.wait()

    def publish(self):
        self._run()

    def __run_app(self, func, message):
        func(**self.process_handler_input(func, message))
        message.send.finish(message.send.user_message_id)

    def __call__(self, func):
        @wraps
        @self.sio.on(self.app_config.handler)
        def wrapper(data):
            message = SyncContext(sio=self.sio, url=self.server_url, **data)
            self.sio.start_background_task(self.__run_app, func, message)

        return wrapper


class AsyncApp(BaseApp):
    sio: AsyncClient

    def __init__(
        self,
        secret: str,
        handler: str,
        name: str | None = None,
        image: str | None = None,
        welcome: str | None = None,
        suggestions: list[str] | None = None,
        **kwargs,
    ):
        super().__init__(
            secret=secret,
            handler=handler,
            name=name,
            image=image,
            welcome=welcome,
            suggestions=suggestions,
            **kwargs,
        )
        self.sio = AsyncClient(
            reconnection_attempts=0, reconnection_delay=1, reconnection_delay_max=25
        )
        self.sio.on("connect")(self.re_connect)
        self.sio.on("connection_log")(self.connection_log)

    async def re_connect(self):
        await self.sio.emit("connect_app", data=self.app_config.model_dump(mode="json"))

    async def _run(self):
        headers = {
            "x-dev-secret": self.key,
        }
        await self.sio.connect(
            self.server_url,
            headers=headers,
            transports=["websocket"],
            socketio_path="/app-socket/socket.io",
        )
        await self.sio.wait()

    def publish(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self._run())

    async def __run_app(self, func, message):
        await func(**self.process_handler_input(func, message))
        await asyncio.sleep(0.2)
        await message.send.finish(message.send.user_message_id)

    def __call__(self, func):
        @wraps
        @self.sio.on(self.app_config.handler)
        async def wrapper(data):
            message = AsyncContext(sio=self.sio, url=self.server_url, **data)
            await self.sio.start_background_task(self.__run_app, func, message)

        return wrapper
