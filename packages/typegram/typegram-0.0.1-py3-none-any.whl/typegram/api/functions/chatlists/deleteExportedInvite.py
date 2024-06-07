
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



class DeleteExportedInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``719C5C5E``

chatlist (:obj:`InputChatlist<typegram.api.ayiin.InputChatlist>`):
                    N/A
                
        slug (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chatlist", "slug"]

    ID = 0x719c5c5e
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, chatlist: "ayiin.InputChatlist", slug: str) -> None:
        
                self.chatlist = chatlist  # InputChatlist
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteExportedInvite":
        # No flags
        
        chatlist = Object.read(b)
        
        slug = String.read(b)
        
        return DeleteExportedInvite(chatlist=chatlist, slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        b.write(String(self.slug))
        
        return b.getvalue()