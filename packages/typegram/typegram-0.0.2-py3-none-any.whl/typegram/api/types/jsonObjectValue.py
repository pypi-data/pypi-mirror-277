
#===========================================================
#            Copyright (C) 2023-present AyiinXd
#===========================================================
#||                                                       ||
#||              _         _ _      __  __   _            ||
#||             /   _   _(_|_)_ __  / /__| |           ||
#||            / _ | | | | | | '_     _  | |           ||
#||           / ___  |_| | | | | | |/   (_| |           ||
#||          /_/   ___, |_|_|_| |_/_/___,_|           ||
#||                  |___/                                ||
#||                                                       ||
#===========================================================
# Appreciating the work of others is not detrimental to you
#===========================================================
#

from io import BytesIO
from typing import Any, Union, List, Optional

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class JsonObjectValue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.JSONObjectValue`.

    Details:
        - Layer: ``181``
        - ID: ``C0DE1BD9``

key (``str``):
                    N/A
                
        value (:obj:`JSONValue<typegram.api.ayiin.JSONValue>`):
                    N/A
                
    """

    __slots__: List[str] = ["key", "value"]

    ID = 0xc0de1bd9
    QUALNAME = "types.jsonObjectValue"

    def __init__(self, *, key: str, value: "api.ayiin.JSONValue") -> None:
        
                self.key = key  # string
        
                self.value = value  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JsonObjectValue":
        # No flags
        
        key = String.read(b)
        
        value = Object.read(b)
        
        return JsonObjectValue(key=key, value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.key))
        
        b.write(self.value.write())
        
        return b.getvalue()