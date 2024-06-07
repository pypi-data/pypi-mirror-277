
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



class MessageService(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Message`.

    Details:
        - Layer: ``181``
        - ID: ``2B085862``

id (``int`` ``32-bit``):
                    N/A
                
        peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        action (:obj:`MessageAction<typegram.api.ayiin.MessageAction>`):
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
                
        legacy (``bool``, *optional*):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        reply_to (:obj:`MessageReplyHeader<typegram.api.ayiin.MessageReplyHeader>`, *optional*):
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

    __slots__: List[str] = ["id", "peer_id", "date", "action", "out", "mentioned", "media_unread", "silent", "post", "legacy", "from_id", "reply_to", "ttl_period"]

    ID = 0x2b085862
    QUALNAME = "functions.types.Message"

    def __init__(self, *, id: int, peer_id: "ayiin.Peer", date: int, action: "ayiin.MessageAction", out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, post: Optional[bool] = None, legacy: Optional[bool] = None, from_id: "ayiin.Peer" = None, reply_to: "ayiin.MessageReplyHeader" = None, ttl_period: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.peer_id = peer_id  # Peer
        
                self.date = date  # int
        
                self.action = action  # MessageAction
        
                self.out = out  # true
        
                self.mentioned = mentioned  # true
        
                self.media_unread = media_unread  # true
        
                self.silent = silent  # true
        
                self.post = post  # true
        
                self.legacy = legacy  # true
        
                self.from_id = from_id  # Peer
        
                self.reply_to = reply_to  # MessageReplyHeader
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageService":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        legacy = True if flags & (1 << 19) else False
        id = Int.read(b)
        
        from_id = Object.read(b) if flags & (1 << 8) else None
        
        peer_id = Object.read(b)
        
        reply_to = Object.read(b) if flags & (1 << 3) else None
        
        date = Int.read(b)
        
        action = Object.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return MessageService(id=id, peer_id=peer_id, date=date, action=action, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, legacy=legacy, from_id=from_id, reply_to=reply_to, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        b.write(self.peer_id.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Int(self.date))
        
        b.write(self.action.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()