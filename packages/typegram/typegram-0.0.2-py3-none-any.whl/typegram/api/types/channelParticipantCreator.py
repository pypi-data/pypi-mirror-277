
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



class ChannelParticipantCreator(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``2FE601D3``

user_id (``int`` ``64-bit``):
                    N/A
                
        admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`):
                    N/A
                
        rank (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "admin_rights", "rank"]

    ID = 0x2fe601d3
    QUALNAME = "types.channelParticipantCreator"

    def __init__(self, *, user_id: int, admin_rights: "api.ayiin.ChatAdminRights", rank: Optional[str] = None) -> None:
        
                self.user_id = user_id  # long
        
                self.admin_rights = admin_rights  # ChatAdminRights
        
                self.rank = rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantCreator":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        admin_rights = Object.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChannelParticipantCreator(user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(self.admin_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()