
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



class UpdateShortChatMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Updates`.

    Details:
        - Layer: ``181``
        - ID: ``4D6DEEA5``

id (``int`` ``32-bit``):
                    N/A
                
        from_id (``int`` ``64-bit``):
                    N/A
                
        chat_id (``int`` ``64-bit``):
                    N/A
                
        message (``str``):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        out (``bool``, *optional*):
                    N/A
                
        mentioned (``bool``, *optional*):
                    N/A
                
        media_unread (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        fwd_from (:obj:`MessageFwdHeader<typegram.api.ayiin.MessageFwdHeader>`, *optional*):
                    N/A
                
        via_bot_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        reply_to (:obj:`MessageReplyHeader<typegram.api.ayiin.MessageReplyHeader>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["id", "from_id", "chat_id", "message", "pts", "pts_count", "date", "out", "mentioned", "media_unread", "silent", "fwd_from", "via_bot_id", "reply_to", "entities", "ttl_period"]

    ID = 0x4d6deea5
    QUALNAME = "functions.types.Updates"

    def __init__(self, *, id: int, from_id: int, chat_id: int, message: str, pts: int, pts_count: int, date: int, out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, fwd_from: "ayiin.MessageFwdHeader" = None, via_bot_id: Optional[int] = None, reply_to: "ayiin.MessageReplyHeader" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, ttl_period: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.from_id = from_id  # long
        
                self.chat_id = chat_id  # long
        
                self.message = message  # string
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int
        
                self.date = date  # int
        
                self.out = out  # true
        
                self.mentioned = mentioned  # true
        
                self.media_unread = media_unread  # true
        
                self.silent = silent  # true
        
                self.fwd_from = fwd_from  # MessageFwdHeader
        
                self.via_bot_id = via_bot_id  # long
        
                self.reply_to = reply_to  # MessageReplyHeader
        
                self.entities = entities  # MessageEntity
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateShortChatMessage":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        id = Int.read(b)
        
        from_id = Long.read(b)
        
        chat_id = Long.read(b)
        
        message = String.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b)
        
        fwd_from = Object.read(b) if flags & (1 << 2) else None
        
        via_bot_id = Long.read(b) if flags & (1 << 11) else None
        reply_to = Object.read(b) if flags & (1 << 3) else None
        
        entities = Object.read(b) if flags & (1 << 7) else []
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return UpdateShortChatMessage(id=id, from_id=from_id, chat_id=chat_id, message=message, pts=pts, pts_count=pts_count, date=date, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, fwd_from=fwd_from, via_bot_id=via_bot_id, reply_to=reply_to, entities=entities, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Long(self.from_id))
        
        b.write(Long(self.chat_id))
        
        b.write(String(self.message))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.date))
        
        if self.fwd_from is not None:
            b.write(self.fwd_from.write())
        
        if self.via_bot_id is not None:
            b.write(Long(self.via_bot_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()