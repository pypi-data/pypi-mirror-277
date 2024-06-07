
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



class DraftMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DraftMessage`.

    Details:
        - Layer: ``181``
        - ID: ``3FCCF7EF``

message (``str``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

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

    __slots__: List[str] = ["message", "date", "no_webpage", "invert_media", "reply_to", "entities", "media"]

    ID = 0x3fccf7ef
    QUALNAME = "functions.types.DraftMessage"

    def __init__(self, *, message: str, date: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: "ayiin.InputReplyTo" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, media: "ayiin.InputMedia" = None) -> None:
        
                self.message = message  # string
        
                self.date = date  # int
        
                self.no_webpage = no_webpage  # true
        
                self.invert_media = invert_media  # true
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.entities = entities  # MessageEntity
        
                self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessage":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 6) else False
        reply_to = Object.read(b) if flags & (1 << 4) else None
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        media = Object.read(b) if flags & (1 << 5) else None
        
        date = Int.read(b)
        
        return DraftMessage(message=message, date=date, no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, entities=entities, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.media is not None:
            b.write(self.media.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()