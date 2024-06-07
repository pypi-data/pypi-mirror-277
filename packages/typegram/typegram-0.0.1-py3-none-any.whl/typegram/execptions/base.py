# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-present Dan <https://github.com/delivrance>
# This file is part of Pyrogram.
# 
# ===========================================================
#             Copyright (C) 2023-present AyiinXd
# ===========================================================
# ||                                                       ||
# ||              _         _ _      __  __   _            ||
# ||             / \  _   _(_|_)_ __ \ \/ /__| |           ||
# ||            / _ \| | | | | | '_ \ \  // _` |           ||
# ||           / ___ \ |_| | | | | | |/  \ (_| |           ||
# ||          /_/   \_\__, |_|_|_| |_/_/\_\__,_|           ||
# ||                  |___/                                ||
# ||                                                       ||
# ===========================================================
#  Appreciating the work of others is not detrimental to you
# ===========================================================


import re
from datetime import datetime
from importlib import import_module
from typing import Type, Union, Optional

import typegram
from typegram.api.object import Object
from typegram.api.types import rpcError

from .all import allError


class GrambotError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class BaseError(GrambotError):
    ID = None
    CODE = None
    NAME = None
    MESSAGE = "{value}"

    def __init__(
        self,
        client: Optional['typegram.Robot'] = None,
        value: Union[int, str, rpcError.RpcError] = None,
        rpc_name: str = None,
        is_unknown: bool = False,
        is_signed: bool = False
    ):
        super().__init__("Telegram says: [{}] [{}{} {}] - {} {}".format(
            client.me.id if client and client.me else "XD",
            "-" if is_signed else "",
            self.CODE,
            self.ID or self.NAME,
            self.MESSAGE.format(value=value),
            f'(caused by "{rpc_name}")' if rpc_name else ""
        ))

        try:
            self.value = int(value)
        except (ValueError, TypeError):
            self.value = value

        if is_unknown:
            with open("unknown_errors.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}\t{value}\t{rpc_name}\n")

    @staticmethod
    def raise_it(client: "typegram.Robot", rpc_error: "rpcError.RpcError", rpc_type: Type[Object]):
        error_code = rpc_error.error_code
        is_signed = error_code < 0
        error_message = rpc_error.error_message
        rpc_name = ".".join(rpc_type.QUALNAME.split(".")[1:])

        if is_signed:
            error_code = -error_code

        if error_code not in allError:
            raise UnknownError(
                value=f"[{error_code} {error_message}]",
                rpc_name=rpc_name,
                is_unknown=True,
                is_signed=is_signed
            )

        error_id = re.sub(r"_\d+", "_X", error_message)

        if error_id not in allError[error_code]:
            raise getattr(
                import_module("techgram.errors"),
                allError[error_code]["_"]
            )(client=client,
              value=f"[{error_code} {error_message}]",
              rpc_name=rpc_name,
              is_unknown=True,
              is_signed=is_signed)

        value = re.search(r"_(\d+)", error_message)
        value = value.group(1) if value is not None else value

        raise getattr(
            import_module("techgram.errors"),
            allError[error_code][error_id]
        )(client=client,
          value=value,
          rpc_name=rpc_name,
          is_unknown=False,
          is_signed=is_signed)


class UnknownError(BaseError):
    CODE = 520
    """:obj:`int`: Error code"""
    NAME = "Unknown error"


class CacheException(GrambotError):
    def __init__(self, message: str):
        super().__init__(message)


class InitializationException(GrambotError):
    def __init__(self, message: str):
        super().__init__(message)

class TimedOut(GrambotError):
    def __init__(self, message: str):
        super().__init__("TimeOut Error: {}".format(message))