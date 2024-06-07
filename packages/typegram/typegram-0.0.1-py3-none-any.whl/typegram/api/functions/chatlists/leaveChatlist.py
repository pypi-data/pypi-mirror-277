
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



class LeaveChatlist(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``74FAE13A``

chatlist (:obj:`InputChatlist<typegram.api.ayiin.InputChatlist>`):
                    N/A
                
        peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["chatlist", "peers"]

    ID = 0x74fae13a
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, chatlist: "ayiin.InputChatlist", peers: List["ayiin.InputPeer"]) -> None:
        
                self.chatlist = chatlist  # InputChatlist
        
                self.peers = peers  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveChatlist":
        # No flags
        
        chatlist = Object.read(b)
        
        peers = Object.read(b)
        
        return LeaveChatlist(chatlist=chatlist, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        b.write(Vector(self.peers))
        
        return b.getvalue()