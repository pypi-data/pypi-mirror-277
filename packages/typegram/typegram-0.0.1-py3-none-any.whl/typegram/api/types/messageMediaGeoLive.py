
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



class MessageMediaGeoLive(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``B940C666``

geo (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`):
                    N/A
                
        period (``int`` ``32-bit``):
                    N/A
                
        heading (``int`` ``32-bit``, *optional*):
                    N/A
                
        proximity_notification_radius (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["geo", "period", "heading", "proximity_notification_radius"]

    ID = 0xb940c666
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, geo: "ayiin.GeoPoint", period: int, heading: Optional[int] = None, proximity_notification_radius: Optional[int] = None) -> None:
        
                self.geo = geo  # GeoPoint
        
                self.period = period  # int
        
                self.heading = heading  # int
        
                self.proximity_notification_radius = proximity_notification_radius  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGeoLive":
        
        flags = Int.read(b)
        
        geo = Object.read(b)
        
        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b)
        
        proximity_notification_radius = Int.read(b) if flags & (1 << 1) else None
        return MessageMediaGeoLive(geo=geo, period=period, heading=heading, proximity_notification_radius=proximity_notification_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.geo.write())
        
        if self.heading is not None:
            b.write(Int(self.heading))
        
        b.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))
        
        return b.getvalue()