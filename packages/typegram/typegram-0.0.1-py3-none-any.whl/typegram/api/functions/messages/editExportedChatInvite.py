
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



class EditExportedChatInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BDCA2F75``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        link (``str``):
                    N/A
                
        revoked (``bool``, *optional*):
                    N/A
                
        expire_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        usage_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        request_needed (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.ExportedChatInvite<typegram.api.ayiin.messages.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "link", "revoked", "expire_date", "usage_limit", "request_needed", "title"]

    ID = 0xbdca2f75
    QUALNAME = "functions.functionsmessages.ExportedChatInvite"

    def __init__(self, *, peer: "ayiin.InputPeer", link: str, revoked: Optional[bool] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, request_needed: Optional[bool] = None, title: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.link = link  # string
        
                self.revoked = revoked  # true
        
                self.expire_date = expire_date  # int
        
                self.usage_limit = usage_limit  # int
        
                self.request_needed = request_needed  # Bool
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditExportedChatInvite":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 2) else False
        peer = Object.read(b)
        
        link = String.read(b)
        
        expire_date = Int.read(b) if flags & (1 << 0) else None
        usage_limit = Int.read(b) if flags & (1 << 1) else None
        request_needed = Bool.read(b) if flags & (1 << 3) else None
        title = String.read(b) if flags & (1 << 4) else None
        return EditExportedChatInvite(peer=peer, link=link, revoked=revoked, expire_date=expire_date, usage_limit=usage_limit, request_needed=request_needed, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.request_needed is not None:
            b.write(Bool(self.request_needed))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()