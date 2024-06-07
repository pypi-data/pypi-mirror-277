
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



class GetAuthorizationForm(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A929597A``

bot_id (``int`` ``64-bit``):
                    N/A
                
        scope (``str``):
                    N/A
                
        public_key (``str``):
                    N/A
                
    Returns:
        :obj:`account.AuthorizationForm<typegram.api.ayiin.account.AuthorizationForm>`
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key"]

    ID = 0xa929597a
    QUALNAME = "functions.functionsaccount.AuthorizationForm"

    def __init__(self, *, bot_id: int, scope: str, public_key: str) -> None:
        
                self.bot_id = bot_id  # long
        
                self.scope = scope  # string
        
                self.public_key = public_key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAuthorizationForm":
        # No flags
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        return GetAuthorizationForm(bot_id=bot_id, scope=scope, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        return b.getvalue()