
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



class UpdateBotPrecheckoutQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``8CAA9A96``

query_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        payload (``bytes``):
                    N/A
                
        currency (``str``):
                    N/A
                
        total_amount (``int`` ``64-bit``):
                    N/A
                
        info (:obj:`PaymentRequestedInfo<typegram.api.ayiin.PaymentRequestedInfo>`, *optional*):
                    N/A
                
        shipping_option_id (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 7 functions.

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

    __slots__: List[str] = ["query_id", "user_id", "payload", "currency", "total_amount", "info", "shipping_option_id"]

    ID = 0x8caa9a96
    QUALNAME = "functions.types.Update"

    def __init__(self, *, query_id: int, user_id: int, payload: bytes, currency: str, total_amount: int, info: "ayiin.PaymentRequestedInfo" = None, shipping_option_id: Optional[str] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.user_id = user_id  # long
        
                self.payload = payload  # bytes
        
                self.currency = currency  # string
        
                self.total_amount = total_amount  # long
        
                self.info = info  # PaymentRequestedInfo
        
                self.shipping_option_id = shipping_option_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotPrecheckoutQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        payload = Bytes.read(b)
        
        info = Object.read(b) if flags & (1 << 0) else None
        
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        return UpdateBotPrecheckoutQuery(query_id=query_id, user_id=user_id, payload=payload, currency=currency, total_amount=total_amount, info=info, shipping_option_id=shipping_option_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(Bytes(self.payload))
        
        if self.info is not None:
            b.write(self.info.write())
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        return b.getvalue()