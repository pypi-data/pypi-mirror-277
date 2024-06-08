
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



class UpdateChannelWebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``2F2BA99F``

channel_id (``int`` ``64-bit``):
                    N/A
                
        webpage (:obj:`WebPage<typegram.api.ayiin.WebPage>`):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "webpage", "pts", "pts_count"]

    ID = 0x2f2ba99f
    QUALNAME = "types.updateChannelWebPage"

    def __init__(self, *, channel_id: int, webpage: "api.ayiin.WebPage", pts: int, pts_count: int) -> None:
        
                self.channel_id = channel_id  # long
        
                self.webpage = webpage  # WebPage
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelWebPage":
        # No flags
        
        channel_id = Long.read(b)
        
        webpage = Object.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdateChannelWebPage(channel_id=channel_id, webpage=webpage, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(self.webpage.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()