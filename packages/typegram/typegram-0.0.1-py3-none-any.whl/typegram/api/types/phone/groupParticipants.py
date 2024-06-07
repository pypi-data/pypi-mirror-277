
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



class GroupParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.GroupParticipants`.

    Details:
        - Layer: ``181``
        - ID: ``F47751B6``

count (``int`` ``32-bit``):
                    N/A
                
        participants (List of :obj:`GroupCallParticipant<typegram.api.ayiin.GroupCallParticipant>`):
                    N/A
                
        next_offset (``str``):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 23 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            phone.PhoneCall
            phone.GroupCall
            phone.GroupParticipants
            phone.JoinAsPeers
            phone.ExportedGroupCallInvite
            phone.GroupCallStreamChannels
            phone.GroupCallStreamRtmpUrl
    """

    __slots__: List[str] = ["count", "participants", "next_offset", "chats", "users", "version"]

    ID = 0xf47751b6
    QUALNAME = "functions.typesphone.GroupParticipants"

    def __init__(self, *, count: int, participants: List["ayiin.GroupCallParticipant"], next_offset: str, chats: List["ayiin.Chat"], users: List["ayiin.User"], version: int) -> None:
        
                self.count = count  # int
        
                self.participants = participants  # GroupCallParticipant
        
                self.next_offset = next_offset  # string
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupParticipants":
        # No flags
        
        count = Int.read(b)
        
        participants = Object.read(b)
        
        next_offset = String.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        version = Int.read(b)
        
        return GroupParticipants(count=count, participants=participants, next_offset=next_offset, chats=chats, users=users, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.participants))
        
        b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(Int(self.version))
        
        return b.getvalue()