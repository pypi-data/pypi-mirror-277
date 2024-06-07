
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



class AdminLogResults(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.channels.AdminLogResults`.

    Details:
        - Layer: ``181``
        - ID: ``ED8AF74D``

events (List of :obj:`ChannelAdminLogEvent<typegram.api.ayiin.ChannelAdminLogEvent>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    __slots__: List[str] = ["events", "chats", "users"]

    ID = 0xed8af74d
    QUALNAME = "functions.typeschannels.AdminLogResults"

    def __init__(self, *, events: List["ayiin.ChannelAdminLogEvent"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.events = events  # ChannelAdminLogEvent
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AdminLogResults":
        # No flags
        
        events = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return AdminLogResults(events=events, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.events))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()