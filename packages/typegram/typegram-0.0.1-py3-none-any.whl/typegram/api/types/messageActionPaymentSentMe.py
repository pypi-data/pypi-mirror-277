
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



class MessageActionPaymentSentMe(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``8F31B327``

currency (``str``):
                    N/A
                
        total_amount (``int`` ``64-bit``):
                    N/A
                
        payload (``bytes``):
                    N/A
                
        charge (:obj:`PaymentCharge<typegram.api.ayiin.PaymentCharge>`):
                    N/A
                
        recurring_init (``bool``, *optional*):
                    N/A
                
        recurring_used (``bool``, *optional*):
                    N/A
                
        info (:obj:`PaymentRequestedInfo<typegram.api.ayiin.PaymentRequestedInfo>`, *optional*):
                    N/A
                
        shipping_option_id (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["currency", "total_amount", "payload", "charge", "recurring_init", "recurring_used", "info", "shipping_option_id"]

    ID = 0x8f31b327
    QUALNAME = "functions.types.MessageAction"

    def __init__(self, *, currency: str, total_amount: int, payload: bytes, charge: "ayiin.PaymentCharge", recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, info: "ayiin.PaymentRequestedInfo" = None, shipping_option_id: Optional[str] = None) -> None:
        
                self.currency = currency  # string
        
                self.total_amount = total_amount  # long
        
                self.payload = payload  # bytes
        
                self.charge = charge  # PaymentCharge
        
                self.recurring_init = recurring_init  # true
        
                self.recurring_used = recurring_used  # true
        
                self.info = info  # PaymentRequestedInfo
        
                self.shipping_option_id = shipping_option_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSentMe":
        
        flags = Int.read(b)
        
        recurring_init = True if flags & (1 << 2) else False
        recurring_used = True if flags & (1 << 3) else False
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        payload = Bytes.read(b)
        
        info = Object.read(b) if flags & (1 << 0) else None
        
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        charge = Object.read(b)
        
        return MessageActionPaymentSentMe(currency=currency, total_amount=total_amount, payload=payload, charge=charge, recurring_init=recurring_init, recurring_used=recurring_used, info=info, shipping_option_id=shipping_option_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(Bytes(self.payload))
        
        if self.info is not None:
            b.write(self.info.write())
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(self.charge.write())
        
        return b.getvalue()