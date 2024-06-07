
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

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class GetDhConfig(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``26CF8950``

version (``int`` ``32-bit``):
                    N/A
                
        random_length (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.DhConfig<typegram.api.ayiin.messages.DhConfig>`
    """

    __slots__: List[str] = ["version", "random_length"]

    ID = 0x26cf8950
    QUALNAME = "functions.functionsmessages.DhConfig"

    def __init__(self, *, version: int, random_length: int) -> None:
        
                self.version = version  # int
        
                self.random_length = random_length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDhConfig":
        # No flags
        
        version = Int.read(b)
        
        random_length = Int.read(b)
        
        return GetDhConfig(version=version, random_length=random_length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.version))
        
        b.write(Int(self.random_length))
        
        return b.getvalue()