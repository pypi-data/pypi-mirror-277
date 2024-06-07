
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



class ChatlistInvite(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.chatlists.ChatlistInvite`.

    Details:
        - Layer: ``181``
        - ID: ``1DCD839D``

title (``str``):
                    N/A
                
        peers (List of :obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        emoticon (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            chatlists.ExportedChatlistInvite
            chatlists.ExportedInvites
            chatlists.ChatlistInvite
            chatlists.ChatlistUpdates
    """

    __slots__: List[str] = ["title", "peers", "chats", "users", "emoticon"]

    ID = 0x1dcd839d
    QUALNAME = "functions.typeschatlists.ChatlistInvite"

    def __init__(self, *, title: str, peers: List["ayiin.Peer"], chats: List["ayiin.Chat"], users: List["ayiin.User"], emoticon: Optional[str] = None) -> None:
        
                self.title = title  # string
        
                self.peers = peers  # Peer
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistInvite":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        emoticon = String.read(b) if flags & (1 << 0) else None
        peers = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChatlistInvite(title=title, peers=peers, chats=chats, users=users, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        b.write(Vector(self.peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()