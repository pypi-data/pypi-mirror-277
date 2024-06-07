
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



class EditAdmin(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D33C8902``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`):
                    N/A
                
        rank (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "user_id", "admin_rights", "rank"]

    ID = 0xd33c8902
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", user_id: "ayiin.InputUser", admin_rights: "ayiin.ChatAdminRights", rank: str) -> None:
        
                self.channel = channel  # InputChannel
        
                self.user_id = user_id  # InputUser
        
                self.admin_rights = admin_rights  # ChatAdminRights
        
                self.rank = rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditAdmin":
        # No flags
        
        channel = Object.read(b)
        
        user_id = Object.read(b)
        
        admin_rights = Object.read(b)
        
        rank = String.read(b)
        
        return EditAdmin(channel=channel, user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.user_id.write())
        
        b.write(self.admin_rights.write())
        
        b.write(String(self.rank))
        
        return b.getvalue()