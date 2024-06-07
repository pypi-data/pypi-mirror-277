
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



class InputBotInlineMessageMediaGeo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``96929A85``

geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`):
                    N/A
                
        heading (``int`` ``32-bit``, *optional*):
                    N/A
                
        period (``int`` ``32-bit``, *optional*):
                    N/A
                
        proximity_notification_radius (``int`` ``32-bit``, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
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

    __slots__: List[str] = ["geo_point", "heading", "period", "proximity_notification_radius", "reply_markup"]

    ID = 0x96929a85
    QUALNAME = "functions.types.InputBotInlineMessage"

    def __init__(self, *, geo_point: "ayiin.InputGeoPoint", heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: "ayiin.ReplyMarkup" = None) -> None:
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.heading = heading  # int
        
                self.period = period  # int
        
                self.proximity_notification_radius = proximity_notification_radius  # int
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaGeo":
        
        flags = Int.read(b)
        
        geo_point = Object.read(b)
        
        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(b) if flags & (1 << 3) else None
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaGeo(geo_point=geo_point, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)

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
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()