
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



class GetChannelDifference(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3173D78``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        filter (:obj:`ChannelMessagesFilter<typegram.api.ayiin.ChannelMessagesFilter>`):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        force (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`updates.ChannelDifference<typegram.api.ayiin.updates.ChannelDifference>`
    """

    __slots__: List[str] = ["channel", "filter", "pts", "limit", "force"]

    ID = 0x3173d78
    QUALNAME = "functions.functionsupdates.ChannelDifference"

    def __init__(self, *, channel: "ayiin.InputChannel", filter: "ayiin.ChannelMessagesFilter", pts: int, limit: int, force: Optional[bool] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.filter = filter  # ChannelMessagesFilter
        
                self.pts = pts  # int
        
                self.limit = limit  # int
        
                self.force = force  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelDifference":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        channel = Object.read(b)
        
        filter = Object.read(b)
        
        pts = Int.read(b)
        
        limit = Int.read(b)
        
        return GetChannelDifference(channel=channel, filter=filter, pts=pts, limit=limit, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.limit))
        
        return b.getvalue()