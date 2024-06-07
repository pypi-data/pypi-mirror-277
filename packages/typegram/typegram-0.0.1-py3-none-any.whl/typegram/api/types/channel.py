
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



class Channel(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Chat`.

    Details:
        - Layer: ``181``
        - ID: ``AADFC8F``

id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        photo (:obj:`ChatPhoto<typegram.api.ayiin.ChatPhoto>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        creator (``bool``, *optional*):
                    N/A
                
        left (``bool``, *optional*):
                    N/A
                
        broadcast (``bool``, *optional*):
                    N/A
                
        verified (``bool``, *optional*):
                    N/A
                
        megagroup (``bool``, *optional*):
                    N/A
                
        restricted (``bool``, *optional*):
                    N/A
                
        signatures (``bool``, *optional*):
                    N/A
                
        min (``bool``, *optional*):
                    N/A
                
        scam (``bool``, *optional*):
                    N/A
                
        has_link (``bool``, *optional*):
                    N/A
                
        has_geo (``bool``, *optional*):
                    N/A
                
        slowmode_enabled (``bool``, *optional*):
                    N/A
                
        call_active (``bool``, *optional*):
                    N/A
                
        call_not_empty (``bool``, *optional*):
                    N/A
                
        fake (``bool``, *optional*):
                    N/A
                
        gigagroup (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        join_to_send (``bool``, *optional*):
                    N/A
                
        join_request (``bool``, *optional*):
                    N/A
                
        forum (``bool``, *optional*):
                    N/A
                
        stories_hidden (``bool``, *optional*):
                    N/A
                
        stories_hidden_min (``bool``, *optional*):
                    N/A
                
        stories_unavailable (``bool``, *optional*):
                    N/A
                
        access_hash (``int`` ``64-bit``, *optional*):
                    N/A
                
        username (``str``, *optional*):
                    N/A
                
        restriction_reason (List of :obj:`RestrictionReason<typegram.api.ayiin.RestrictionReason>`, *optional*):
                    N/A
                
        admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`, *optional*):
                    N/A
                
        default_banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`, *optional*):
                    N/A
                
        participants_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        usernames (List of :obj:`Username<typegram.api.ayiin.Username>`, *optional*):
                    N/A
                
        stories_max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        color (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`, *optional*):
                    N/A
                
        profile_color (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`, *optional*):
                    N/A
                
        emoji_status (:obj:`EmojiStatus<typegram.api.ayiin.EmojiStatus>`, *optional*):
                    N/A
                
        level (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["id", "title", "photo", "date", "creator", "left", "broadcast", "verified", "megagroup", "restricted", "signatures", "min", "scam", "has_link", "has_geo", "slowmode_enabled", "call_active", "call_not_empty", "fake", "gigagroup", "noforwards", "join_to_send", "join_request", "forum", "stories_hidden", "stories_hidden_min", "stories_unavailable", "access_hash", "username", "restriction_reason", "admin_rights", "banned_rights", "default_banned_rights", "participants_count", "usernames", "stories_max_id", "color", "profile_color", "emoji_status", "level"]

    ID = 0xaadfc8f
    QUALNAME = "functions.types.Chat"

    def __init__(self, *, id: int, title: str, photo: "ayiin.ChatPhoto", date: int, creator: Optional[bool] = None, left: Optional[bool] = None, broadcast: Optional[bool] = None, verified: Optional[bool] = None, megagroup: Optional[bool] = None, restricted: Optional[bool] = None, signatures: Optional[bool] = None, min: Optional[bool] = None, scam: Optional[bool] = None, has_link: Optional[bool] = None, has_geo: Optional[bool] = None, slowmode_enabled: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, fake: Optional[bool] = None, gigagroup: Optional[bool] = None, noforwards: Optional[bool] = None, join_to_send: Optional[bool] = None, join_request: Optional[bool] = None, forum: Optional[bool] = None, stories_hidden: Optional[bool] = None, stories_hidden_min: Optional[bool] = None, stories_unavailable: Optional[bool] = None, access_hash: Optional[int] = None, username: Optional[str] = None, restriction_reason: Optional[List["ayiin.RestrictionReason"]] = None, admin_rights: "ayiin.ChatAdminRights" = None, banned_rights: "ayiin.ChatBannedRights" = None, default_banned_rights: "ayiin.ChatBannedRights" = None, participants_count: Optional[int] = None, usernames: Optional[List["ayiin.Username"]] = None, stories_max_id: Optional[int] = None, color: "ayiin.PeerColor" = None, profile_color: "ayiin.PeerColor" = None, emoji_status: "ayiin.EmojiStatus" = None, level: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.title = title  # string
        
                self.photo = photo  # ChatPhoto
        
                self.date = date  # int
        
                self.creator = creator  # true
        
                self.left = left  # true
        
                self.broadcast = broadcast  # true
        
                self.verified = verified  # true
        
                self.megagroup = megagroup  # true
        
                self.restricted = restricted  # true
        
                self.signatures = signatures  # true
        
                self.min = min  # true
        
                self.scam = scam  # true
        
                self.has_link = has_link  # true
        
                self.has_geo = has_geo  # true
        
                self.slowmode_enabled = slowmode_enabled  # true
        
                self.call_active = call_active  # true
        
                self.call_not_empty = call_not_empty  # true
        
                self.fake = fake  # true
        
                self.gigagroup = gigagroup  # true
        
                self.noforwards = noforwards  # true
        
                self.join_to_send = join_to_send  # true
        
                self.join_request = join_request  # true
        
                self.forum = forum  # true
        
                self.stories_hidden = stories_hidden  # true
        
                self.stories_hidden_min = stories_hidden_min  # true
        
                self.stories_unavailable = stories_unavailable  # true
        
                self.access_hash = access_hash  # long
        
                self.username = username  # string
        
                self.restriction_reason = restriction_reason  # RestrictionReason
        
                self.admin_rights = admin_rights  # ChatAdminRights
        
                self.banned_rights = banned_rights  # ChatBannedRights
        
                self.default_banned_rights = default_banned_rights  # ChatBannedRights
        
                self.participants_count = participants_count  # int
        
                self.usernames = usernames  # Username
        
                self.stories_max_id = stories_max_id  # int
        
                self.color = color  # PeerColor
        
                self.profile_color = profile_color  # PeerColor
        
                self.emoji_status = emoji_status  # EmojiStatus
        
                self.level = level  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Channel":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        broadcast = True if flags & (1 << 5) else False
        verified = True if flags & (1 << 7) else False
        megagroup = True if flags & (1 << 8) else False
        restricted = True if flags & (1 << 9) else False
        signatures = True if flags & (1 << 11) else False
        min = True if flags & (1 << 12) else False
        scam = True if flags & (1 << 19) else False
        has_link = True if flags & (1 << 20) else False
        has_geo = True if flags & (1 << 21) else False
        slowmode_enabled = True if flags & (1 << 22) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        fake = True if flags & (1 << 25) else False
        gigagroup = True if flags & (1 << 26) else False
        noforwards = True if flags & (1 << 27) else False
        join_to_send = True if flags & (1 << 28) else False
        join_request = True if flags & (1 << 29) else False
        forum = True if flags & (1 << 30) else False
        flags2 = Int.read(b)
        
        stories_hidden = True if flags2 & (1 << 1) else False
        stories_hidden_min = True if flags2 & (1 << 2) else False
        stories_unavailable = True if flags2 & (1 << 3) else False
        id = Long.read(b)
        
        access_hash = Long.read(b) if flags & (1 << 13) else None
        title = String.read(b)
        
        username = String.read(b) if flags & (1 << 6) else None
        photo = Object.read(b)
        
        date = Int.read(b)
        
        restriction_reason = Object.read(b) if flags & (1 << 9) else []
        
        admin_rights = Object.read(b) if flags & (1 << 14) else None
        
        banned_rights = Object.read(b) if flags & (1 << 15) else None
        
        default_banned_rights = Object.read(b) if flags & (1 << 18) else None
        
        participants_count = Int.read(b) if flags & (1 << 17) else None
        usernames = Object.read(b) if flags2 & (1 << 0) else []
        
        stories_max_id = Int.read(b) if flags2 & (1 << 4) else None
        color = Object.read(b) if flags2 & (1 << 7) else None
        
        profile_color = Object.read(b) if flags2 & (1 << 8) else None
        
        emoji_status = Object.read(b) if flags2 & (1 << 9) else None
        
        level = Int.read(b) if flags2 & (1 << 10) else None
        return Channel(id=id, title=title, photo=photo, date=date, creator=creator, left=left, broadcast=broadcast, verified=verified, megagroup=megagroup, restricted=restricted, signatures=signatures, min=min, scam=scam, has_link=has_link, has_geo=has_geo, slowmode_enabled=slowmode_enabled, call_active=call_active, call_not_empty=call_not_empty, fake=fake, gigagroup=gigagroup, noforwards=noforwards, join_to_send=join_to_send, join_request=join_request, forum=forum, stories_hidden=stories_hidden, stories_hidden_min=stories_hidden_min, stories_unavailable=stories_unavailable, access_hash=access_hash, username=username, restriction_reason=restriction_reason, admin_rights=admin_rights, banned_rights=banned_rights, default_banned_rights=default_banned_rights, participants_count=participants_count, usernames=usernames, stories_max_id=stories_max_id, color=color, profile_color=profile_color, emoji_status=emoji_status, level=level)

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
        
        b.write(String(self.title))
        
        if self.username is not None:
            b.write(String(self.username))
        
        b.write(self.photo.write())
        
        b.write(Int(self.date))
        
        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))
        
        if self.admin_rights is not None:
            b.write(self.admin_rights.write())
        
        if self.banned_rights is not None:
            b.write(self.banned_rights.write())
        
        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())
        
        if self.participants_count is not None:
            b.write(Int(self.participants_count))
        
        if self.usernames is not None:
            b.write(Vector(self.usernames))
        
        if self.stories_max_id is not None:
            b.write(Int(self.stories_max_id))
        
        if self.color is not None:
            b.write(self.color.write())
        
        if self.profile_color is not None:
            b.write(self.profile_color.write())
        
        if self.emoji_status is not None:
            b.write(self.emoji_status.write())
        
        if self.level is not None:
            b.write(Int(self.level))
        
        return b.getvalue()