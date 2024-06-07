
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



class RequestFirebaseSms(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8E39261E``

phone_number (``str``):
                    N/A
                
        phone_code_hash (``str``):
                    N/A
                
        safety_net_token (``str``, *optional*):
                    N/A
                
        play_integrity_token (``str``, *optional*):
                    N/A
                
        ios_push_secret (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "safety_net_token", "play_integrity_token", "ios_push_secret"]

    ID = 0x8e39261e
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, play_integrity_token: Optional[str] = None, ios_push_secret: Optional[str] = None) -> None:
        
                self.phone_number = phone_number  # string
        
                self.phone_code_hash = phone_code_hash  # string
        
                self.safety_net_token = safety_net_token  # string
        
                self.play_integrity_token = play_integrity_token  # string
        
                self.ios_push_secret = ios_push_secret  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestFirebaseSms":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        safety_net_token = String.read(b) if flags & (1 << 0) else None
        play_integrity_token = String.read(b) if flags & (1 << 2) else None
        ios_push_secret = String.read(b) if flags & (1 << 1) else None
        return RequestFirebaseSms(phone_number=phone_number, phone_code_hash=phone_code_hash, safety_net_token=safety_net_token, play_integrity_token=play_integrity_token, ios_push_secret=ios_push_secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        if self.safety_net_token is not None:
            b.write(String(self.safety_net_token))
        
        if self.play_integrity_token is not None:
            b.write(String(self.play_integrity_token))
        
        if self.ios_push_secret is not None:
            b.write(String(self.ios_push_secret))
        
        return b.getvalue()