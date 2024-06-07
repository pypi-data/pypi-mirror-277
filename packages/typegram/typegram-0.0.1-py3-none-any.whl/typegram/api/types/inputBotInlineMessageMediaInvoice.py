
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



class InputBotInlineMessageMediaInvoice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``D7E78225``

title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        invoice (:obj:`Invoice<typegram.api.ayiin.Invoice>`):
                    N/A
                
        payload (``bytes``):
                    N/A
                
        provider (``str``):
                    N/A
                
        provider_data (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        photo (:obj:`InputWebDocument<typegram.api.ayiin.InputWebDocument>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

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

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider", "provider_data", "photo", "reply_markup"]

    ID = 0xd7e78225
    QUALNAME = "functions.types.InputBotInlineMessage"

    def __init__(self, *, title: str, description: str, invoice: "ayiin.Invoice", payload: bytes, provider: str, provider_data: "ayiin.DataJSON", photo: "ayiin.InputWebDocument" = None, reply_markup: "ayiin.ReplyMarkup" = None) -> None:
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.invoice = invoice  # Invoice
        
                self.payload = payload  # bytes
        
                self.provider = provider  # string
        
                self.provider_data = provider_data  # DataJSON
        
                self.photo = photo  # InputWebDocument
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 0) else None
        
        invoice = Object.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b)
        
        provider_data = Object.read(b)
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, photo=photo, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()