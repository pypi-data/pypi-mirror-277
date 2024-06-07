
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



class UpdateBotShippingQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B5AEFD7D``

query_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        payload (``bytes``):
                    N/A
                
        shipping_address (:obj:`PostAddress<typegram.api.ayiin.PostAddress>`):
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

    __slots__: List[str] = ["query_id", "user_id", "payload", "shipping_address"]

    ID = 0xb5aefd7d
    QUALNAME = "functions.types.Update"

    def __init__(self, *, query_id: int, user_id: int, payload: bytes, shipping_address: "ayiin.PostAddress") -> None:
        
                self.query_id = query_id  # long
        
                self.user_id = user_id  # long
        
                self.payload = payload  # bytes
        
                self.shipping_address = shipping_address  # PostAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotShippingQuery":
        # No flags
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        payload = Bytes.read(b)
        
        shipping_address = Object.read(b)
        
        return UpdateBotShippingQuery(query_id=query_id, user_id=user_id, payload=payload, shipping_address=shipping_address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(Bytes(self.payload))
        
        b.write(self.shipping_address.write())
        
        return b.getvalue()