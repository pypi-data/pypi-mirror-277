
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



class Bind_auth_key_inner(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``75A3F765``

nonce (``int`` ``64-bit``):
                    N/A
                
        temp_auth_key_id (``int`` ``64-bit``):
                    N/A
                
        perm_auth_key_id (``int`` ``64-bit``):
                    N/A
                
        temp_session_id (``int`` ``64-bit``):
                    N/A
                
        expires_at (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`BindAuthKeyInner<typegram.api.ayiin.BindAuthKeyInner>`
    """

    __slots__: List[str] = ["nonce", "temp_auth_key_id", "perm_auth_key_id", "temp_session_id", "expires_at"]

    ID = 0x75a3f765
    QUALNAME = "functions.functions.BindAuthKeyInner"

    def __init__(self, *, nonce: int, temp_auth_key_id: int, perm_auth_key_id: int, temp_session_id: int, expires_at: int) -> None:
        
                self.nonce = nonce  # long
        
                self.temp_auth_key_id = temp_auth_key_id  # long
        
                self.perm_auth_key_id = perm_auth_key_id  # long
        
                self.temp_session_id = temp_session_id  # long
        
                self.expires_at = expires_at  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Bind_auth_key_inner":
        # No flags
        
        nonce = Long.read(b)
        
        temp_auth_key_id = Long.read(b)
        
        perm_auth_key_id = Long.read(b)
        
        temp_session_id = Long.read(b)
        
        expires_at = Int.read(b)
        
        return Bind_auth_key_inner(nonce=nonce, temp_auth_key_id=temp_auth_key_id, perm_auth_key_id=perm_auth_key_id, temp_session_id=temp_session_id, expires_at=expires_at)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.nonce))
        
        b.write(Long(self.temp_auth_key_id))
        
        b.write(Long(self.perm_auth_key_id))
        
        b.write(Long(self.temp_session_id))
        
        b.write(Int(self.expires_at))
        
        return b.getvalue()