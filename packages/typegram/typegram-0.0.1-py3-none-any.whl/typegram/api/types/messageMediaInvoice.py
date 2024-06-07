
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



class MessageMediaInvoice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``F6A548D3``

title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        currency (``str``):
                    N/A
                
        total_amount (``int`` ``64-bit``):
                    N/A
                
        start_param (``str``):
                    N/A
                
        shipping_address_requested (``bool``, *optional*):
                    N/A
                
        test (``bool``, *optional*):
                    N/A
                
        photo (:obj:`WebDocument<typegram.api.ayiin.WebDocument>`, *optional*):
                    N/A
                
        receipt_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        extended_media (:obj:`MessageExtendedMedia<typegram.api.ayiin.MessageExtendedMedia>`, *optional*):
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

    __slots__: List[str] = ["title", "description", "currency", "total_amount", "start_param", "shipping_address_requested", "test", "photo", "receipt_msg_id", "extended_media"]

    ID = 0xf6a548d3
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: "ayiin.WebDocument" = None, receipt_msg_id: Optional[int] = None, extended_media: "ayiin.MessageExtendedMedia" = None) -> None:
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.currency = currency  # string
        
                self.total_amount = total_amount  # long
        
                self.start_param = start_param  # string
        
                self.shipping_address_requested = shipping_address_requested  # true
        
                self.test = test  # true
        
                self.photo = photo  # WebDocument
        
                self.receipt_msg_id = receipt_msg_id  # int
        
                self.extended_media = extended_media  # MessageExtendedMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaInvoice":
        
        flags = Int.read(b)
        
        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 0) else None
        
        receipt_msg_id = Int.read(b) if flags & (1 << 2) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        start_param = String.read(b)
        
        extended_media = Object.read(b) if flags & (1 << 4) else None
        
        return MessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, start_param=start_param, shipping_address_requested=shipping_address_requested, test=test, photo=photo, receipt_msg_id=receipt_msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.receipt_msg_id is not None:
            b.write(Int(self.receipt_msg_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()