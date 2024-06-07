
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



class UserFull(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.UserFull`.

    Details:
        - Layer: ``181``
        - ID: ``CC997720``

id (``int`` ``64-bit``):
                    N/A
                
        settings (:obj:`PeerSettings<typegram.api.ayiin.PeerSettings>`):
                    N/A
                
        notify_settings (:obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`):
                    N/A
                
        common_chats_count (``int`` ``32-bit``):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        phone_calls_available (``bool``, *optional*):
                    N/A
                
        phone_calls_private (``bool``, *optional*):
                    N/A
                
        can_pin_message (``bool``, *optional*):
                    N/A
                
        has_scheduled (``bool``, *optional*):
                    N/A
                
        video_calls_available (``bool``, *optional*):
                    N/A
                
        voice_messages_forbidden (``bool``, *optional*):
                    N/A
                
        translations_disabled (``bool``, *optional*):
                    N/A
                
        stories_pinned_available (``bool``, *optional*):
                    N/A
                
        blocked_my_stories_from (``bool``, *optional*):
                    N/A
                
        wallpaper_overridden (``bool``, *optional*):
                    N/A
                
        contact_require_premium (``bool``, *optional*):
                    N/A
                
        read_dates_private (``bool``, *optional*):
                    N/A
                
        sponsored_enabled (``bool``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
        personal_photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        profile_photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        fallback_photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        bot_info (:obj:`BotInfo<typegram.api.ayiin.BotInfo>`, *optional*):
                    N/A
                
        pinned_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        theme_emoticon (``str``, *optional*):
                    N/A
                
        private_forward_name (``str``, *optional*):
                    N/A
                
        bot_group_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        bot_broadcast_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        premium_gifts (List of :obj:`PremiumGiftOption<typegram.api.ayiin.PremiumGiftOption>`, *optional*):
                    N/A
                
        wallpaper (:obj:`WallPaper<typegram.api.ayiin.WallPaper>`, *optional*):
                    N/A
                
        stories (:obj:`PeerStories<typegram.api.ayiin.PeerStories>`, *optional*):
                    N/A
                
        business_work_hours (:obj:`BusinessWorkHours<typegram.api.ayiin.BusinessWorkHours>`, *optional*):
                    N/A
                
        business_location (:obj:`BusinessLocation<typegram.api.ayiin.BusinessLocation>`, *optional*):
                    N/A
                
        business_greeting_message (:obj:`BusinessGreetingMessage<typegram.api.ayiin.BusinessGreetingMessage>`, *optional*):
                    N/A
                
        business_away_message (:obj:`BusinessAwayMessage<typegram.api.ayiin.BusinessAwayMessage>`, *optional*):
                    N/A
                
        business_intro (:obj:`BusinessIntro<typegram.api.ayiin.BusinessIntro>`, *optional*):
                    N/A
                
        birthday (:obj:`Birthday<typegram.api.ayiin.Birthday>`, *optional*):
                    N/A
                
        personal_channel_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        personal_channel_message (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["id", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "video_calls_available", "voice_messages_forbidden", "translations_disabled", "stories_pinned_available", "blocked_my_stories_from", "wallpaper_overridden", "contact_require_premium", "read_dates_private", "sponsored_enabled", "about", "personal_photo", "profile_photo", "fallback_photo", "bot_info", "pinned_msg_id", "folder_id", "ttl_period", "theme_emoticon", "private_forward_name", "bot_group_admin_rights", "bot_broadcast_admin_rights", "premium_gifts", "wallpaper", "stories", "business_work_hours", "business_location", "business_greeting_message", "business_away_message", "business_intro", "birthday", "personal_channel_id", "personal_channel_message"]

    ID = 0xcc997720
    QUALNAME = "functions.types.UserFull"

    def __init__(self, *, id: int, settings: "ayiin.PeerSettings", notify_settings: "ayiin.PeerNotifySettings", common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, voice_messages_forbidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, wallpaper_overridden: Optional[bool] = None, contact_require_premium: Optional[bool] = None, read_dates_private: Optional[bool] = None, sponsored_enabled: Optional[bool] = None, about: Optional[str] = None, personal_photo: "ayiin.Photo" = None, profile_photo: "ayiin.Photo" = None, fallback_photo: "ayiin.Photo" = None, bot_info: "ayiin.BotInfo" = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme_emoticon: Optional[str] = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: "ayiin.ChatAdminRights" = None, bot_broadcast_admin_rights: "ayiin.ChatAdminRights" = None, premium_gifts: Optional[List["ayiin.PremiumGiftOption"]] = None, wallpaper: "ayiin.WallPaper" = None, stories: "ayiin.PeerStories" = None, business_work_hours: "ayiin.BusinessWorkHours" = None, business_location: "ayiin.BusinessLocation" = None, business_greeting_message: "ayiin.BusinessGreetingMessage" = None, business_away_message: "ayiin.BusinessAwayMessage" = None, business_intro: "ayiin.BusinessIntro" = None, birthday: "ayiin.Birthday" = None, personal_channel_id: Optional[int] = None, personal_channel_message: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.settings = settings  # PeerSettings
        
                self.notify_settings = notify_settings  # PeerNotifySettings
        
                self.common_chats_count = common_chats_count  # int
        
                self.blocked = blocked  # true
        
                self.phone_calls_available = phone_calls_available  # true
        
                self.phone_calls_private = phone_calls_private  # true
        
                self.can_pin_message = can_pin_message  # true
        
                self.has_scheduled = has_scheduled  # true
        
                self.video_calls_available = video_calls_available  # true
        
                self.voice_messages_forbidden = voice_messages_forbidden  # true
        
                self.translations_disabled = translations_disabled  # true
        
                self.stories_pinned_available = stories_pinned_available  # true
        
                self.blocked_my_stories_from = blocked_my_stories_from  # true
        
                self.wallpaper_overridden = wallpaper_overridden  # true
        
                self.contact_require_premium = contact_require_premium  # true
        
                self.read_dates_private = read_dates_private  # true
        
                self.sponsored_enabled = sponsored_enabled  # true
        
                self.about = about  # string
        
                self.personal_photo = personal_photo  # Photo
        
                self.profile_photo = profile_photo  # Photo
        
                self.fallback_photo = fallback_photo  # Photo
        
                self.bot_info = bot_info  # BotInfo
        
                self.pinned_msg_id = pinned_msg_id  # int
        
                self.folder_id = folder_id  # int
        
                self.ttl_period = ttl_period  # int
        
                self.theme_emoticon = theme_emoticon  # string
        
                self.private_forward_name = private_forward_name  # string
        
                self.bot_group_admin_rights = bot_group_admin_rights  # ChatAdminRights
        
                self.bot_broadcast_admin_rights = bot_broadcast_admin_rights  # ChatAdminRights
        
                self.premium_gifts = premium_gifts  # PremiumGiftOption
        
                self.wallpaper = wallpaper  # WallPaper
        
                self.stories = stories  # PeerStories
        
                self.business_work_hours = business_work_hours  # BusinessWorkHours
        
                self.business_location = business_location  # BusinessLocation
        
                self.business_greeting_message = business_greeting_message  # BusinessGreetingMessage
        
                self.business_away_message = business_away_message  # BusinessAwayMessage
        
                self.business_intro = business_intro  # BusinessIntro
        
                self.birthday = birthday  # Birthday
        
                self.personal_channel_id = personal_channel_id  # long
        
                self.personal_channel_message = personal_channel_message  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserFull":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        video_calls_available = True if flags & (1 << 13) else False
        voice_messages_forbidden = True if flags & (1 << 20) else False
        translations_disabled = True if flags & (1 << 23) else False
        stories_pinned_available = True if flags & (1 << 26) else False
        blocked_my_stories_from = True if flags & (1 << 27) else False
        wallpaper_overridden = True if flags & (1 << 28) else False
        contact_require_premium = True if flags & (1 << 29) else False
        read_dates_private = True if flags & (1 << 30) else False
        flags2 = Int.read(b)
        
        sponsored_enabled = True if flags2 & (1 << 7) else False
        id = Long.read(b)
        
        about = String.read(b) if flags & (1 << 1) else None
        settings = Object.read(b)
        
        personal_photo = Object.read(b) if flags & (1 << 21) else None
        
        profile_photo = Object.read(b) if flags & (1 << 2) else None
        
        fallback_photo = Object.read(b) if flags & (1 << 22) else None
        
        notify_settings = Object.read(b)
        
        bot_info = Object.read(b) if flags & (1 << 3) else None
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        common_chats_count = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 11) else None
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        theme_emoticon = String.read(b) if flags & (1 << 15) else None
        private_forward_name = String.read(b) if flags & (1 << 16) else None
        bot_group_admin_rights = Object.read(b) if flags & (1 << 17) else None
        
        bot_broadcast_admin_rights = Object.read(b) if flags & (1 << 18) else None
        
        premium_gifts = Object.read(b) if flags & (1 << 19) else []
        
        wallpaper = Object.read(b) if flags & (1 << 24) else None
        
        stories = Object.read(b) if flags & (1 << 25) else None
        
        business_work_hours = Object.read(b) if flags2 & (1 << 0) else None
        
        business_location = Object.read(b) if flags2 & (1 << 1) else None
        
        business_greeting_message = Object.read(b) if flags2 & (1 << 2) else None
        
        business_away_message = Object.read(b) if flags2 & (1 << 3) else None
        
        business_intro = Object.read(b) if flags2 & (1 << 4) else None
        
        birthday = Object.read(b) if flags2 & (1 << 5) else None
        
        personal_channel_id = Long.read(b) if flags2 & (1 << 6) else None
        personal_channel_message = Int.read(b) if flags2 & (1 << 6) else None
        return UserFull(id=id, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, video_calls_available=video_calls_available, voice_messages_forbidden=voice_messages_forbidden, translations_disabled=translations_disabled, stories_pinned_available=stories_pinned_available, blocked_my_stories_from=blocked_my_stories_from, wallpaper_overridden=wallpaper_overridden, contact_require_premium=contact_require_premium, read_dates_private=read_dates_private, sponsored_enabled=sponsored_enabled, about=about, personal_photo=personal_photo, profile_photo=profile_photo, fallback_photo=fallback_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, ttl_period=ttl_period, theme_emoticon=theme_emoticon, private_forward_name=private_forward_name, bot_group_admin_rights=bot_group_admin_rights, bot_broadcast_admin_rights=bot_broadcast_admin_rights, premium_gifts=premium_gifts, wallpaper=wallpaper, stories=stories, business_work_hours=business_work_hours, business_location=business_location, business_greeting_message=business_greeting_message, business_away_message=business_away_message, business_intro=business_intro, birthday=birthday, personal_channel_id=personal_channel_id, personal_channel_message=personal_channel_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        flags2 = 0
        
        b.write(Int(flags2))
        
        b.write(Long(self.id))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.settings.write())
        
        if self.personal_photo is not None:
            b.write(self.personal_photo.write())
        
        if self.profile_photo is not None:
            b.write(self.profile_photo.write())
        
        if self.fallback_photo is not None:
            b.write(self.fallback_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            b.write(self.bot_info.write())
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        b.write(Int(self.common_chats_count))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        
        if self.private_forward_name is not None:
            b.write(String(self.private_forward_name))
        
        if self.bot_group_admin_rights is not None:
            b.write(self.bot_group_admin_rights.write())
        
        if self.bot_broadcast_admin_rights is not None:
            b.write(self.bot_broadcast_admin_rights.write())
        
        if self.premium_gifts is not None:
            b.write(Vector(self.premium_gifts))
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.stories is not None:
            b.write(self.stories.write())
        
        if self.business_work_hours is not None:
            b.write(self.business_work_hours.write())
        
        if self.business_location is not None:
            b.write(self.business_location.write())
        
        if self.business_greeting_message is not None:
            b.write(self.business_greeting_message.write())
        
        if self.business_away_message is not None:
            b.write(self.business_away_message.write())
        
        if self.business_intro is not None:
            b.write(self.business_intro.write())
        
        if self.birthday is not None:
            b.write(self.birthday.write())
        
        if self.personal_channel_id is not None:
            b.write(Long(self.personal_channel_id))
        
        if self.personal_channel_message is not None:
            b.write(Int(self.personal_channel_message))
        
        return b.getvalue()