
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



class BroadcastStats(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.BroadcastStats`.

    Details:
        - Layer: ``181``
        - ID: ``396CA5FC``

period (:obj:`StatsDateRangeDays<typegram.api.ayiin.StatsDateRangeDays>`):
                    N/A
                
        followers (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        views_per_post (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        shares_per_post (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        reactions_per_post (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        views_per_story (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        shares_per_story (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        reactions_per_story (:obj:`StatsAbsValueAndPrev<typegram.api.ayiin.StatsAbsValueAndPrev>`):
                    N/A
                
        enabled_notifications (:obj:`StatsPercentValue<typegram.api.ayiin.StatsPercentValue>`):
                    N/A
                
        growth_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        followers_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        mute_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        top_hours_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        interactions_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        iv_interactions_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        views_by_source_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        new_followers_by_source_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        languages_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        reactions_by_emotion_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        story_interactions_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        story_reactions_by_emotion_graph (:obj:`StatsGraph<typegram.api.ayiin.StatsGraph>`):
                    N/A
                
        recent_posts_interactions (List of :obj:`PostInteractionCounters<typegram.api.ayiin.PostInteractionCounters>`):
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

    __slots__: List[str] = ["period", "followers", "views_per_post", "shares_per_post", "reactions_per_post", "views_per_story", "shares_per_story", "reactions_per_story", "enabled_notifications", "growth_graph", "followers_graph", "mute_graph", "top_hours_graph", "interactions_graph", "iv_interactions_graph", "views_by_source_graph", "new_followers_by_source_graph", "languages_graph", "reactions_by_emotion_graph", "story_interactions_graph", "story_reactions_by_emotion_graph", "recent_posts_interactions"]

    ID = 0x396ca5fc
    QUALNAME = "functions.typesstats.BroadcastStats"

    def __init__(self, *, period: "ayiin.StatsDateRangeDays", followers: "ayiin.StatsAbsValueAndPrev", views_per_post: "ayiin.StatsAbsValueAndPrev", shares_per_post: "ayiin.StatsAbsValueAndPrev", reactions_per_post: "ayiin.StatsAbsValueAndPrev", views_per_story: "ayiin.StatsAbsValueAndPrev", shares_per_story: "ayiin.StatsAbsValueAndPrev", reactions_per_story: "ayiin.StatsAbsValueAndPrev", enabled_notifications: "ayiin.StatsPercentValue", growth_graph: "ayiin.StatsGraph", followers_graph: "ayiin.StatsGraph", mute_graph: "ayiin.StatsGraph", top_hours_graph: "ayiin.StatsGraph", interactions_graph: "ayiin.StatsGraph", iv_interactions_graph: "ayiin.StatsGraph", views_by_source_graph: "ayiin.StatsGraph", new_followers_by_source_graph: "ayiin.StatsGraph", languages_graph: "ayiin.StatsGraph", reactions_by_emotion_graph: "ayiin.StatsGraph", story_interactions_graph: "ayiin.StatsGraph", story_reactions_by_emotion_graph: "ayiin.StatsGraph", recent_posts_interactions: List["ayiin.PostInteractionCounters"]) -> None:
        
                self.period = period  # StatsDateRangeDays
        
                self.followers = followers  # StatsAbsValueAndPrev
        
                self.views_per_post = views_per_post  # StatsAbsValueAndPrev
        
                self.shares_per_post = shares_per_post  # StatsAbsValueAndPrev
        
                self.reactions_per_post = reactions_per_post  # StatsAbsValueAndPrev
        
                self.views_per_story = views_per_story  # StatsAbsValueAndPrev
        
                self.shares_per_story = shares_per_story  # StatsAbsValueAndPrev
        
                self.reactions_per_story = reactions_per_story  # StatsAbsValueAndPrev
        
                self.enabled_notifications = enabled_notifications  # StatsPercentValue
        
                self.growth_graph = growth_graph  # StatsGraph
        
                self.followers_graph = followers_graph  # StatsGraph
        
                self.mute_graph = mute_graph  # StatsGraph
        
                self.top_hours_graph = top_hours_graph  # StatsGraph
        
                self.interactions_graph = interactions_graph  # StatsGraph
        
                self.iv_interactions_graph = iv_interactions_graph  # StatsGraph
        
                self.views_by_source_graph = views_by_source_graph  # StatsGraph
        
                self.new_followers_by_source_graph = new_followers_by_source_graph  # StatsGraph
        
                self.languages_graph = languages_graph  # StatsGraph
        
                self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph
        
                self.story_interactions_graph = story_interactions_graph  # StatsGraph
        
                self.story_reactions_by_emotion_graph = story_reactions_by_emotion_graph  # StatsGraph
        
                self.recent_posts_interactions = recent_posts_interactions  # PostInteractionCounters

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastStats":
        # No flags
        
        period = Object.read(b)
        
        followers = Object.read(b)
        
        views_per_post = Object.read(b)
        
        shares_per_post = Object.read(b)
        
        reactions_per_post = Object.read(b)
        
        views_per_story = Object.read(b)
        
        shares_per_story = Object.read(b)
        
        reactions_per_story = Object.read(b)
        
        enabled_notifications = Object.read(b)
        
        growth_graph = Object.read(b)
        
        followers_graph = Object.read(b)
        
        mute_graph = Object.read(b)
        
        top_hours_graph = Object.read(b)
        
        interactions_graph = Object.read(b)
        
        iv_interactions_graph = Object.read(b)
        
        views_by_source_graph = Object.read(b)
        
        new_followers_by_source_graph = Object.read(b)
        
        languages_graph = Object.read(b)
        
        reactions_by_emotion_graph = Object.read(b)
        
        story_interactions_graph = Object.read(b)
        
        story_reactions_by_emotion_graph = Object.read(b)
        
        recent_posts_interactions = Object.read(b)
        
        return BroadcastStats(period=period, followers=followers, views_per_post=views_per_post, shares_per_post=shares_per_post, reactions_per_post=reactions_per_post, views_per_story=views_per_story, shares_per_story=shares_per_story, reactions_per_story=reactions_per_story, enabled_notifications=enabled_notifications, growth_graph=growth_graph, followers_graph=followers_graph, mute_graph=mute_graph, top_hours_graph=top_hours_graph, interactions_graph=interactions_graph, iv_interactions_graph=iv_interactions_graph, views_by_source_graph=views_by_source_graph, new_followers_by_source_graph=new_followers_by_source_graph, languages_graph=languages_graph, reactions_by_emotion_graph=reactions_by_emotion_graph, story_interactions_graph=story_interactions_graph, story_reactions_by_emotion_graph=story_reactions_by_emotion_graph, recent_posts_interactions=recent_posts_interactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.period.write())
        
        b.write(self.followers.write())
        
        b.write(self.views_per_post.write())
        
        b.write(self.shares_per_post.write())
        
        b.write(self.reactions_per_post.write())
        
        b.write(self.views_per_story.write())
        
        b.write(self.shares_per_story.write())
        
        b.write(self.reactions_per_story.write())
        
        b.write(self.enabled_notifications.write())
        
        b.write(self.growth_graph.write())
        
        b.write(self.followers_graph.write())
        
        b.write(self.mute_graph.write())
        
        b.write(self.top_hours_graph.write())
        
        b.write(self.interactions_graph.write())
        
        b.write(self.iv_interactions_graph.write())
        
        b.write(self.views_by_source_graph.write())
        
        b.write(self.new_followers_by_source_graph.write())
        
        b.write(self.languages_graph.write())
        
        b.write(self.reactions_by_emotion_graph.write())
        
        b.write(self.story_interactions_graph.write())
        
        b.write(self.story_reactions_by_emotion_graph.write())
        
        b.write(Vector(self.recent_posts_interactions))
        
        return b.getvalue()