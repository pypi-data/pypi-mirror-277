
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



class EditExportedInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``653DB63D``

chatlist (:obj:`InputChatlist<typegram.api.ayiin.InputChatlist>`):
                    N/A
                
        slug (``str``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`ExportedChatlistInvite<typegram.api.ayiin.ExportedChatlistInvite>`
    """

    __slots__: List[str] = ["chatlist", "slug", "title", "peers"]

    ID = 0x653db63d
    QUALNAME = "functions.functions.ExportedChatlistInvite"

    def __init__(self, *, chatlist: "ayiin.InputChatlist", slug: str, title: Optional[str] = None, peers: Optional[List["ayiin.InputPeer"]] = None) -> None:
        
                self.chatlist = chatlist  # InputChatlist
        
                self.slug = slug  # string
        
                self.title = title  # string
        
                self.peers = peers  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditExportedInvite":
        
        flags = Int.read(b)
        
        chatlist = Object.read(b)
        
        slug = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        peers = Object.read(b) if flags & (1 << 2) else []
        
        return EditExportedInvite(chatlist=chatlist, slug=slug, title=title, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.chatlist.write())
        
        b.write(String(self.slug))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.peers is not None:
            b.write(Vector(self.peers))
        
        return b.getvalue()