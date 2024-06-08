
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class InvitedUsers(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.InvitedUsers`.

    Details:
        - Layer: ``181``
        - ID: ``7F5DEFA6``

updates (:obj:`Updates<typegram.api.ayiin.Updates>`):
                    N/A
                
        missing_invitees (List of :obj:`MissingInvitee<typegram.api.ayiin.MissingInvitee>`):
                    N/A
                
    Functions:
        This object can be returned by 21 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.addChatUser
            messages.createChat
            channels.inviteToChannel
    """

    __slots__: List[str] = ["updates", "missing_invitees"]

    ID = 0x7f5defa6
    QUALNAME = "types.messages.invitedUsers"

    def __init__(self, *, updates: "api.ayiin.Updates", missing_invitees: List["api.ayiin.MissingInvitee"]) -> None:
        
                self.updates = updates  # Updates
        
                self.missing_invitees = missing_invitees  # MissingInvitee

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvitedUsers":
        # No flags
        
        updates = Object.read(b)
        
        missing_invitees = Object.read(b)
        
        return InvitedUsers(updates=updates, missing_invitees=missing_invitees)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.updates.write())
        
        b.write(Vector(self.missing_invitees))
        
        return b.getvalue()