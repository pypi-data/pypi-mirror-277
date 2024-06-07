
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



class GetBroadcastRevenueTransactions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``69280F``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`stats.BroadcastRevenueTransactions<typegram.api.ayiin.stats.BroadcastRevenueTransactions>`
    """

    __slots__: List[str] = ["channel", "offset", "limit"]

    ID = 0x69280f
    QUALNAME = "functions.functionsstats.BroadcastRevenueTransactions"

    def __init__(self, *, channel: "ayiin.InputChannel", offset: int, limit: int) -> None:
        
                self.channel = channel  # InputChannel
        
                self.offset = offset  # int
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBroadcastRevenueTransactions":
        # No flags
        
        channel = Object.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetBroadcastRevenueTransactions(channel=channel, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()