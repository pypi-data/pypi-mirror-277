
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



class WallPaperSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WallPaperSettings`.

    Details:
        - Layer: ``181``
        - ID: ``372EFCD0``

blur (``bool``, *optional*):
                    N/A
                
        motion (``bool``, *optional*):
                    N/A
                
        background_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        second_background_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        third_background_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        fourth_background_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        intensity (``int`` ``32-bit``, *optional*):
                    N/A
                
        rotation (``int`` ``32-bit``, *optional*):
                    N/A
                
        emoticon (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["blur", "motion", "background_color", "second_background_color", "third_background_color", "fourth_background_color", "intensity", "rotation", "emoticon"]

    ID = 0x372efcd0
    QUALNAME = "functions.types.WallPaperSettings"

    def __init__(self, *, blur: Optional[bool] = None, motion: Optional[bool] = None, background_color: Optional[int] = None, second_background_color: Optional[int] = None, third_background_color: Optional[int] = None, fourth_background_color: Optional[int] = None, intensity: Optional[int] = None, rotation: Optional[int] = None, emoticon: Optional[str] = None) -> None:
        
                self.blur = blur  # true
        
                self.motion = motion  # true
        
                self.background_color = background_color  # int
        
                self.second_background_color = second_background_color  # int
        
                self.third_background_color = third_background_color  # int
        
                self.fourth_background_color = fourth_background_color  # int
        
                self.intensity = intensity  # int
        
                self.rotation = rotation  # int
        
                self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaperSettings":
        
        flags = Int.read(b)
        
        blur = True if flags & (1 << 1) else False
        motion = True if flags & (1 << 2) else False
        background_color = Int.read(b) if flags & (1 << 0) else None
        second_background_color = Int.read(b) if flags & (1 << 4) else None
        third_background_color = Int.read(b) if flags & (1 << 5) else None
        fourth_background_color = Int.read(b) if flags & (1 << 6) else None
        intensity = Int.read(b) if flags & (1 << 3) else None
        rotation = Int.read(b) if flags & (1 << 4) else None
        emoticon = String.read(b) if flags & (1 << 7) else None
        return WallPaperSettings(blur=blur, motion=motion, background_color=background_color, second_background_color=second_background_color, third_background_color=third_background_color, fourth_background_color=fourth_background_color, intensity=intensity, rotation=rotation, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.background_color is not None:
            b.write(Int(self.background_color))
        
        if self.second_background_color is not None:
            b.write(Int(self.second_background_color))
        
        if self.third_background_color is not None:
            b.write(Int(self.third_background_color))
        
        if self.fourth_background_color is not None:
            b.write(Int(self.fourth_background_color))
        
        if self.intensity is not None:
            b.write(Int(self.intensity))
        
        if self.rotation is not None:
            b.write(Int(self.rotation))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        return b.getvalue()