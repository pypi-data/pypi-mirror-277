
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



class GetChatInviteImporters(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DF04DD4E``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset_date (``int`` ``32-bit``):
                    N/A
                
        offset_user (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        requested (``bool``, *optional*):
                    N/A
                
        link (``str``, *optional*):
                    N/A
                
        q (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.ChatInviteImporters<typegram.api.ayiin.messages.ChatInviteImporters>`
    """

    __slots__: List[str] = ["peer", "offset_date", "offset_user", "limit", "requested", "link", "q"]

    ID = 0xdf04dd4e
    QUALNAME = "functions.functionsmessages.ChatInviteImporters"

    def __init__(self, *, peer: "ayiin.InputPeer", offset_date: int, offset_user: "ayiin.InputUser", limit: int, requested: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.offset_date = offset_date  # int
        
                self.offset_user = offset_user  # InputUser
        
                self.limit = limit  # int
        
                self.requested = requested  # true
        
                self.link = link  # string
        
                self.q = q  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatInviteImporters":
        
        flags = Int.read(b)
        
        requested = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        link = String.read(b) if flags & (1 << 1) else None
        q = String.read(b) if flags & (1 << 2) else None
        offset_date = Int.read(b)
        
        offset_user = Object.read(b)
        
        limit = Int.read(b)
        
        return GetChatInviteImporters(peer=peer, offset_date=offset_date, offset_user=offset_user, limit=limit, requested=requested, link=link, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.link is not None:
            b.write(String(self.link))
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(self.offset_user.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()