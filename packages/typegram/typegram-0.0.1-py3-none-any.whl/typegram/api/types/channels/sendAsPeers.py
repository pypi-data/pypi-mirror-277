
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



class SendAsPeers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.channels.SendAsPeers`.

    Details:
        - Layer: ``181``
        - ID: ``F496B0C6``

peers (List of :obj:`SendAsPeer<typegram.api.ayiin.SendAsPeer>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    __slots__: List[str] = ["peers", "chats", "users"]

    ID = 0xf496b0c6
    QUALNAME = "functions.typeschannels.SendAsPeers"

    def __init__(self, *, peers: List["ayiin.SendAsPeer"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.peers = peers  # SendAsPeer
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendAsPeers":
        # No flags
        
        peers = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return SendAsPeers(peers=peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()