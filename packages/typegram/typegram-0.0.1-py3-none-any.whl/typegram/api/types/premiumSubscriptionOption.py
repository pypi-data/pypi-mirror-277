
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



class PremiumSubscriptionOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PremiumSubscriptionOption`.

    Details:
        - Layer: ``181``
        - ID: ``5F2D1DF2``

months (``int`` ``32-bit``):
                    N/A
                
        currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        bot_url (``str``):
                    N/A
                
        current (``bool``, *optional*):
                    N/A
                
        can_purchase_upgrade (``bool``, *optional*):
                    N/A
                
        transaction (``str``, *optional*):
                    N/A
                
        store_product (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 26 functions.

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

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "current", "can_purchase_upgrade", "transaction", "store_product"]

    ID = 0x5f2d1df2
    QUALNAME = "functions.types.PremiumSubscriptionOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None) -> None:
        
                self.months = months  # int
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.bot_url = bot_url  # string
        
                self.current = current  # true
        
                self.can_purchase_upgrade = can_purchase_upgrade  # true
        
                self.transaction = transaction  # string
        
                self.store_product = store_product  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumSubscriptionOption":
        
        flags = Int.read(b)
        
        current = True if flags & (1 << 1) else False
        can_purchase_upgrade = True if flags & (1 << 2) else False
        transaction = String.read(b) if flags & (1 << 3) else None
        months = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        bot_url = String.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumSubscriptionOption(months=months, currency=currency, amount=amount, bot_url=bot_url, current=current, can_purchase_upgrade=can_purchase_upgrade, transaction=transaction, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.transaction is not None:
            b.write(String(self.transaction))
        
        b.write(Int(self.months))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.bot_url))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        return b.getvalue()