
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



class InputGroupCallStream(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``598A92A``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        time_ms (``int`` ``64-bit``):
                    N/A
                
        scale (``int`` ``32-bit``):
                    N/A
                
        video_channel (``int`` ``32-bit``, *optional*):
                    N/A
                
        video_quality (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["call", "time_ms", "scale", "video_channel", "video_quality"]

    ID = 0x598a92a
    QUALNAME = "functions.types.InputFileLocation"

    def __init__(self, *, call: "ayiin.InputGroupCall", time_ms: int, scale: int, video_channel: Optional[int] = None, video_quality: Optional[int] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.time_ms = time_ms  # long
        
                self.scale = scale  # int
        
                self.video_channel = video_channel  # int
        
                self.video_quality = video_quality  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGroupCallStream":
        
        flags = Int.read(b)
        
        call = Object.read(b)
        
        time_ms = Long.read(b)
        
        scale = Int.read(b)
        
        video_channel = Int.read(b) if flags & (1 << 0) else None
        video_quality = Int.read(b) if flags & (1 << 0) else None
        return InputGroupCallStream(call=call, time_ms=time_ms, scale=scale, video_channel=video_channel, video_quality=video_quality)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(Long(self.time_ms))
        
        b.write(Int(self.scale))
        
        if self.video_channel is not None:
            b.write(Int(self.video_channel))
        
        if self.video_quality is not None:
            b.write(Int(self.video_quality))
        
        return b.getvalue()