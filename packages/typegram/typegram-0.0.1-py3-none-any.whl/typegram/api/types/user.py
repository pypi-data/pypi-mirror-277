
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



class User(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.User`.

    Details:
        - Layer: ``181``
        - ID: ``215C4438``

id (``int`` ``64-bit``):
                    N/A
                
        is_self (``bool``, *optional*):
                    N/A
                
        contact (``bool``, *optional*):
                    N/A
                
        mutual_contact (``bool``, *optional*):
                    N/A
                
        deleted (``bool``, *optional*):
                    N/A
                
        bot (``bool``, *optional*):
                    N/A
                
        bot_chat_history (``bool``, *optional*):
                    N/A
                
        bot_nochats (``bool``, *optional*):
                    N/A
                
        verified (``bool``, *optional*):
                    N/A
                
        restricted (``bool``, *optional*):
                    N/A
                
        min (``bool``, *optional*):
                    N/A
                
        bot_inline_geo (``bool``, *optional*):
                    N/A
                
        support (``bool``, *optional*):
                    N/A
                
        scam (``bool``, *optional*):
                    N/A
                
        apply_min_photo (``bool``, *optional*):
                    N/A
                
        fake (``bool``, *optional*):
                    N/A
                
        bot_attach_menu (``bool``, *optional*):
                    N/A
                
        premium (``bool``, *optional*):
                    N/A
                
        attach_menu_enabled (``bool``, *optional*):
                    N/A
                
        bot_can_edit (``bool``, *optional*):
                    N/A
                
        close_friend (``bool``, *optional*):
                    N/A
                
        stories_hidden (``bool``, *optional*):
                    N/A
                
        stories_unavailable (``bool``, *optional*):
                    N/A
                
        contact_require_premium (``bool``, *optional*):
                    N/A
                
        bot_business (``bool``, *optional*):
                    N/A
                
        access_hash (``int`` ``64-bit``, *optional*):
                    N/A
                
        first_name (``str``, *optional*):
                    N/A
                
        last_name (``str``, *optional*):
                    N/A
                
        username (``str``, *optional*):
                    N/A
                
        phone (``str``, *optional*):
                    N/A
                
        photo (:obj:`UserProfilePhoto<typegram.api.ayiin.UserProfilePhoto>`, *optional*):
                    N/A
                
        status (:obj:`UserStatus<typegram.api.ayiin.UserStatus>`, *optional*):
                    N/A
                
        bot_info_version (``int`` ``32-bit``, *optional*):
                    N/A
                
        restriction_reason (List of :obj:`RestrictionReason<typegram.api.ayiin.RestrictionReason>`, *optional*):
                    N/A
                
        bot_inline_placeholder (``str``, *optional*):
                    N/A
                
        lang_code (``str``, *optional*):
                    N/A
                
        emoji_status (:obj:`EmojiStatus<typegram.api.ayiin.EmojiStatus>`, *optional*):
                    N/A
                
        usernames (List of :obj:`Username<typegram.api.ayiin.Username>`, *optional*):
                    N/A
                
        stories_max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        color (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`, *optional*):
                    N/A
                
        profile_color (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 5 functions.

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

    __slots__: List[str] = ["id", "is_self", "contact", "mutual_contact", "deleted", "bot", "bot_chat_history", "bot_nochats", "verified", "restricted", "min", "bot_inline_geo", "support", "scam", "apply_min_photo", "fake", "bot_attach_menu", "premium", "attach_menu_enabled", "bot_can_edit", "close_friend", "stories_hidden", "stories_unavailable", "contact_require_premium", "bot_business", "access_hash", "first_name", "last_name", "username", "phone", "photo", "status", "bot_info_version", "restriction_reason", "bot_inline_placeholder", "lang_code", "emoji_status", "usernames", "stories_max_id", "color", "profile_color"]

    ID = 0x215c4438
    QUALNAME = "functions.types.User"

    def __init__(self, *, id: int, is_self: Optional[bool] = None, contact: Optional[bool] = None, mutual_contact: Optional[bool] = None, deleted: Optional[bool] = None, bot: Optional[bool] = None, bot_chat_history: Optional[bool] = None, bot_nochats: Optional[bool] = None, verified: Optional[bool] = None, restricted: Optional[bool] = None, min: Optional[bool] = None, bot_inline_geo: Optional[bool] = None, support: Optional[bool] = None, scam: Optional[bool] = None, apply_min_photo: Optional[bool] = None, fake: Optional[bool] = None, bot_attach_menu: Optional[bool] = None, premium: Optional[bool] = None, attach_menu_enabled: Optional[bool] = None, bot_can_edit: Optional[bool] = None, close_friend: Optional[bool] = None, stories_hidden: Optional[bool] = None, stories_unavailable: Optional[bool] = None, contact_require_premium: Optional[bool] = None, bot_business: Optional[bool] = None, access_hash: Optional[int] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, phone: Optional[str] = None, photo: "ayiin.UserProfilePhoto" = None, status: "ayiin.UserStatus" = None, bot_info_version: Optional[int] = None, restriction_reason: Optional[List["ayiin.RestrictionReason"]] = None, bot_inline_placeholder: Optional[str] = None, lang_code: Optional[str] = None, emoji_status: "ayiin.EmojiStatus" = None, usernames: Optional[List["ayiin.Username"]] = None, stories_max_id: Optional[int] = None, color: "ayiin.PeerColor" = None, profile_color: "ayiin.PeerColor" = None) -> None:
        
                self.id = id  # long
        
                self.is_self = is_self  # true
        
                self.contact = contact  # true
        
                self.mutual_contact = mutual_contact  # true
        
                self.deleted = deleted  # true
        
                self.bot = bot  # true
        
                self.bot_chat_history = bot_chat_history  # true
        
                self.bot_nochats = bot_nochats  # true
        
                self.verified = verified  # true
        
                self.restricted = restricted  # true
        
                self.min = min  # true
        
                self.bot_inline_geo = bot_inline_geo  # true
        
                self.support = support  # true
        
                self.scam = scam  # true
        
                self.apply_min_photo = apply_min_photo  # true
        
                self.fake = fake  # true
        
                self.bot_attach_menu = bot_attach_menu  # true
        
                self.premium = premium  # true
        
                self.attach_menu_enabled = attach_menu_enabled  # true
        
                self.bot_can_edit = bot_can_edit  # true
        
                self.close_friend = close_friend  # true
        
                self.stories_hidden = stories_hidden  # true
        
                self.stories_unavailable = stories_unavailable  # true
        
                self.contact_require_premium = contact_require_premium  # true
        
                self.bot_business = bot_business  # true
        
                self.access_hash = access_hash  # long
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.username = username  # string
        
                self.phone = phone  # string
        
                self.photo = photo  # UserProfilePhoto
        
                self.status = status  # UserStatus
        
                self.bot_info_version = bot_info_version  # int
        
                self.restriction_reason = restriction_reason  # RestrictionReason
        
                self.bot_inline_placeholder = bot_inline_placeholder  # string
        
                self.lang_code = lang_code  # string
        
                self.emoji_status = emoji_status  # EmojiStatus
        
                self.usernames = usernames  # Username
        
                self.stories_max_id = stories_max_id  # int
        
                self.color = color  # PeerColor
        
                self.profile_color = profile_color  # PeerColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "User":
        
        flags = Int.read(b)
        
        is_self = True if flags & (1 << 10) else False
        contact = True if flags & (1 << 11) else False
        mutual_contact = True if flags & (1 << 12) else False
        deleted = True if flags & (1 << 13) else False
        bot = True if flags & (1 << 14) else False
        bot_chat_history = True if flags & (1 << 15) else False
        bot_nochats = True if flags & (1 << 16) else False
        verified = True if flags & (1 << 17) else False
        restricted = True if flags & (1 << 18) else False
        min = True if flags & (1 << 20) else False
        bot_inline_geo = True if flags & (1 << 21) else False
        support = True if flags & (1 << 23) else False
        scam = True if flags & (1 << 24) else False
        apply_min_photo = True if flags & (1 << 25) else False
        fake = True if flags & (1 << 26) else False
        bot_attach_menu = True if flags & (1 << 27) else False
        premium = True if flags & (1 << 28) else False
        attach_menu_enabled = True if flags & (1 << 29) else False
        flags2 = Int.read(b)
        
        bot_can_edit = True if flags2 & (1 << 1) else False
        close_friend = True if flags2 & (1 << 2) else False
        stories_hidden = True if flags2 & (1 << 3) else False
        stories_unavailable = True if flags2 & (1 << 4) else False
        contact_require_premium = True if flags2 & (1 << 10) else False
        bot_business = True if flags2 & (1 << 11) else False
        id = Long.read(b)
        
        access_hash = Long.read(b) if flags & (1 << 0) else None
        first_name = String.read(b) if flags & (1 << 1) else None
        last_name = String.read(b) if flags & (1 << 2) else None
        username = String.read(b) if flags & (1 << 3) else None
        phone = String.read(b) if flags & (1 << 4) else None
        photo = Object.read(b) if flags & (1 << 5) else None
        
        status = Object.read(b) if flags & (1 << 6) else None
        
        bot_info_version = Int.read(b) if flags & (1 << 14) else None
        restriction_reason = Object.read(b) if flags & (1 << 18) else []
        
        bot_inline_placeholder = String.read(b) if flags & (1 << 19) else None
        lang_code = String.read(b) if flags & (1 << 22) else None
        emoji_status = Object.read(b) if flags & (1 << 30) else None
        
        usernames = Object.read(b) if flags2 & (1 << 0) else []
        
        stories_max_id = Int.read(b) if flags2 & (1 << 5) else None
        color = Object.read(b) if flags2 & (1 << 8) else None
        
        profile_color = Object.read(b) if flags2 & (1 << 9) else None
        
        return User(id=id, is_self=is_self, contact=contact, mutual_contact=mutual_contact, deleted=deleted, bot=bot, bot_chat_history=bot_chat_history, bot_nochats=bot_nochats, verified=verified, restricted=restricted, min=min, bot_inline_geo=bot_inline_geo, support=support, scam=scam, apply_min_photo=apply_min_photo, fake=fake, bot_attach_menu=bot_attach_menu, premium=premium, attach_menu_enabled=attach_menu_enabled, bot_can_edit=bot_can_edit, close_friend=close_friend, stories_hidden=stories_hidden, stories_unavailable=stories_unavailable, contact_require_premium=contact_require_premium, bot_business=bot_business, access_hash=access_hash, first_name=first_name, last_name=last_name, username=username, phone=phone, photo=photo, status=status, bot_info_version=bot_info_version, restriction_reason=restriction_reason, bot_inline_placeholder=bot_inline_placeholder, lang_code=lang_code, emoji_status=emoji_status, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        flags2 = 0
        
        b.write(Int(flags2))
        
        b.write(Long(self.id))
        
        if self.access_hash is not None:
            b.write(Long(self.access_hash))
        
        if self.first_name is not None:
            b.write(String(self.first_name))
        
        if self.last_name is not None:
            b.write(String(self.last_name))
        
        if self.username is not None:
            b.write(String(self.username))
        
        if self.phone is not None:
            b.write(String(self.phone))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.status is not None:
            b.write(self.status.write())
        
        if self.bot_info_version is not None:
            b.write(Int(self.bot_info_version))
        
        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))
        
        if self.bot_inline_placeholder is not None:
            b.write(String(self.bot_inline_placeholder))
        
        if self.lang_code is not None:
            b.write(String(self.lang_code))
        
        if self.emoji_status is not None:
            b.write(self.emoji_status.write())
        
        if self.usernames is not None:
            b.write(Vector(self.usernames))
        
        if self.stories_max_id is not None:
            b.write(Int(self.stories_max_id))
        
        if self.color is not None:
            b.write(self.color.write())
        
        if self.profile_color is not None:
            b.write(self.profile_color.write())
        
        return b.getvalue()