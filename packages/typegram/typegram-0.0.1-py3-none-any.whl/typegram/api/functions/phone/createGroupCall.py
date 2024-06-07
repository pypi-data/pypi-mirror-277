
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



class CreateGroupCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``48CDC6D8``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        random_id (``int`` ``32-bit``):
                    N/A
                
        rtmp_stream (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        schedule_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "rtmp_stream", "title", "schedule_date"]

    ID = 0x48cdc6d8
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", random_id: int, rtmp_stream: Optional[bool] = None, title: Optional[str] = None, schedule_date: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.random_id = random_id  # int
        
                self.rtmp_stream = rtmp_stream  # true
        
                self.title = title  # string
        
                self.schedule_date = schedule_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateGroupCall":
        
        flags = Int.read(b)
        
        rtmp_stream = True if flags & (1 << 2) else False
        peer = Object.read(b)
        
        random_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        schedule_date = Int.read(b) if flags & (1 << 1) else None
        return CreateGroupCall(peer=peer, random_id=random_id, rtmp_stream=rtmp_stream, title=title, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.random_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        return b.getvalue()