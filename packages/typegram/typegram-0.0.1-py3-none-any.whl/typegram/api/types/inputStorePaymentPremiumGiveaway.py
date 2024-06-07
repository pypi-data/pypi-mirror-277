
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



class InputStorePaymentPremiumGiveaway(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputStorePaymentPurpose`.

    Details:
        - Layer: ``181``
        - ID: ``160544CA``

boost_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        until_date (``int`` ``32-bit``):
                    N/A
                
        currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        only_new_subscribers (``bool``, *optional*):
                    N/A
                
        winners_are_visible (``bool``, *optional*):
                    N/A
                
        additional_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        countries_iso2 (List of ``str``, *optional*):
                    N/A
                
        prize_description (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

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

    __slots__: List[str] = ["boost_peer", "random_id", "until_date", "currency", "amount", "only_new_subscribers", "winners_are_visible", "additional_peers", "countries_iso2", "prize_description"]

    ID = 0x160544ca
    QUALNAME = "functions.types.InputStorePaymentPurpose"

    def __init__(self, *, boost_peer: "ayiin.InputPeer", random_id: int, until_date: int, currency: str, amount: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, additional_peers: Optional[List["ayiin.InputPeer"]] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None) -> None:
        
                self.boost_peer = boost_peer  # InputPeer
        
                self.random_id = random_id  # long
        
                self.until_date = until_date  # int
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.only_new_subscribers = only_new_subscribers  # true
        
                self.winners_are_visible = winners_are_visible  # true
        
                self.additional_peers = additional_peers  # InputPeer
        
                self.countries_iso2 = countries_iso2  # string
        
                self.prize_description = prize_description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiveaway":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 3) else False
        boost_peer = Object.read(b)
        
        additional_peers = Object.read(b) if flags & (1 << 1) else []
        
        countries_iso2 = Object.read(b, String) if flags & (1 << 2) else []
        
        prize_description = String.read(b) if flags & (1 << 4) else None
        random_id = Long.read(b)
        
        until_date = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentPremiumGiveaway(boost_peer=boost_peer, random_id=random_id, until_date=until_date, currency=currency, amount=amount, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, additional_peers=additional_peers, countries_iso2=countries_iso2, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.boost_peer.write())
        
        if self.additional_peers is not None:
            b.write(Vector(self.additional_peers))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.until_date))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()