
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



class ResolveBusinessChatLink(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5492E5EE``

slug (``str``):
                    N/A
                
    Returns:
        :obj:`account.ResolvedBusinessChatLinks<typegram.api.ayiin.account.ResolvedBusinessChatLinks>`
    """

    __slots__: List[str] = ["slug"]

    ID = 0x5492e5ee
    QUALNAME = "functions.functionsaccount.ResolvedBusinessChatLinks"

    def __init__(self, *, slug: str) -> None:
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolveBusinessChatLink":
        # No flags
        
        slug = String.read(b)
        
        return ResolveBusinessChatLink(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()