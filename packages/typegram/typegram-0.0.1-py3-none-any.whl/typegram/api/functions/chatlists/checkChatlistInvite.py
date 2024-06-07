
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



class CheckChatlistInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``41C10FFF``

slug (``str``):
                    N/A
                
    Returns:
        :obj:`chatlists.ChatlistInvite<typegram.api.ayiin.chatlists.ChatlistInvite>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x41c10fff
    QUALNAME = "functions.functionschatlists.ChatlistInvite"

    def __init__(self, *, slug: str) -> None:
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckChatlistInvite":
        # No flags
        
        slug = String.read(b)
        
        return CheckChatlistInvite(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()