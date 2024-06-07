
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



class ImportBotAuthorization(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``67A3FF2C``

flags (``int`` ``32-bit``):
                    N/A
                
        api_id (``int`` ``32-bit``):
                    N/A
                
        api_hash (``str``):
                    N/A
                
        bot_auth_token (``str``):
                    N/A
                
    Returns:
        :obj:`auth.Authorization<typegram.api.ayiin.auth.Authorization>`
    """

    __slots__: List[str] = ["flags", "api_id", "api_hash", "bot_auth_token"]

    ID = 0x67a3ff2c
    QUALNAME = "functions.functionsauth.Authorization"

    def __init__(self, *, flags: int, api_id: int, api_hash: str, bot_auth_token: str) -> None:
        
                self.flags = flags  # int
        
                self.api_id = api_id  # int
        
                self.api_hash = api_hash  # string
        
                self.bot_auth_token = bot_auth_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportBotAuthorization":
        # No flags
        
        flags = Int.read(b)
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        bot_auth_token = String.read(b)
        
        return ImportBotAuthorization(flags=flags, api_id=api_id, api_hash=api_hash, bot_auth_token=bot_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.flags))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        b.write(String(self.bot_auth_token))
        
        return b.getvalue()