
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



class MegagroupStats(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.MegagroupStats`.

    Details:
        - Layer: ``181``
        - ID: ``EF7FF916``

period (:obj:`StatsDateRangeDays<typegram.api.ayiin.StatsDateRangeDays>`):
                    N/A
                
        members (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        messages (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        viewers (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        posters (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        growth_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        members_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        new_members_by_source_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        languages_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        messages_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        actions_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        top_hours_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        weekdays_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        top_posters (List of :obj:`StatsGroupTopPoster<typegram.api.ayiin.StatsGroupTopPoster>`):
                    N/A
                
        top_admins (List of :obj:`StatsGroupTopAdmin<typegram.api.ayiin.StatsGroupTopAdmin>`):
                    N/A
                
        top_inviters (List of :obj:`StatsGroupTopInviter<typegram.api.ayiin.StatsGroupTopInviter>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

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

    __slots__: List[str] = ["period", "members", "messages", "viewers", "posters", "growth_graph", "members_graph", "new_members_by_source_graph", "languages_graph", "messages_graph", "actions_graph", "top_hours_graph", "weekdays_graph", "top_posters", "top_admins", "top_inviters", "users"]

    ID = 0xef7ff916
    QUALNAME = "functions.typesstats.MegagroupStats"

    def __init__(self, *, period: "ayiin.StatsDateRangeDays", members: "ayiin.StatsAbsValueAndPrev", messages: "ayiin.StatsAbsValueAndPrev", viewers: "ayiin.StatsAbsValueAndPrev", posters: "ayiin.StatsAbsValueAndPrev", growth_graph: "ayiin.StatsGraph", members_graph: "ayiin.StatsGraph", new_members_by_source_graph: "ayiin.StatsGraph", languages_graph: "ayiin.StatsGraph", messages_graph: "ayiin.StatsGraph", actions_graph: "ayiin.StatsGraph", top_hours_graph: "ayiin.StatsGraph", weekdays_graph: "ayiin.StatsGraph", top_posters: List["ayiin.StatsGroupTopPoster"], top_admins: List["ayiin.StatsGroupTopAdmin"], top_inviters: List["ayiin.StatsGroupTopInviter"], users: List["ayiin.User"]) -> None:
        
                self.period = period  # StatsDateRangeDays
        
                self.members = members  # StatsAbsValueAndPrev
        
                self.messages = messages  # StatsAbsValueAndPrev
        
                self.viewers = viewers  # StatsAbsValueAndPrev
        
                self.posters = posters  # StatsAbsValueAndPrev
        
                self.growth_graph = growth_graph  # StatsGraph
        
                self.members_graph = members_graph  # StatsGraph
        
                self.new_members_by_source_graph = new_members_by_source_graph  # StatsGraph
        
                self.languages_graph = languages_graph  # StatsGraph
        
                self.messages_graph = messages_graph  # StatsGraph
        
                self.actions_graph = actions_graph  # StatsGraph
        
                self.top_hours_graph = top_hours_graph  # StatsGraph
        
                self.weekdays_graph = weekdays_graph  # StatsGraph
        
                self.top_posters = top_posters  # StatsGroupTopPoster
        
                self.top_admins = top_admins  # StatsGroupTopAdmin
        
                self.top_inviters = top_inviters  # StatsGroupTopInviter
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MegagroupStats":
        # No flags
        
        period = Object.read(b)
        
        members = Object.read(b)
        
        messages = Object.read(b)
        
        viewers = Object.read(b)
        
        posters = Object.read(b)
        
        growth_graph = Object.read(b)
        
        members_graph = Object.read(b)
        
        new_members_by_source_graph = Object.read(b)
        
        languages_graph = Object.read(b)
        
        messages_graph = Object.read(b)
        
        actions_graph = Object.read(b)
        
        top_hours_graph = Object.read(b)
        
        weekdays_graph = Object.read(b)
        
        top_posters = Object.read(b)
        
        top_admins = Object.read(b)
        
        top_inviters = Object.read(b)
        
        users = Object.read(b)
        
        return MegagroupStats(period=period, members=members, messages=messages, viewers=viewers, posters=posters, growth_graph=growth_graph, members_graph=members_graph, new_members_by_source_graph=new_members_by_source_graph, languages_graph=languages_graph, messages_graph=messages_graph, actions_graph=actions_graph, top_hours_graph=top_hours_graph, weekdays_graph=weekdays_graph, top_posters=top_posters, top_admins=top_admins, top_inviters=top_inviters, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.period.write())
        
        b.write(self.members.write())
        
        b.write(self.messages.write())
        
        b.write(self.viewers.write())
        
        b.write(self.posters.write())
        
        b.write(self.growth_graph.write())
        
        b.write(self.members_graph.write())
        
        b.write(self.new_members_by_source_graph.write())
        
        b.write(self.languages_graph.write())
        
        b.write(self.messages_graph.write())
        
        b.write(self.actions_graph.write())
        
        b.write(self.top_hours_graph.write())
        
        b.write(self.weekdays_graph.write())
        
        b.write(Vector(self.top_posters))
        
        b.write(Vector(self.top_admins))
        
        b.write(Vector(self.top_inviters))
        
        b.write(Vector(self.users))
        
        return b.getvalue()