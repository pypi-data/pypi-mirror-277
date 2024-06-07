
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



class AcceptAuthorization(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F3ED4C73``

bot_id (``int`` ``64-bit``):
                    N/A
                
        scope (``str``):
                    N/A
                
        public_key (``str``):
                    N/A
                
        value_hashes (List of :obj:`SecureValueHash<typegram.api.ayiin.SecureValueHash>`):
                    N/A
                
        credentials (:obj:`SecureCredentialsEncrypted<typegram.api.ayiin.SecureCredentialsEncrypted>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key", "value_hashes", "credentials"]

    ID = 0xf3ed4c73
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, bot_id: int, scope: str, public_key: str, value_hashes: List["ayiin.SecureValueHash"], credentials: "ayiin.SecureCredentialsEncrypted") -> None:
        
                self.bot_id = bot_id  # long
        
                self.scope = scope  # string
        
                self.public_key = public_key  # string
        
                self.value_hashes = value_hashes  # SecureValueHash
        
                self.credentials = credentials  # SecureCredentialsEncrypted

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptAuthorization":
        # No flags
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        value_hashes = Object.read(b)
        
        credentials = Object.read(b)
        
        return AcceptAuthorization(bot_id=bot_id, scope=scope, public_key=public_key, value_hashes=value_hashes, credentials=credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        b.write(Vector(self.value_hashes))
        
        b.write(self.credentials.write())
        
        return b.getvalue()