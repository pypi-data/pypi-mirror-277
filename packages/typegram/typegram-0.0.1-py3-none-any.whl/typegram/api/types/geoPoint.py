
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



class GeoPoint(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GeoPoint`.

    Details:
        - Layer: ``181``
        - ID: ``B2A2F663``

long (``float`` ``64-bit``):
                    N/A
                
        lat (``float`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        accuracy_radius (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

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

    __slots__: List[str] = ["long", "lat", "access_hash", "accuracy_radius"]

    ID = 0xb2a2f663
    QUALNAME = "functions.types.GeoPoint"

    def __init__(self, *, long: float, lat: float, access_hash: int, accuracy_radius: Optional[int] = None) -> None:
        
                self.long = long  # double
        
                self.lat = lat  # double
        
                self.access_hash = access_hash  # long
        
                self.accuracy_radius = accuracy_radius  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GeoPoint":
        
        flags = Int.read(b)
        
        long = Double.read(b)
        
        lat = Double.read(b)
        
        access_hash = Long.read(b)
        
        accuracy_radius = Int.read(b) if flags & (1 << 0) else None
        return GeoPoint(long=long, lat=lat, access_hash=access_hash, accuracy_radius=accuracy_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Double(self.long))
        
        b.write(Double(self.lat))
        
        b.write(Long(self.access_hash))
        
        if self.accuracy_radius is not None:
            b.write(Int(self.accuracy_radius))
        
        return b.getvalue()