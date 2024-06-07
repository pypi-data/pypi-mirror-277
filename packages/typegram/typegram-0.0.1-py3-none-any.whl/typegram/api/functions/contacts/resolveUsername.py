
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



class ResolveUsername(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F93CCBA3``

username (``str``):
                    N/A
                
    Returns:
        :obj:`contacts.ResolvedPeer<typegram.api.ayiin.contacts.ResolvedPeer>`
    """

    __slots__: List[str] = ["username"]

    ID = 0xf93ccba3
    QUALNAME = "functions.functionscontacts.ResolvedPeer"

    def __init__(self, *, username: str) -> None:
        
                self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveUsername":
        # No flags
        
        username = String.read(b)
        
        return ResolveUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.username))
        
        return b.getvalue()