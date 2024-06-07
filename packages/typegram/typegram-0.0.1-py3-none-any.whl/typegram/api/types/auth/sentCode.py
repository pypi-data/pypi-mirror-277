
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



class SentCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCode`.

    Details:
        - Layer: ``181``
        - ID: ``5E002502``

type (:obj:`auth.SentCodeType<typegram.api.ayiin.auth.SentCodeType>`):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        next_type (:obj:`auth.CodeType<typegram.api.ayiin.auth.CodeType>`, *optional*):
                    N/A
                
        timeout (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["type", "phone_code_hash", "next_type", "timeout"]

    ID = 0x5e002502
    QUALNAME = "functions.typesauth.SentCode"

    def __init__(self, *, type: "ayiinauth.SentCodeType", phone_code_hash: str, next_type: "ayiinauth.CodeType" = None, timeout: Optional[int] = None) -> None:
        
                self.type = type  # auth.SentCodeType
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.next_type = next_type  # auth.CodeType
        
                self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCode":
        
        flags = Int.read(b)
        
        type = Object.read(b)
        
        phone_code_hash = String.read(b)
        
        next_type = Object.read(b) if flags & (1 << 1) else None
        
        timeout = Int.read(b) if flags & (1 << 2) else None
        return SentCode(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        b.write(String(self.phone_code_hash))
        
        if self.next_type is not None:
            b.write(self.next_type.write())
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        return b.getvalue()