
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



class ChannelParticipant(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.channels.ChannelParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``DFB80317``

participant (:obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 27 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    __slots__: List[str] = ["participant", "chats", "users"]

    ID = 0xdfb80317
    QUALNAME = "functions.typeschannels.ChannelParticipant"

    def __init__(self, *, participant: "ayiin.ChannelParticipant", chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.participant = participant  # ChannelParticipant
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipant":
        # No flags
        
        participant = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChannelParticipant(participant=participant, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.participant.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()