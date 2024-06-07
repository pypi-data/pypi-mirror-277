
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



class GetBroadcastRevenueStats(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``75DFB671``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`stats.BroadcastRevenueStats<typegram.api.ayiin.stats.BroadcastRevenueStats>`
    """

    __slots__: List[str] = ["channel", "dark"]

    ID = 0x75dfb671
    QUALNAME = "functions.functionsstats.BroadcastRevenueStats"

    def __init__(self, *, channel: "ayiin.InputChannel", dark: Optional[bool] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.dark = dark  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBroadcastRevenueStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = Object.read(b)
        
        return GetBroadcastRevenueStats(channel=channel, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        return b.getvalue()