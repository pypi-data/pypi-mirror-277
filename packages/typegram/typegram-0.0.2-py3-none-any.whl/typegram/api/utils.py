# !
# ? Pyrogram - Telegram MTProto API Client Library for Python
# ? Copyright (C) 2017-present Dan <https://github.com/delivrance>
# ? This file is part of Pyrogram.
# ? 
# ? ===========================================================
# ?             Copyright (C) 2023-present AyiinXd
# ? ===========================================================
# ? ||                                                       ||
# ? ||              _         _ _      __  __   _            ||
# ? ||             / \  _   _(_|_)_ __ \ \/ /__| |           ||
# ? ||            / _ \| | | | | | '_ \ \  // _` |           ||
# ? ||           / ___ \ |_| | | | | | |/  \ (_| |           ||
# ? ||          /_/   \_\__, |_|_|_| |_/_/\_\__,_|           ||
# ? ||                  |___/                                ||
# ? ||                                                       ||
# ? ===========================================================
# ?  Appreciating the work of others is not detrimental to you
# ? ===========================================================


from io import BytesIO
from struct import unpack, pack
from typing import Any, List, Union, cast

from .object import Object


class BoolFalse(bytes, Object):
    ID = 0xBC799737
    value = False

    @classmethod
    def read(cls, *args: Any) -> bool:
        return cls.value

    def __new__(cls) -> bytes:  # type: ignore
        return cls.ID.to_bytes(4, "little")


class BoolTrue(BoolFalse):
    ID = 0x997275B5
    value = True


class Bool(bytes, Object):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bool:
        return int.from_bytes(data.read(4), "little") == BoolTrue.ID

    def __new__(cls, value: bool) -> bytes:  # type: ignore
        return BoolTrue() if value else BoolFalse()


class Bytes(bytes, Object):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> bytes:
        length = int.from_bytes(data.read(1), "little")

        if length <= 253:
            x = data.read(length)
            data.read(-(length + 1) % 4)
        else:
            length = int.from_bytes(data.read(3), "little")
            x = data.read(length)
            data.read(-length % 4)

        return x

    def __new__(cls, value: bytes) -> bytes:  # type: ignore
        length = len(value)

        if length <= 253:
            return (
                bytes([length])
                + value
                + bytes(-(length + 1) % 4)
            )
        else:
            return (
                bytes([254])
                + length.to_bytes(3, "little")
                + value
                + bytes(-length % 4)
            )


class Double(bytes, Object):
    @classmethod
    def read(cls, data: BytesIO, *args: Any) -> float:
        return cast(float, unpack("d", data.read(8))[0])

    def __new__(cls, value: float) -> bytes:  # type: ignore
        return pack("d", value)


class Int(bytes, Object):
    SIZE = 4

    @classmethod
    def read(cls, data: BytesIO, signed: bool = True, *args: Any) -> int:
        return int.from_bytes(data.read(cls.SIZE), "little", signed=signed)

    def __new__(cls, value: int, signed: bool = True) -> bytes:  # type: ignore
        return value.to_bytes(cls.SIZE, "little", signed=signed)


class Long(Int):
    SIZE = 8


class Int128(Int):
    SIZE = 16


class Int256(Int):
    SIZE = 32


class String(Bytes):
    @classmethod
    def read(cls, data: BytesIO, *args) -> str:  # type: ignore
        return cast(bytes, super(String, String).read(data)).decode(errors="replace")

    def __new__(cls, value: str) -> bytes:  # type: ignore
        return super().__new__(cls, value.encode())


class Vector(bytes, Object):
    ID = 0x1CB5C415

    # Method added to handle the special case when a query returns a bare Vector (of Ints);
    # i.e., RpcResult body starts with 0x1cb5c415 (Vector Id) - e.g., messages.GetMessagesViews.
    @staticmethod
    def read_bare(b: BytesIO, size: int) -> Union[int, Any]:
        if size == 4:
            return Int.read(b)

        if size == 8:
            return Long.read(b)

        return Object.read(b)

    @classmethod
    def read(cls, data: BytesIO, t: Any = None, *args: Any) -> List:
        count = Int.read(data)
        left = len(data.read())
        size = (left / count) if count else 0
        data.seek(-left, 1)

        return List(
            t.read(data) if t
            else Vector.read_bare(data, size)
            for _ in range(count)
        )

    def __new__(cls, value: list, t: Any = None) -> bytes:  # type: ignore
        return b"".join(
            [Int(cls.ID, False), Int(len(value))]
            + [cast(bytes, t(i)) if t else i.write() for i in value]
        )
