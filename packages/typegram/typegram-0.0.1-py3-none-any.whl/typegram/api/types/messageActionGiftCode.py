
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



class MessageActionGiftCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``678C2E09``

months (``int`` ``32-bit``):
                    N/A
                
        slug (``str``):
                    N/A
                
        via_giveaway (``bool``, *optional*):
                    N/A
                
        unclaimed (``bool``, *optional*):
                    N/A
                
        boost_peer (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        currency (``str``, *optional*):
                    N/A
                
        amount (``int`` ``64-bit``, *optional*):
                    N/A
                
        crypto_currency (``str``, *optional*):
                    N/A
                
        crypto_amount (``int`` ``64-bit``, *optional*):
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

    __slots__: List[str] = ["months", "slug", "via_giveaway", "unclaimed", "boost_peer", "currency", "amount", "crypto_currency", "crypto_amount"]

    ID = 0x678c2e09
    QUALNAME = "functions.types.MessageAction"

    def __init__(self, *, months: int, slug: str, via_giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, boost_peer: "ayiin.Peer" = None, currency: Optional[str] = None, amount: Optional[int] = None, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None) -> None:
        
                self.months = months  # int
        
                self.slug = slug  # string
        
                self.via_giveaway = via_giveaway  # true
        
                self.unclaimed = unclaimed  # true
        
                self.boost_peer = boost_peer  # Peer
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.crypto_currency = crypto_currency  # string
        
                self.crypto_amount = crypto_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftCode":
        
        flags = Int.read(b)
        
        via_giveaway = True if flags & (1 << 0) else False
        unclaimed = True if flags & (1 << 2) else False
        boost_peer = Object.read(b) if flags & (1 << 1) else None
        
        months = Int.read(b)
        
        slug = String.read(b)
        
        currency = String.read(b) if flags & (1 << 2) else None
        amount = Long.read(b) if flags & (1 << 2) else None
        crypto_currency = String.read(b) if flags & (1 << 3) else None
        crypto_amount = Long.read(b) if flags & (1 << 3) else None
        return MessageActionGiftCode(months=months, slug=slug, via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(Int(self.months))
        
        b.write(String(self.slug))
        
        if self.currency is not None:
            b.write(String(self.currency))
        
        if self.amount is not None:
            b.write(Long(self.amount))
        
        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))
        
        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))
        
        return b.getvalue()