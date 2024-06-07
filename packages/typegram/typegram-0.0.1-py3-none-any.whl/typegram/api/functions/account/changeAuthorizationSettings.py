
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



class ChangeAuthorizationSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``40F48462``

hash (``int`` ``64-bit``):
                    N/A
                
        confirmed (``bool``, *optional*):
                    N/A
                
        encrypted_requests_disabled (``bool``, *optional*):
                    N/A
                
        call_requests_disabled (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hash", "confirmed", "encrypted_requests_disabled", "call_requests_disabled"]

    ID = 0x40f48462
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, hash: int, confirmed: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None) -> None:
        
                self.hash = hash  # long
        
                self.confirmed = confirmed  # true
        
                self.encrypted_requests_disabled = encrypted_requests_disabled  # Bool
        
                self.call_requests_disabled = call_requests_disabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeAuthorizationSettings":
        
        flags = Int.read(b)
        
        confirmed = True if flags & (1 << 3) else False
        hash = Long.read(b)
        
        encrypted_requests_disabled = Bool.read(b) if flags & (1 << 0) else None
        call_requests_disabled = Bool.read(b) if flags & (1 << 1) else None
        return ChangeAuthorizationSettings(hash=hash, confirmed=confirmed, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        if self.encrypted_requests_disabled is not None:
            b.write(Bool(self.encrypted_requests_disabled))
        
        if self.call_requests_disabled is not None:
            b.write(Bool(self.call_requests_disabled))
        
        return b.getvalue()