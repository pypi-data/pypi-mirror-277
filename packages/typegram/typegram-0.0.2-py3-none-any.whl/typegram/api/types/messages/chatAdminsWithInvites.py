
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



class ChatAdminsWithInvites(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.ChatAdminsWithInvites`.

    Details:
        - Layer: ``181``
        - ID: ``B69B72D7``

admins (List of :obj:`ChatAdminWithInvites<typegram.api.ayiin.ChatAdminWithInvites>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 30 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAdminsWithInvites
    """

    __slots__: List[str] = ["admins", "users"]

    ID = 0xb69b72d7
    QUALNAME = "types.messages.chatAdminsWithInvites"

    def __init__(self, *, admins: List["api.ayiin.ChatAdminWithInvites"], users: List["api.ayiin.User"]) -> None:
        
                self.admins = admins  # ChatAdminWithInvites
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminsWithInvites":
        # No flags
        
        admins = Object.read(b)
        
        users = Object.read(b)
        
        return ChatAdminsWithInvites(admins=admins, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.admins))
        
        b.write(Vector(self.users))
        
        return b.getvalue()