
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



class SendCode(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A677244F``

phone_number (``str``):
                    N/A
                
        api_id (``int`` ``32-bit``):
                    N/A
                
        api_hash (``str``):
                    N/A
                
        settings (:obj:`CodeSettings<typegram.api.ayiin.CodeSettings>`):
                    N/A
                
    Returns:
        :obj:`auth.SentCode<typegram.api.ayiin.auth.SentCode>`
    """

    __slots__: List[str] = ["phone_number", "api_id", "api_hash", "settings"]

    ID = 0xa677244f
    QUALNAME = "functions.functionsauth.SentCode"

    def __init__(self, *, phone_number: str, api_id: int, api_hash: str, settings: "ayiin.CodeSettings") -> None:
        
                self.phone_number = phone_number  # string
        
                self.api_id = api_id  # int
        
                self.api_hash = api_hash  # string
        
                self.settings = settings  # CodeSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendCode":
        # No flags
        
        phone_number = String.read(b)
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        settings = Object.read(b)
        
        return SendCode(phone_number=phone_number, api_id=api_id, api_hash=api_hash, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        b.write(self.settings.write())
        
        return b.getvalue()