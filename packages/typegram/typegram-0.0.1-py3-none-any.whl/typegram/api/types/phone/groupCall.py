
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



class GroupCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.GroupCall`.

    Details:
        - Layer: ``181``
        - ID: ``9E727AAD``

call (:obj:`GroupCall<typegram.api.ayiin.GroupCall>`):
                    N/A
                
        participants (List of :obj:`GroupCallParticipant<typegram.api.ayiin.GroupCallParticipant>`):
                    N/A
                
        participants_next_offset (``str``):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["call", "participants", "participants_next_offset", "chats", "users"]

    ID = 0x9e727aad
    QUALNAME = "functions.typesphone.GroupCall"

    def __init__(self, *, call: "ayiin.GroupCall", participants: List["ayiin.GroupCallParticipant"], participants_next_offset: str, chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.call = call  # GroupCall
        
                self.participants = participants  # GroupCallParticipant
        
                self.participants_next_offset = participants_next_offset  # string
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCall":
        # No flags
        
        call = Object.read(b)
        
        participants = Object.read(b)
        
        participants_next_offset = String.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return GroupCall(call=call, participants=participants, participants_next_offset=participants_next_offset, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.participants))
        
        b.write(String(self.participants_next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()