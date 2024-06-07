
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



class GetForumTopics(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DE560D1``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        offset_date (``int`` ``32-bit``):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        offset_topic (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        q (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.ForumTopics<typegram.api.ayiin.messages.ForumTopics>`
    """

    __slots__: List[str] = ["channel", "offset_date", "offset_id", "offset_topic", "limit", "q"]

    ID = 0xde560d1
    QUALNAME = "functions.functionsmessages.ForumTopics"

    def __init__(self, *, channel: "ayiin.InputChannel", offset_date: int, offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.offset_date = offset_date  # int
        
                self.offset_id = offset_id  # int
        
                self.offset_topic = offset_topic  # int
        
                self.limit = limit  # int
        
                self.q = q  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetForumTopics":
        
        flags = Int.read(b)
        
        channel = Object.read(b)
        
        q = String.read(b) if flags & (1 << 0) else None
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_topic = Int.read(b)
        
        limit = Int.read(b)
        
        return GetForumTopics(channel=channel, offset_date=offset_date, offset_id=offset_id, offset_topic=offset_topic, limit=limit, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.offset_topic))
        
        b.write(Int(self.limit))
        
        return b.getvalue()