
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



class BotInlineMediaResult(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotInlineResult`.

    Details:
        - Layer: ``181``
        - ID: ``17DB940B``

id (``str``):
                    N/A
                
        type (``str``):
                    N/A
                
        send_message (:obj:`BotInlineMessage<typegram.api.ayiin.BotInlineMessage>`):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["id", "type", "send_message", "photo", "document", "title", "description"]

    ID = 0x17db940b
    QUALNAME = "functions.types.BotInlineResult"

    def __init__(self, *, id: str, type: str, send_message: "ayiin.BotInlineMessage", photo: "ayiin.Photo" = None, document: "ayiin.Document" = None, title: Optional[str] = None, description: Optional[str] = None) -> None:
        
                self.id = id  # string
        
                self.type = type  # string
        
                self.send_message = send_message  # BotInlineMessage
        
                self.photo = photo  # Photo
        
                self.document = document  # Document
        
                self.title = title  # string
        
                self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMediaResult":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 0) else None
        
        document = Object.read(b) if flags & (1 << 1) else None
        
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        send_message = Object.read(b)
        
        return BotInlineMediaResult(id=id, type=type, send_message=send_message, photo=photo, document=document, title=title, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        b.write(self.send_message.write())
        
        return b.getvalue()