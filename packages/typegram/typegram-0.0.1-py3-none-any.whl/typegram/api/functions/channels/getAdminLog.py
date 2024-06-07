
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



class GetAdminLog(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``33DDF480``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        q (``str``):
                    N/A
                
        max_id (``int`` ``64-bit``):
                    N/A
                
        min_id (``int`` ``64-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        events_filter (:obj:`ChannelAdminLogEventsFilter<typegram.api.ayiin.ChannelAdminLogEventsFilter>`, *optional*):
                    N/A
                
        admins (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
    Returns:
        :obj:`channels.AdminLogResults<typegram.api.ayiin.channels.AdminLogResults>`
    """

    __slots__: List[str] = ["channel", "q", "max_id", "min_id", "limit", "events_filter", "admins"]

    ID = 0x33ddf480
    QUALNAME = "functions.functionschannels.AdminLogResults"

    def __init__(self, *, channel: "ayiin.InputChannel", q: str, max_id: int, min_id: int, limit: int, events_filter: "ayiin.ChannelAdminLogEventsFilter" = None, admins: Optional[List["ayiin.InputUser"]] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.q = q  # string
        
                self.max_id = max_id  # long
        
                self.min_id = min_id  # long
        
                self.limit = limit  # int
        
                self.events_filter = events_filter  # ChannelAdminLogEventsFilter
        
                self.admins = admins  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminLog":
        
        flags = Int.read(b)
        
        channel = Object.read(b)
        
        q = String.read(b)
        
        events_filter = Object.read(b) if flags & (1 << 0) else None
        
        admins = Object.read(b) if flags & (1 << 1) else []
        
        max_id = Long.read(b)
        
        min_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetAdminLog(channel=channel, q=q, max_id=max_id, min_id=min_id, limit=limit, events_filter=events_filter, admins=admins)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(String(self.q))
        
        if self.events_filter is not None:
            b.write(self.events_filter.write())
        
        if self.admins is not None:
            b.write(Vector(self.admins))
        
        b.write(Long(self.max_id))
        
        b.write(Long(self.min_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()