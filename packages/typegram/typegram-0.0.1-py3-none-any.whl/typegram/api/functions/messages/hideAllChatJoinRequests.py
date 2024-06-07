
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



class HideAllChatJoinRequests(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E085F4EA``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        approved (``bool``, *optional*):
                    N/A
                
        link (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "approved", "link"]

    ID = 0xe085f4ea
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", approved: Optional[bool] = None, link: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.approved = approved  # true
        
                self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HideAllChatJoinRequests":
        
        flags = Int.read(b)
        
        approved = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        link = String.read(b) if flags & (1 << 1) else None
        return HideAllChatJoinRequests(peer=peer, approved=approved, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.link is not None:
            b.write(String(self.link))
        
        return b.getvalue()