
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



class UpdatePinnedForumTopic(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6C2D9026``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        topic_id (``int`` ``32-bit``):
                    N/A
                
        pinned (``bool``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "topic_id", "pinned"]

    ID = 0x6c2d9026
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", topic_id: int, pinned: bool) -> None:
        
                self.channel = channel  # InputChannel
        
                self.topic_id = topic_id  # int
        
                self.pinned = pinned  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopic":
        # No flags
        
        channel = Object.read(b)
        
        topic_id = Int.read(b)
        
        pinned = Bool.read(b)
        
        return UpdatePinnedForumTopic(channel=channel, topic_id=topic_id, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.topic_id))
        
        b.write(Bool(self.pinned))
        
        return b.getvalue()