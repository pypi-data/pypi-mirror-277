
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



class ChannelParticipantSelf(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``35A8BFA7``

user_id (``int`` ``64-bit``):
                    N/A
                
        inviter_id (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        via_request (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "inviter_id", "date", "via_request"]

    ID = 0x35a8bfa7
    QUALNAME = "types.channelParticipantSelf"

    def __init__(self, *, user_id: int, inviter_id: int, date: int, via_request: Optional[bool] = None) -> None:
        
                self.user_id = user_id  # long
        
                self.inviter_id = inviter_id  # long
        
                self.date = date  # int
        
                self.via_request = via_request  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantSelf":
        
        flags = Int.read(b)
        
        via_request = True if flags & (1 << 0) else False
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        return ChannelParticipantSelf(user_id=user_id, inviter_id=inviter_id, date=date, via_request=via_request)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        return b.getvalue()