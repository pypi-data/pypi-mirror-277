
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



class ChannelParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.channels.ChannelParticipants`.

    Details:
        - Layer: ``181``
        - ID: ``9AB0FEAF``

count (``int`` ``32-bit``):
                    N/A
                
        participants (List of :obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 28 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    __slots__: List[str] = ["count", "participants", "chats", "users"]

    ID = 0x9ab0feaf
    QUALNAME = "functions.typeschannels.ChannelParticipants"

    def __init__(self, *, count: int, participants: List["ayiin.ChannelParticipant"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.count = count  # int
        
                self.participants = participants  # ChannelParticipant
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipants":
        # No flags
        
        count = Int.read(b)
        
        participants = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChannelParticipants(count=count, participants=participants, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.participants))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()