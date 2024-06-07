
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



class InputWebFileGeoPointLocation(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputWebFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``9F2221C9``

geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        w (``int`` ``32-bit``):
                    N/A
                
        h (``int`` ``32-bit``):
                    N/A
                
        zoom (``int`` ``32-bit``):
                    N/A
                
        scale (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 21 functions.

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

    __slots__: List[str] = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "functions.types.InputWebFileLocation"

    def __init__(self, *, geo_point: "ayiin.InputGeoPoint", access_hash: int, w: int, h: int, zoom: int, scale: int) -> None:
        
                self.geo_point = geo_point  # InputGeoPoint
        
                self.access_hash = access_hash  # long
        
                self.w = w  # int
        
                self.h = h  # int
        
                self.zoom = zoom  # int
        
                self.scale = scale  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileGeoPointLocation":
        # No flags
        
        geo_point = Object.read(b)
        
        access_hash = Long.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        zoom = Int.read(b)
        
        scale = Int.read(b)
        
        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Int(self.zoom))
        
        b.write(Int(self.scale))
        
        return b.getvalue()