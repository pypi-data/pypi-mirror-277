
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



class UpdateReadChannelDiscussionOutbox(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``695C9E7C``

channel_id (``int`` ``64-bit``):
                    N/A
                
        top_msg_id (``int`` ``32-bit``):
                    N/A
                
        read_max_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "top_msg_id", "read_max_id"]

    ID = 0x695c9e7c
    QUALNAME = "types.updateReadChannelDiscussionOutbox"

    def __init__(self, *, channel_id: int, top_msg_id: int, read_max_id: int) -> None:
        
                self.channel_id = channel_id  # long
        
                self.top_msg_id = top_msg_id  # int
        
                self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadChannelDiscussionOutbox":
        # No flags
        
        channel_id = Long.read(b)
        
        top_msg_id = Int.read(b)
        
        read_max_id = Int.read(b)
        
        return UpdateReadChannelDiscussionOutbox(channel_id=channel_id, top_msg_id=top_msg_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.top_msg_id))
        
        b.write(Int(self.read_max_id))
        
        return b.getvalue()