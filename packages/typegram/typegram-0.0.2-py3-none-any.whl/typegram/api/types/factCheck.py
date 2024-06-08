
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



class FactCheck(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.FactCheck`.

    Details:
        - Layer: ``181``
        - ID: ``B89BFCCF``

hash (``int`` ``64-bit``):
                    N/A
                
        need_check (``bool``, *optional*):
                    N/A
                
        country (``str``, *optional*):
                    N/A
                
        text (:obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getFactCheck
    """

    __slots__: List[str] = ["hash", "need_check", "country", "text"]

    ID = 0xb89bfccf
    QUALNAME = "types.factCheck"

    def __init__(self, *, hash: int, need_check: Optional[bool] = None, country: Optional[str] = None, text: "api.ayiin.TextWithEntities" = None) -> None:
        
                self.hash = hash  # long
        
                self.need_check = need_check  # true
        
                self.country = country  # string
        
                self.text = text  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FactCheck":
        
        flags = Int.read(b)
        
        need_check = True if flags & (1 << 0) else False
        country = String.read(b) if flags & (1 << 1) else None
        text = Object.read(b) if flags & (1 << 1) else None
        
        hash = Long.read(b)
        
        return FactCheck(hash=hash, need_check=need_check, country=country, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.country is not None:
            b.write(String(self.country))
        
        if self.text is not None:
            b.write(self.text.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()