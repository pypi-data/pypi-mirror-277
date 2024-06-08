
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



class DhConfig(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.DhConfig`.

    Details:
        - Layer: ``181``
        - ID: ``2C221EDD``

g (``int`` ``32-bit``):
                    N/A
                
        p (``bytes``):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
        random (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getDhConfig
    """

    __slots__: List[str] = ["g", "p", "version", "random"]

    ID = 0x2c221edd
    QUALNAME = "types.messages.dhConfig"

    def __init__(self, *, g: int, p: bytes, version: int, random: bytes) -> None:
        
                self.g = g  # int
        
                self.p = p  # bytes
        
                self.version = version  # int
        
                self.random = random  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DhConfig":
        # No flags
        
        g = Int.read(b)
        
        p = Bytes.read(b)
        
        version = Int.read(b)
        
        random = Bytes.read(b)
        
        return DhConfig(g=g, p=p, version=version, random=random)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.g))
        
        b.write(Bytes(self.p))
        
        b.write(Int(self.version))
        
        b.write(Bytes(self.random))
        
        return b.getvalue()