
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



class InputMediaGeoLive(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``971FA843``

geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`):
                    N/A
                
        stopped (``bool``, *optional*):
                    N/A
                
        heading (``int`` ``32-bit``, *optional*):
                    N/A
                
        period (``int`` ``32-bit``, *optional*):
                    N/A
                
        proximity_notification_radius (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

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

    __slots__: List[str] = ["geo_point", "stopped", "heading", "period", "proximity_notification_radius"]

    ID = 0x971fa843
    QUALNAME = "functions.types.InputMedia"

    def __init__(self, *, geo_point: "ayiin.InputGeoPoint", stopped: Optional[bool] = None, heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None) -> None:
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.stopped = stopped  # true
        
                self.heading = heading  # int
        
                self.period = period  # int
        
                self.proximity_notification_radius = proximity_notification_radius  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaGeoLive":
        
        flags = Int.read(b)
        
        stopped = True if flags & (1 << 0) else False
        geo_point = Object.read(b)
        
        heading = Int.read(b) if flags & (1 << 2) else None
        period = Int.read(b) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(b) if flags & (1 << 3) else None
        return InputMediaGeoLive(geo_point=geo_point, stopped=stopped, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        if self.heading is not None:
            b.write(Int(self.heading))
        
        if self.period is not None:
            b.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))
        
        return b.getvalue()