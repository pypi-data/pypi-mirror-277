
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



class InputMediaInvoice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``405FEF0D``

title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        invoice (:obj:`Invoice<typegram.api.ayiin.Invoice>`):
                    N/A
                
        payload (``bytes``):
                    N/A
                
        provider_data (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        photo (:obj:`InputWebDocument<typegram.api.ayiin.InputWebDocument>`, *optional*):
                    N/A
                
        provider (``str``, *optional*):
                    N/A
                
        start_param (``str``, *optional*):
                    N/A
                
        extended_media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

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

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider_data", "photo", "provider", "start_param", "extended_media"]

    ID = 0x405fef0d
    QUALNAME = "functions.types.InputMedia"

    def __init__(self, *, title: str, description: str, invoice: "ayiin.Invoice", payload: bytes, provider_data: "ayiin.DataJSON", photo: "ayiin.InputWebDocument" = None, provider: Optional[str] = None, start_param: Optional[str] = None, extended_media: "ayiin.InputMedia" = None) -> None:
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.invoice = invoice  # Invoice
        
                self.payload = payload  # bytes
        
                self.provider_data = provider_data  # DataJSON
        
                self.photo = photo  # InputWebDocument
        
                self.provider = provider  # string
        
                self.start_param = start_param  # string
        
                self.extended_media = extended_media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 0) else None
        
        invoice = Object.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b) if flags & (1 << 3) else None
        provider_data = Object.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        extended_media = Object.read(b) if flags & (1 << 2) else None
        
        return InputMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider_data=provider_data, photo=photo, provider=provider, start_param=start_param, extended_media=extended_media)

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
        
        if self.provider is not None:
            b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()