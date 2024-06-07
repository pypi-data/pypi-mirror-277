
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



class Invoice(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Invoice`.

    Details:
        - Layer: ``181``
        - ID: ``5DB95A15``

currency (``str``):
                    N/A
                
        prices (List of :obj:`LabeledPrice<typegram.api.ayiin.LabeledPrice>`):
                    N/A
                
        test (``bool``, *optional*):
                    N/A
                
        name_requested (``bool``, *optional*):
                    N/A
                
        phone_requested (``bool``, *optional*):
                    N/A
                
        email_requested (``bool``, *optional*):
                    N/A
                
        shipping_address_requested (``bool``, *optional*):
                    N/A
                
        flexible (``bool``, *optional*):
                    N/A
                
        phone_to_provider (``bool``, *optional*):
                    N/A
                
        email_to_provider (``bool``, *optional*):
                    N/A
                
        recurring (``bool``, *optional*):
                    N/A
                
        max_tip_amount (``int`` ``64-bit``, *optional*):
                    N/A
                
        suggested_tip_amounts (List of ``int`` ``64-bit``, *optional*):
                    N/A
                
        terms_url (``str``, *optional*):
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

    __slots__: List[str] = ["currency", "prices", "test", "name_requested", "phone_requested", "email_requested", "shipping_address_requested", "flexible", "phone_to_provider", "email_to_provider", "recurring", "max_tip_amount", "suggested_tip_amounts", "terms_url"]

    ID = 0x5db95a15
    QUALNAME = "functions.types.Invoice"

    def __init__(self, *, currency: str, prices: List["ayiin.LabeledPrice"], test: Optional[bool] = None, name_requested: Optional[bool] = None, phone_requested: Optional[bool] = None, email_requested: Optional[bool] = None, shipping_address_requested: Optional[bool] = None, flexible: Optional[bool] = None, phone_to_provider: Optional[bool] = None, email_to_provider: Optional[bool] = None, recurring: Optional[bool] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, terms_url: Optional[str] = None) -> None:
        
                self.currency = currency  # string
        
                self.prices = prices  # LabeledPrice
        
                self.test = test  # true
        
                self.name_requested = name_requested  # true
        
                self.phone_requested = phone_requested  # true
        
                self.email_requested = email_requested  # true
        
                self.shipping_address_requested = shipping_address_requested  # true
        
                self.flexible = flexible  # true
        
                self.phone_to_provider = phone_to_provider  # true
        
                self.email_to_provider = email_to_provider  # true
        
                self.recurring = recurring  # true
        
                self.max_tip_amount = max_tip_amount  # long
        
                self.suggested_tip_amounts = suggested_tip_amounts  # long
        
                self.terms_url = terms_url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Invoice":
        
        flags = Int.read(b)
        
        test = True if flags & (1 << 0) else False
        name_requested = True if flags & (1 << 1) else False
        phone_requested = True if flags & (1 << 2) else False
        email_requested = True if flags & (1 << 3) else False
        shipping_address_requested = True if flags & (1 << 4) else False
        flexible = True if flags & (1 << 5) else False
        phone_to_provider = True if flags & (1 << 6) else False
        email_to_provider = True if flags & (1 << 7) else False
        recurring = True if flags & (1 << 9) else False
        currency = String.read(b)
        
        prices = Object.read(b)
        
        max_tip_amount = Long.read(b) if flags & (1 << 8) else None
        suggested_tip_amounts = Object.read(b, Long) if flags & (1 << 8) else []
        
        terms_url = String.read(b) if flags & (1 << 10) else None
        return Invoice(currency=currency, prices=prices, test=test, name_requested=name_requested, phone_requested=phone_requested, email_requested=email_requested, shipping_address_requested=shipping_address_requested, flexible=flexible, phone_to_provider=phone_to_provider, email_to_provider=email_to_provider, recurring=recurring, max_tip_amount=max_tip_amount, suggested_tip_amounts=suggested_tip_amounts, terms_url=terms_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Vector(self.prices))
        
        if self.max_tip_amount is not None:
            b.write(Long(self.max_tip_amount))
        
        if self.suggested_tip_amounts is not None:
            b.write(Vector(self.suggested_tip_amounts, Long))
        
        if self.terms_url is not None:
            b.write(String(self.terms_url))
        
        return b.getvalue()