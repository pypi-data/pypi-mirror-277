
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



class ChannelFull(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatFull`.

    Details:
        - Layer: ``181``
        - ID: ``BBAB348D``

id (``int`` ``64-bit``):
                    N/A
                
        about (``str``):
                    N/A
                
        read_inbox_max_id (``int`` ``32-bit``):
                    N/A
                
        read_outbox_max_id (``int`` ``32-bit``):
                    N/A
                
        unread_count (``int`` ``32-bit``):
                    N/A
                
        chat_photo (:obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        notify_settings (:obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`):
                    N/A
                
        bot_info (List of :obj:`BotInfo<typegram.api.ayiin.BotInfo>`):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        can_view_participants (``bool``, *optional*):
                    N/A
                
        can_set_username (``bool``, *optional*):
                    N/A
                
        can_set_stickers (``bool``, *optional*):
                    N/A
                
        hidden_prehistory (``bool``, *optional*):
                    N/A
                
        can_set_location (``bool``, *optional*):
                    N/A
                
        has_scheduled (``bool``, *optional*):
                    N/A
                
        can_view_stats (``bool``, *optional*):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        can_delete_channel (``bool``, *optional*):
                    N/A
                
        antispam (``bool``, *optional*):
                    N/A
                
        participants_hidden (``bool``, *optional*):
                    N/A
                
        translations_disabled (``bool``, *optional*):
                    N/A
                
        stories_pinned_available (``bool``, *optional*):
                    N/A
                
        view_forum_as_messages (``bool``, *optional*):
                    N/A
                
        restricted_sponsored (``bool``, *optional*):
                    N/A
                
        can_view_revenue (``bool``, *optional*):
                    N/A
                
        participants_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        admins_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        kicked_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        banned_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        online_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        exported_invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`, *optional*):
                    N/A
                
        migrated_from_chat_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        migrated_from_max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        pinned_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        stickerset (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`, *optional*):
                    N/A
                
        available_min_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        linked_chat_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        location (:obj:`ChannelLocation<typegram.api.ayiin.ChannelLocation>`, *optional*):
                    N/A
                
        slowmode_seconds (``int`` ``32-bit``, *optional*):
                    N/A
                
        slowmode_next_send_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        stats_dc (``int`` ``32-bit``, *optional*):
                    N/A
                
        call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        pending_suggestions (List of ``str``, *optional*):
                    N/A
                
        groupcall_default_join_as (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        theme_emoticon (``str``, *optional*):
                    N/A
                
        requests_pending (``int`` ``32-bit``, *optional*):
                    N/A
                
        recent_requesters (List of ``int`` ``64-bit``, *optional*):
                    N/A
                
        default_send_as (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        available_reactions (:obj:`ChatReactions<typegram.api.ayiin.ChatReactions>`, *optional*):
                    N/A
                
        reactions_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        stories (:obj:`PeerStories<typegram.api.ayiin.PeerStories>`, *optional*):
                    N/A
                
        wallpaper (:obj:`WallPaper<typegram.api.ayiin.WallPaper>`, *optional*):
                    N/A
                
        boosts_applied (``int`` ``32-bit``, *optional*):
                    N/A
                
        boosts_unrestrict (``int`` ``32-bit``, *optional*):
                    N/A
                
        emojiset (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            .X
            .RpcDropAnswer
            .Bool
            .Authorization
            .PeerNotifySettings
            .User
            .Vector<SecureValue>
            .SecureValue
            .Updates
            .WallPaper
            .Document
            .Theme
            .Vector<WallPaper>
            .GlobalPrivacySettings
            .EmojiList
            .BusinessChatLink
            .ReactionsNotifySettings
            .Vector<User>
            .Vector<Bool>
            .Vector<int>
            .Vector<ReceivedNotifyMessage>
            .EncryptedChat
            .Vector<long>
            .MessageMedia
            .ExportedChatInvite
            .ChatInvite
            .Vector<StickerSetCovered>
            .EncryptedFile
            .ChatOnlines
            .EmojiKeywordsDifference
            .Vector<EmojiLanguage>
            .EmojiURL
            .UrlAuthResult
            .Vector<ReadParticipantDate>
            .AttachMenuBots
            .AttachMenuBotsBot
            .WebViewResult
            .SimpleWebViewResult
            .WebViewMessageSent
            .Vector<Document>
            .AppWebViewResult
            .OutboxReadDate
            .Vector<FactCheck>
            .Vector<FileHash>
            .ExportedMessageLink
            .DataJSON
            .Vector<BotCommand>
            .BotMenuButton
            .Vector<PremiumGiftCodeOption>
            .LangPackDifference
            .Vector<LangPackString>
            .Vector<LangPackLanguage>
            .LangPackLanguage
            .StatsGraph
            .ExportedChatlistInvite
            .Vector<Peer>
            .ExportedStoryLink
            .SmsJob
            .ResPQ
            .P_Q_inner_data
            .BindAuthKeyInner
            .Server_DH_Params
            .Server_DH_inner_data
            .Client_DH_Inner_Data
            .Set_client_DH_params_answer
    """

    __slots__: List[str] = ["id", "about", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "chat_photo", "notify_settings", "bot_info", "pts", "can_view_participants", "can_set_username", "can_set_stickers", "hidden_prehistory", "can_set_location", "has_scheduled", "can_view_stats", "blocked", "can_delete_channel", "antispam", "participants_hidden", "translations_disabled", "stories_pinned_available", "view_forum_as_messages", "restricted_sponsored", "can_view_revenue", "participants_count", "admins_count", "kicked_count", "banned_count", "online_count", "exported_invite", "migrated_from_chat_id", "migrated_from_max_id", "pinned_msg_id", "stickerset", "available_min_id", "folder_id", "linked_chat_id", "location", "slowmode_seconds", "slowmode_next_send_date", "stats_dc", "call", "ttl_period", "pending_suggestions", "groupcall_default_join_as", "theme_emoticon", "requests_pending", "recent_requesters", "default_send_as", "available_reactions", "reactions_limit", "stories", "wallpaper", "boosts_applied", "boosts_unrestrict", "emojiset"]

    ID = 0xbbab348d
    QUALNAME = "functions.types.ChatFull"

    def __init__(self, *, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, chat_photo: "ayiin.Photo", notify_settings: "ayiin.PeerNotifySettings", bot_info: List["ayiin.BotInfo"], pts: int, can_view_participants: Optional[bool] = None, can_set_username: Optional[bool] = None, can_set_stickers: Optional[bool] = None, hidden_prehistory: Optional[bool] = None, can_set_location: Optional[bool] = None, has_scheduled: Optional[bool] = None, can_view_stats: Optional[bool] = None, blocked: Optional[bool] = None, can_delete_channel: Optional[bool] = None, antispam: Optional[bool] = None, participants_hidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, restricted_sponsored: Optional[bool] = None, can_view_revenue: Optional[bool] = None, participants_count: Optional[int] = None, admins_count: Optional[int] = None, kicked_count: Optional[int] = None, banned_count: Optional[int] = None, online_count: Optional[int] = None, exported_invite: "ayiin.ExportedChatInvite" = None, migrated_from_chat_id: Optional[int] = None, migrated_from_max_id: Optional[int] = None, pinned_msg_id: Optional[int] = None, stickerset: "ayiin.StickerSet" = None, available_min_id: Optional[int] = None, folder_id: Optional[int] = None, linked_chat_id: Optional[int] = None, location: "ayiin.ChannelLocation" = None, slowmode_seconds: Optional[int] = None, slowmode_next_send_date: Optional[int] = None, stats_dc: Optional[int] = None, call: "ayiin.InputGroupCall" = None, ttl_period: Optional[int] = None, pending_suggestions: Optional[List[str]] = None, groupcall_default_join_as: "ayiin.Peer" = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, default_send_as: "ayiin.Peer" = None, available_reactions: "ayiin.ChatReactions" = None, reactions_limit: Optional[int] = None, stories: "ayiin.PeerStories" = None, wallpaper: "ayiin.WallPaper" = None, boosts_applied: Optional[int] = None, boosts_unrestrict: Optional[int] = None, emojiset: "ayiin.StickerSet" = None) -> None:
        
                self.id = id  # long
        
                self.about = about  # string
        
                self.read_inbox_max_id = read_inbox_max_id  # int
        
                self.read_outbox_max_id = read_outbox_max_id  # int
        
                self.unread_count = unread_count  # int
        
                self.chat_photo = chat_photo  # Photo
        
                self.notify_settings = notify_settings  # PeerNotifySettings
        
                self.bot_info = bot_info  # BotInfo
        
                self.pts = pts  # int
        
                self.can_view_participants = can_view_participants  # true
        
                self.can_set_username = can_set_username  # true
        
                self.can_set_stickers = can_set_stickers  # true
        
                self.hidden_prehistory = hidden_prehistory  # true
        
                self.can_set_location = can_set_location  # true
        
                self.has_scheduled = has_scheduled  # true
        
                self.can_view_stats = can_view_stats  # true
        
                self.blocked = blocked  # true
        
                self.can_delete_channel = can_delete_channel  # true
        
                self.antispam = antispam  # true
        
                self.participants_hidden = participants_hidden  # true
        
                self.translations_disabled = translations_disabled  # true
        
                self.stories_pinned_available = stories_pinned_available  # true
        
                self.view_forum_as_messages = view_forum_as_messages  # true
        
                self.restricted_sponsored = restricted_sponsored  # true
        
                self.can_view_revenue = can_view_revenue  # true
        
                self.participants_count = participants_count  # int
        
                self.admins_count = admins_count  # int
        
                self.kicked_count = kicked_count  # int
        
                self.banned_count = banned_count  # int
        
                self.online_count = online_count  # int
        
                self.exported_invite = exported_invite  # ExportedChatInvite
        
                self.migrated_from_chat_id = migrated_from_chat_id  # long
        
                self.migrated_from_max_id = migrated_from_max_id  # int
        
                self.pinned_msg_id = pinned_msg_id  # int
        
                self.stickerset = stickerset  # StickerSet
        
                self.available_min_id = available_min_id  # int
        
                self.folder_id = folder_id  # int
        
                self.linked_chat_id = linked_chat_id  # long
        
                self.location = location  # ChannelLocation
        
                self.slowmode_seconds = slowmode_seconds  # int
        
                self.slowmode_next_send_date = slowmode_next_send_date  # int
        
                self.stats_dc = stats_dc  # int
        
                self.call = call  # InputGroupCall
        
                self.ttl_period = ttl_period  # int
        
                self.pending_suggestions = pending_suggestions  # string
        
                self.groupcall_default_join_as = groupcall_default_join_as  # Peer
        
                self.theme_emoticon = theme_emoticon  # string
        
                self.requests_pending = requests_pending  # int
        
                self.recent_requesters = recent_requesters  # long
        
                self.default_send_as = default_send_as  # Peer
        
                self.available_reactions = available_reactions  # ChatReactions
        
                self.reactions_limit = reactions_limit  # int
        
                self.stories = stories  # PeerStories
        
                self.wallpaper = wallpaper  # WallPaper
        
                self.boosts_applied = boosts_applied  # int
        
                self.boosts_unrestrict = boosts_unrestrict  # int
        
                self.emojiset = emojiset  # StickerSet

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelFull":
        
        flags = Int.read(b)
        
        can_view_participants = True if flags & (1 << 3) else False
        can_set_username = True if flags & (1 << 6) else False
        can_set_stickers = True if flags & (1 << 7) else False
        hidden_prehistory = True if flags & (1 << 10) else False
        can_set_location = True if flags & (1 << 16) else False
        has_scheduled = True if flags & (1 << 19) else False
        can_view_stats = True if flags & (1 << 20) else False
        blocked = True if flags & (1 << 22) else False
        flags2 = Int.read(b)
        
        can_delete_channel = True if flags2 & (1 << 0) else False
        antispam = True if flags2 & (1 << 1) else False
        participants_hidden = True if flags2 & (1 << 2) else False
        translations_disabled = True if flags2 & (1 << 3) else False
        stories_pinned_available = True if flags2 & (1 << 5) else False
        view_forum_as_messages = True if flags2 & (1 << 6) else False
        restricted_sponsored = True if flags2 & (1 << 11) else False
        can_view_revenue = True if flags2 & (1 << 12) else False
        id = Long.read(b)
        
        about = String.read(b)
        
        participants_count = Int.read(b) if flags & (1 << 0) else None
        admins_count = Int.read(b) if flags & (1 << 1) else None
        kicked_count = Int.read(b) if flags & (1 << 2) else None
        banned_count = Int.read(b) if flags & (1 << 2) else None
        online_count = Int.read(b) if flags & (1 << 13) else None
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        chat_photo = Object.read(b)
        
        notify_settings = Object.read(b)
        
        exported_invite = Object.read(b) if flags & (1 << 23) else None
        
        bot_info = Object.read(b)
        
        migrated_from_chat_id = Long.read(b) if flags & (1 << 4) else None
        migrated_from_max_id = Int.read(b) if flags & (1 << 4) else None
        pinned_msg_id = Int.read(b) if flags & (1 << 5) else None
        stickerset = Object.read(b) if flags & (1 << 8) else None
        
        available_min_id = Int.read(b) if flags & (1 << 9) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        linked_chat_id = Long.read(b) if flags & (1 << 14) else None
        location = Object.read(b) if flags & (1 << 15) else None
        
        slowmode_seconds = Int.read(b) if flags & (1 << 17) else None
        slowmode_next_send_date = Int.read(b) if flags & (1 << 18) else None
        stats_dc = Int.read(b) if flags & (1 << 12) else None
        pts = Int.read(b)
        
        call = Object.read(b) if flags & (1 << 21) else None
        
        ttl_period = Int.read(b) if flags & (1 << 24) else None
        pending_suggestions = Object.read(b, String) if flags & (1 << 25) else []
        
        groupcall_default_join_as = Object.read(b) if flags & (1 << 26) else None
        
        theme_emoticon = String.read(b) if flags & (1 << 27) else None
        requests_pending = Int.read(b) if flags & (1 << 28) else None
        recent_requesters = Object.read(b, Long) if flags & (1 << 28) else []
        
        default_send_as = Object.read(b) if flags & (1 << 29) else None
        
        available_reactions = Object.read(b) if flags & (1 << 30) else None
        
        reactions_limit = Int.read(b) if flags2 & (1 << 13) else None
        stories = Object.read(b) if flags2 & (1 << 4) else None
        
        wallpaper = Object.read(b) if flags2 & (1 << 7) else None
        
        boosts_applied = Int.read(b) if flags2 & (1 << 8) else None
        boosts_unrestrict = Int.read(b) if flags2 & (1 << 9) else None
        emojiset = Object.read(b) if flags2 & (1 << 10) else None
        
        return ChannelFull(id=id, about=about, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, chat_photo=chat_photo, notify_settings=notify_settings, bot_info=bot_info, pts=pts, can_view_participants=can_view_participants, can_set_username=can_set_username, can_set_stickers=can_set_stickers, hidden_prehistory=hidden_prehistory, can_set_location=can_set_location, has_scheduled=has_scheduled, can_view_stats=can_view_stats, blocked=blocked, can_delete_channel=can_delete_channel, antispam=antispam, participants_hidden=participants_hidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, view_forum_as_messages=view_forum_as_messages, restricted_sponsored=restricted_sponsored, can_view_revenue=can_view_revenue, participants_count=participants_count, admins_count=admins_count, kicked_count=kicked_count, banned_count=banned_count, online_count=online_count, exported_invite=exported_invite, migrated_from_chat_id=migrated_from_chat_id, migrated_from_max_id=migrated_from_max_id, pinned_msg_id=pinned_msg_id, stickerset=stickerset, available_min_id=available_min_id, folder_id=folder_id, linked_chat_id=linked_chat_id, location=location, slowmode_seconds=slowmode_seconds, slowmode_next_send_date=slowmode_next_send_date, stats_dc=stats_dc, call=call, ttl_period=ttl_period, pending_suggestions=pending_suggestions, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, default_send_as=default_send_as, available_reactions=available_reactions, reactions_limit=reactions_limit, stories=stories, wallpaper=wallpaper, boosts_applied=boosts_applied, boosts_unrestrict=boosts_unrestrict, emojiset=emojiset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        flags2 = 0
        
        b.write(Int(flags2))
        
        b.write(Long(self.id))
        
        b.write(String(self.about))
        
        if self.participants_count is not None:
            b.write(Int(self.participants_count))
        
        if self.admins_count is not None:
            b.write(Int(self.admins_count))
        
        if self.kicked_count is not None:
            b.write(Int(self.kicked_count))
        
        if self.banned_count is not None:
            b.write(Int(self.banned_count))
        
        if self.online_count is not None:
            b.write(Int(self.online_count))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(self.chat_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.exported_invite is not None:
            b.write(self.exported_invite.write())
        
        b.write(Vector(self.bot_info))
        
        if self.migrated_from_chat_id is not None:
            b.write(Long(self.migrated_from_chat_id))
        
        if self.migrated_from_max_id is not None:
            b.write(Int(self.migrated_from_max_id))
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        if self.stickerset is not None:
            b.write(self.stickerset.write())
        
        if self.available_min_id is not None:
            b.write(Int(self.available_min_id))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.linked_chat_id is not None:
            b.write(Long(self.linked_chat_id))
        
        if self.location is not None:
            b.write(self.location.write())
        
        if self.slowmode_seconds is not None:
            b.write(Int(self.slowmode_seconds))
        
        if self.slowmode_next_send_date is not None:
            b.write(Int(self.slowmode_next_send_date))
        
        if self.stats_dc is not None:
            b.write(Int(self.stats_dc))
        
        b.write(Int(self.pts))
        
        if self.call is not None:
            b.write(self.call.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.pending_suggestions is not None:
            b.write(Vector(self.pending_suggestions, String))
        
        if self.groupcall_default_join_as is not None:
            b.write(self.groupcall_default_join_as.write())
        
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        
        if self.requests_pending is not None:
            b.write(Int(self.requests_pending))
        
        if self.recent_requesters is not None:
            b.write(Vector(self.recent_requesters, Long))
        
        if self.default_send_as is not None:
            b.write(self.default_send_as.write())
        
        if self.available_reactions is not None:
            b.write(self.available_reactions.write())
        
        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))
        
        if self.stories is not None:
            b.write(self.stories.write())
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.boosts_applied is not None:
            b.write(Int(self.boosts_applied))
        
        if self.boosts_unrestrict is not None:
            b.write(Int(self.boosts_unrestrict))
        
        if self.emojiset is not None:
            b.write(self.emojiset.write())
        
        return b.getvalue()