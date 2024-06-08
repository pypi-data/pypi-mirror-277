
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



class ExportedChatInvites(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.ExportedChatInvites`.

    Details:
        - Layer: ``181``
        - ID: ``BDC62DCC``

count (``int`` ``32-bit``):
                    N/A
                
        invites (List of :obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 28 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getExportedChatInvites
    """

    __slots__: List[str] = ["count", "invites", "users"]

    ID = 0xbdc62dcc
    QUALNAME = "types.messages.exportedChatInvites"

    def __init__(self, *, count: int, invites: List["api.ayiin.ExportedChatInvite"], users: List["api.ayiin.User"]) -> None:
        
                self.count = count  # int
        
                self.invites = invites  # ExportedChatInvite
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInvites":
        # No flags
        
        count = Int.read(b)
        
        invites = Object.read(b)
        
        users = Object.read(b)
        
        return ExportedChatInvites(count=count, invites=invites, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.invites))
        
        b.write(Vector(self.users))
        
        return b.getvalue()