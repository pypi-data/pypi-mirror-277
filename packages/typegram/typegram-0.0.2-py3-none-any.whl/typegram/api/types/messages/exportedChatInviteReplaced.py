
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



class ExportedChatInviteReplaced(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.ExportedChatInvite`.

    Details:
        - Layer: ``181``
        - ID: ``222600EF``

invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`):
                    N/A
                
        new_invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 35 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getExportedChatInvite
            messages.editExportedChatInvite
    """

    __slots__: List[str] = ["invite", "new_invite", "users"]

    ID = 0x222600ef
    QUALNAME = "types.messages.exportedChatInviteReplaced"

    def __init__(self, *, invite: "api.ayiin.ExportedChatInvite", new_invite: "api.ayiin.ExportedChatInvite", users: List["api.ayiin.User"]) -> None:
        
                self.invite = invite  # ExportedChatInvite
        
                self.new_invite = new_invite  # ExportedChatInvite
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInviteReplaced":
        # No flags
        
        invite = Object.read(b)
        
        new_invite = Object.read(b)
        
        users = Object.read(b)
        
        return ExportedChatInviteReplaced(invite=invite, new_invite=new_invite, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.invite.write())
        
        b.write(self.new_invite.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()