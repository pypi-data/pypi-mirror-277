
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



class ChatAdminWithInvites(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatAdminWithInvites`.

    Details:
        - Layer: ``181``
        - ID: ``F2ECEF23``

admin_id (``int`` ``64-bit``):
                    N/A
                
        invites_count (``int`` ``32-bit``):
                    N/A
                
        revoked_invites_count (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["admin_id", "invites_count", "revoked_invites_count"]

    ID = 0xf2ecef23
    QUALNAME = "types.chatAdminWithInvites"

    def __init__(self, *, admin_id: int, invites_count: int, revoked_invites_count: int) -> None:
        
                self.admin_id = admin_id  # long
        
                self.invites_count = invites_count  # int
        
                self.revoked_invites_count = revoked_invites_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminWithInvites":
        # No flags
        
        admin_id = Long.read(b)
        
        invites_count = Int.read(b)
        
        revoked_invites_count = Int.read(b)
        
        return ChatAdminWithInvites(admin_id=admin_id, invites_count=invites_count, revoked_invites_count=revoked_invites_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.admin_id))
        
        b.write(Int(self.invites_count))
        
        b.write(Int(self.revoked_invites_count))
        
        return b.getvalue()