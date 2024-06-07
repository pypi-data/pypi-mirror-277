
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



class Message(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Message`.

    Details:
        - Layer: ``181``
        - ID: ``94345242``

id (``int`` ``32-bit``):
                    N/A
                
        peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        message (``str``):
                    N/A
                
        out (``bool``, *optional*):
                    N/A
                
        mentioned (``bool``, *optional*):
                    N/A
                
        media_unread (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        post (``bool``, *optional*):
                    N/A
                
        from_scheduled (``bool``, *optional*):
                    N/A
                
        legacy (``bool``, *optional*):
                    N/A
                
        edit_hide (``bool``, *optional*):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        offline (``bool``, *optional*):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        from_boosts_applied (``int`` ``32-bit``, *optional*):
                    N/A
                
        saved_peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        fwd_from (:obj:`MessageFwdHeader<typegram.api.ayiin.MessageFwdHeader>`, *optional*):
                    N/A
                
        via_bot_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        via_business_bot_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        reply_to (:obj:`MessageReplyHeader<typegram.api.ayiin.MessageReplyHeader>`, *optional*):
                    N/A
                
        media (:obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        views (``int`` ``32-bit``, *optional*):
                    N/A
                
        forwards (``int`` ``32-bit``, *optional*):
                    N/A
                
        replies (:obj:`MessageReplies<typegram.api.ayiin.MessageReplies>`, *optional*):
                    N/A
                
        edit_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        post_author (``str``, *optional*):
                    N/A
                
        grouped_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        reactions (:obj:`MessageReactions<typegram.api.ayiin.MessageReactions>`, *optional*):
                    N/A
                
        restriction_reason (List of :obj:`RestrictionReason<typegram.api.ayiin.RestrictionReason>`, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        quick_reply_shortcut_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        effect (``int`` ``64-bit``, *optional*):
                    N/A
                
        factcheck (:obj:`FactCheck<typegram.api.ayiin.FactCheck>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

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

    __slots__: List[str] = ["id", "peer_id", "date", "message", "out", "mentioned", "media_unread", "silent", "post", "from_scheduled", "legacy", "edit_hide", "pinned", "noforwards", "invert_media", "offline", "from_id", "from_boosts_applied", "saved_peer_id", "fwd_from", "via_bot_id", "via_business_bot_id", "reply_to", "media", "reply_markup", "entities", "views", "forwards", "replies", "edit_date", "post_author", "grouped_id", "reactions", "restriction_reason", "ttl_period", "quick_reply_shortcut_id", "effect", "factcheck"]

    ID = 0x94345242
    QUALNAME = "functions.types.Message"

    def __init__(self, *, id: int, peer_id: "ayiin.Peer", date: int, message: str, out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, post: Optional[bool] = None, from_scheduled: Optional[bool] = None, legacy: Optional[bool] = None, edit_hide: Optional[bool] = None, pinned: Optional[bool] = None, noforwards: Optional[bool] = None, invert_media: Optional[bool] = None, offline: Optional[bool] = None, from_id: "ayiin.Peer" = None, from_boosts_applied: Optional[int] = None, saved_peer_id: "ayiin.Peer" = None, fwd_from: "ayiin.MessageFwdHeader" = None, via_bot_id: Optional[int] = None, via_business_bot_id: Optional[int] = None, reply_to: "ayiin.MessageReplyHeader" = None, media: "ayiin.MessageMedia" = None, reply_markup: "ayiin.ReplyMarkup" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, views: Optional[int] = None, forwards: Optional[int] = None, replies: "ayiin.MessageReplies" = None, edit_date: Optional[int] = None, post_author: Optional[str] = None, grouped_id: Optional[int] = None, reactions: "ayiin.MessageReactions" = None, restriction_reason: Optional[List["ayiin.RestrictionReason"]] = None, ttl_period: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None, effect: Optional[int] = None, factcheck: "ayiin.FactCheck" = None) -> None:
        
                self.id = id  # int
        
                self.peer_id = peer_id  # Peer
        
                self.date = date  # int
        
                self.message = message  # string
        
                self.out = out  # true
        
                self.mentioned = mentioned  # true
        
                self.media_unread = media_unread  # true
        
                self.silent = silent  # true
        
                self.post = post  # true
        
                self.from_scheduled = from_scheduled  # true
        
                self.legacy = legacy  # true
        
                self.edit_hide = edit_hide  # true
        
                self.pinned = pinned  # true
        
                self.noforwards = noforwards  # true
        
                self.invert_media = invert_media  # true
        
                self.offline = offline  # true
        
                self.from_id = from_id  # Peer
        
                self.from_boosts_applied = from_boosts_applied  # int
        
                self.saved_peer_id = saved_peer_id  # Peer
        
                self.fwd_from = fwd_from  # MessageFwdHeader
        
                self.via_bot_id = via_bot_id  # long
        
                self.via_business_bot_id = via_business_bot_id  # long
        
                self.reply_to = reply_to  # MessageReplyHeader
        
                self.media = media  # MessageMedia
        
                self.reply_markup = reply_markup  # ReplyMarkup
        
                self.entities = entities  # MessageEntity
        
                self.views = views  # int
        
                self.forwards = forwards  # int
        
                self.replies = replies  # MessageReplies
        
                self.edit_date = edit_date  # int
        
                self.post_author = post_author  # string
        
                self.grouped_id = grouped_id  # long
        
                self.reactions = reactions  # MessageReactions
        
                self.restriction_reason = restriction_reason  # RestrictionReason
        
                self.ttl_period = ttl_period  # int
        
                self.quick_reply_shortcut_id = quick_reply_shortcut_id  # int
        
                self.effect = effect  # long
        
                self.factcheck = factcheck  # FactCheck

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Message":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        from_scheduled = True if flags & (1 << 18) else False
        legacy = True if flags & (1 << 19) else False
        edit_hide = True if flags & (1 << 21) else False
        pinned = True if flags & (1 << 24) else False
        noforwards = True if flags & (1 << 26) else False
        invert_media = True if flags & (1 << 27) else False
        flags2 = Int.read(b)
        
        offline = True if flags2 & (1 << 1) else False
        id = Int.read(b)
        
        from_id = Object.read(b) if flags & (1 << 8) else None
        
        from_boosts_applied = Int.read(b) if flags & (1 << 29) else None
        peer_id = Object.read(b)
        
        saved_peer_id = Object.read(b) if flags & (1 << 28) else None
        
        fwd_from = Object.read(b) if flags & (1 << 2) else None
        
        via_bot_id = Long.read(b) if flags & (1 << 11) else None
        via_business_bot_id = Long.read(b) if flags2 & (1 << 0) else None
        reply_to = Object.read(b) if flags & (1 << 3) else None
        
        date = Int.read(b)
        
        message = String.read(b)
        
        media = Object.read(b) if flags & (1 << 9) else None
        
        reply_markup = Object.read(b) if flags & (1 << 6) else None
        
        entities = Object.read(b) if flags & (1 << 7) else []
        
        views = Int.read(b) if flags & (1 << 10) else None
        forwards = Int.read(b) if flags & (1 << 10) else None
        replies = Object.read(b) if flags & (1 << 23) else None
        
        edit_date = Int.read(b) if flags & (1 << 15) else None
        post_author = String.read(b) if flags & (1 << 16) else None
        grouped_id = Long.read(b) if flags & (1 << 17) else None
        reactions = Object.read(b) if flags & (1 << 20) else None
        
        restriction_reason = Object.read(b) if flags & (1 << 22) else []
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        quick_reply_shortcut_id = Int.read(b) if flags & (1 << 30) else None
        effect = Long.read(b) if flags2 & (1 << 2) else None
        factcheck = Object.read(b) if flags2 & (1 << 3) else None
        
        return Message(id=id, peer_id=peer_id, date=date, message=message, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, from_scheduled=from_scheduled, legacy=legacy, edit_hide=edit_hide, pinned=pinned, noforwards=noforwards, invert_media=invert_media, offline=offline, from_id=from_id, from_boosts_applied=from_boosts_applied, saved_peer_id=saved_peer_id, fwd_from=fwd_from, via_bot_id=via_bot_id, via_business_bot_id=via_business_bot_id, reply_to=reply_to, media=media, reply_markup=reply_markup, entities=entities, views=views, forwards=forwards, replies=replies, edit_date=edit_date, post_author=post_author, grouped_id=grouped_id, reactions=reactions, restriction_reason=restriction_reason, ttl_period=ttl_period, quick_reply_shortcut_id=quick_reply_shortcut_id, effect=effect, factcheck=factcheck)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        flags2 = 0
        
        b.write(Int(flags2))
        
        b.write(Int(self.id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.from_boosts_applied is not None:
            b.write(Int(self.from_boosts_applied))
        
        b.write(self.peer_id.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.fwd_from is not None:
            b.write(self.fwd_from.write())
        
        if self.via_bot_id is not None:
            b.write(Long(self.via_bot_id))
        
        if self.via_business_bot_id is not None:
            b.write(Long(self.via_business_bot_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Int(self.date))
        
        b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        if self.forwards is not None:
            b.write(Int(self.forwards))
        
        if self.replies is not None:
            b.write(self.replies.write())
        
        if self.edit_date is not None:
            b.write(Int(self.edit_date))
        
        if self.post_author is not None:
            b.write(String(self.post_author))
        
        if self.grouped_id is not None:
            b.write(Long(self.grouped_id))
        
        if self.reactions is not None:
            b.write(self.reactions.write())
        
        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.quick_reply_shortcut_id is not None:
            b.write(Int(self.quick_reply_shortcut_id))
        
        if self.effect is not None:
            b.write(Long(self.effect))
        
        if self.factcheck is not None:
            b.write(self.factcheck.write())
        
        return b.getvalue()