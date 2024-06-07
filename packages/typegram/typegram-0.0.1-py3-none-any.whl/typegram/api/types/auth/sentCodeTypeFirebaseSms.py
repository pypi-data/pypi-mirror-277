
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



class SentCodeTypeFirebaseSms(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``13C90F17``

length (``int`` ``32-bit``):
                    N/A
                
        nonce (``bytes``, *optional*):
                    N/A
                
        play_integrity_nonce (``bytes``, *optional*):
                    N/A
                
        receipt (``str``, *optional*):
                    N/A
                
        push_timeout (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.SentCode
            auth.Authorization
            auth.ExportedAuthorization
            auth.LoginToken
    """

    __slots__: List[str] = ["length", "nonce", "play_integrity_nonce", "receipt", "push_timeout"]

    ID = 0x13c90f17
    QUALNAME = "functions.typesauth.SentCodeType"

    def __init__(self, *, length: int, nonce: Optional[bytes] = None, play_integrity_nonce: Optional[bytes] = None, receipt: Optional[str] = None, push_timeout: Optional[int] = None) -> None:
        
                self.length = length  # int
        
                self.nonce = nonce  # bytes
        
                self.play_integrity_nonce = play_integrity_nonce  # bytes
        
                self.receipt = receipt  # string
        
                self.push_timeout = push_timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFirebaseSms":
        
        flags = Int.read(b)
        
        nonce = Bytes.read(b) if flags & (1 << 0) else None
        play_integrity_nonce = Bytes.read(b) if flags & (1 << 2) else None
        receipt = String.read(b) if flags & (1 << 1) else None
        push_timeout = Int.read(b) if flags & (1 << 1) else None
        length = Int.read(b)
        
        return SentCodeTypeFirebaseSms(length=length, nonce=nonce, play_integrity_nonce=play_integrity_nonce, receipt=receipt, push_timeout=push_timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.nonce is not None:
            b.write(Bytes(self.nonce))
        
        if self.play_integrity_nonce is not None:
            b.write(Bytes(self.play_integrity_nonce))
        
        if self.receipt is not None:
            b.write(String(self.receipt))
        
        if self.push_timeout is not None:
            b.write(Int(self.push_timeout))
        
        b.write(Int(self.length))
        
        return b.getvalue()