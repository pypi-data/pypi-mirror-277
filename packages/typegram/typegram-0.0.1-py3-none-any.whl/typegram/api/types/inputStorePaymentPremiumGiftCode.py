
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



class InputStorePaymentPremiumGiftCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputStorePaymentPurpose`.

    Details:
        - Layer: ``181``
        - ID: ``A3805F3F``

users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        boost_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
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

    __slots__: List[str] = ["users", "currency", "amount", "boost_peer"]

    ID = 0xa3805f3f
    QUALNAME = "functions.types.InputStorePaymentPurpose"

    def __init__(self, *, users: List["ayiin.InputUser"], currency: str, amount: int, boost_peer: "ayiin.InputPeer" = None) -> None:
        
                self.users = users  # InputUser
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.boost_peer = boost_peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiftCode":
        
        flags = Int.read(b)
        
        users = Object.read(b)
        
        boost_peer = Object.read(b) if flags & (1 << 0) else None
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentPremiumGiftCode(users=users, currency=currency, amount=amount, boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.users))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()