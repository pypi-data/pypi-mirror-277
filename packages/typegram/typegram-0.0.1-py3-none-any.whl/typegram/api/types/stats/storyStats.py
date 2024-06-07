
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



class StoryStats(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.StoryStats`.

    Details:
        - Layer: ``181``
        - ID: ``50CD067C``

views_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        reactions_by_emotion_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["views_graph", "reactions_by_emotion_graph"]

    ID = 0x50cd067c
    QUALNAME = "functions.typesstats.StoryStats"

    def __init__(self, *, views_graph: "ayiin.StatsGraph", reactions_by_emotion_graph: "ayiin.StatsGraph") -> None:
        
                self.views_graph = views_graph  # StatsGraph
        
                self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryStats":
        # No flags
        
        views_graph = Object.read(b)
        
        reactions_by_emotion_graph = Object.read(b)
        
        return StoryStats(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.views_graph.write())
        
        b.write(self.reactions_by_emotion_graph.write())
        
        return b.getvalue()