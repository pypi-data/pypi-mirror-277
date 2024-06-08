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
from json import dumps
from typing import cast, List, Any, Union, Dict

from .all import objects

class Object:
    __slots__: List[str] = []

    QUALNAME = "Base"

    @classmethod
    def read(cls, b: BytesIO, *args: Any) -> Any:
        return cast(Object, objects[int.from_bytes(b.read(4), "little")]).read(b, *args)

    def write(self, *args: Any) -> bytes:
        pass

    @staticmethod
    def default(obj: "Object") -> Union[str, Dict[str, str]]:
        if isinstance(obj, bytes):
            return repr(obj)

        return {
            "_": obj.QUALNAME,
            **{
                attr: getattr(obj, attr)
                for attr in obj.__slots__
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        if not hasattr(self, "QUALNAME"):
            return repr(self)

        return "typegram.api.{}({})".format(
            self.QUALNAME,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in self.__slots__
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: Any) -> bool:
        for attr in self.__slots__:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __len__(self) -> int:
        return len(self.write())

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        pass
