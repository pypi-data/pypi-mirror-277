
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



class BroadcastRevenueStats(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.BroadcastRevenueStats`.

    Details:
        - Layer: ``181``
        - ID: ``5407E297``

top_hours_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        revenue_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        balances (:obj:`BroadcastRevenueBalances<typegram.api.ayiin.BroadcastRevenueBalances>`):
                    N/A
                
        usd_rate (``float`` ``64-bit``):
                    N/A
                
    Functions:
        This object can be returned by 27 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stats.BroadcastStats
            stats.MegagroupStats
            stats.PublicForwards
            stats.MessageStats
            stats.StoryStats
            stats.BroadcastRevenueStats
            stats.BroadcastRevenueWithdrawalUrl
            stats.BroadcastRevenueTransactions
    """

    __slots__: List[str] = ["top_hours_graph", "revenue_graph", "balances", "usd_rate"]

    ID = 0x5407e297
    QUALNAME = "functions.typesstats.BroadcastRevenueStats"

    def __init__(self, *, top_hours_graph: "ayiin.StatsGraph", revenue_graph: "ayiin.StatsGraph", balances: "ayiin.BroadcastRevenueBalances", usd_rate: float) -> None:
        
                self.top_hours_graph = top_hours_graph  # StatsGraph
        
                self.revenue_graph = revenue_graph  # StatsGraph
        
                self.balances = balances  # BroadcastRevenueBalances
        
                self.usd_rate = usd_rate  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueStats":
        # No flags
        
        top_hours_graph = Object.read(b)
        
        revenue_graph = Object.read(b)
        
        balances = Object.read(b)
        
        usd_rate = Double.read(b)
        
        return BroadcastRevenueStats(top_hours_graph=top_hours_graph, revenue_graph=revenue_graph, balances=balances, usd_rate=usd_rate)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.top_hours_graph.write())
        
        b.write(self.revenue_graph.write())
        
        b.write(self.balances.write())
        
        b.write(Double(self.usd_rate))
        
        return b.getvalue()