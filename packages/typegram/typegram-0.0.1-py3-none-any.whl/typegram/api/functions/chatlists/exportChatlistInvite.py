
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



class ExportChatlistInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8472478E``

chatlist (:obj:`InputChatlist<typegram.api.ayiin.InputChatlist>`):
                    N/A
                
        title (``str``):
                    N/A
                
        peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`chatlists.ExportedChatlistInvite<typegram.api.ayiin.chatlists.ExportedChatlistInvite>`
    """

    __slots__: List[str] = ["chatlist", "title", "peers"]

    ID = 0x8472478e
    QUALNAME = "functions.functionschatlists.ExportedChatlistInvite"

    def __init__(self, *, chatlist: "ayiin.InputChatlist", title: str, peers: List["ayiin.InputPeer"]) -> None:
        
                self.chatlist = chatlist  # InputChatlist
        
                self.title = title  # string
        
                self.peers = peers  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportChatlistInvite":
        # No flags
        
        chatlist = Object.read(b)
        
        title = String.read(b)
        
        peers = Object.read(b)
        
        return ExportChatlistInvite(chatlist=chatlist, title=title, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        b.write(String(self.title))
        
        b.write(Vector(self.peers))
        
        return b.getvalue()