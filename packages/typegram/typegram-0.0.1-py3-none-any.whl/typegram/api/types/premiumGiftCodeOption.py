
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



class PremiumGiftCodeOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PremiumGiftCodeOption`.

    Details:
        - Layer: ``181``
        - ID: ``257E962B``

users (``int`` ``32-bit``):
                    N/A
                
        months (``int`` ``32-bit``):
                    N/A
                
        currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        store_product (``str``, *optional*):
                    N/A
                
        store_quantity (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["users", "months", "currency", "amount", "store_product", "store_quantity"]

    ID = 0x257e962b
    QUALNAME = "functions.types.PremiumGiftCodeOption"

    def __init__(self, *, users: int, months: int, currency: str, amount: int, store_product: Optional[str] = None, store_quantity: Optional[int] = None) -> None:
        
                self.users = users  # int
        
                self.months = months  # int
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.store_product = store_product  # string
        
                self.store_quantity = store_quantity  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumGiftCodeOption":
        
        flags = Int.read(b)
        
        users = Int.read(b)
        
        months = Int.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        store_quantity = Int.read(b) if flags & (1 << 1) else None
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return PremiumGiftCodeOption(users=users, months=months, currency=currency, amount=amount, store_product=store_product, store_quantity=store_quantity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.users))
        
        b.write(Int(self.months))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        if self.store_quantity is not None:
            b.write(Int(self.store_quantity))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()