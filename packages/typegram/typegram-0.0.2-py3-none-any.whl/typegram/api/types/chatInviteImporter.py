
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



class ChatInviteImporter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatInviteImporter`.

    Details:
        - Layer: ``181``
        - ID: ``8C5ADFD9``

user_id (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        requested (``bool``, *optional*):
                    N/A
                
        via_chatlist (``bool``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
        approved_by (``int`` ``64-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "date", "requested", "via_chatlist", "about", "approved_by"]

    ID = 0x8c5adfd9
    QUALNAME = "types.chatInviteImporter"

    def __init__(self, *, user_id: int, date: int, requested: Optional[bool] = None, via_chatlist: Optional[bool] = None, about: Optional[str] = None, approved_by: Optional[int] = None) -> None:
        
                self.user_id = user_id  # long
        
                self.date = date  # int
        
                self.requested = requested  # true
        
                self.via_chatlist = via_chatlist  # true
        
                self.about = about  # string
        
                self.approved_by = approved_by  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteImporter":
        
        flags = Int.read(b)
        
        requested = True if flags & (1 << 0) else False
        via_chatlist = True if flags & (1 << 3) else False
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        about = String.read(b) if flags & (1 << 2) else None
        approved_by = Long.read(b) if flags & (1 << 1) else None
        return ChatInviteImporter(user_id=user_id, date=date, requested=requested, via_chatlist=via_chatlist, about=about, approved_by=approved_by)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        if self.about is not None:
            b.write(String(self.about))
        
        if self.approved_by is not None:
            b.write(Long(self.approved_by))
        
        return b.getvalue()