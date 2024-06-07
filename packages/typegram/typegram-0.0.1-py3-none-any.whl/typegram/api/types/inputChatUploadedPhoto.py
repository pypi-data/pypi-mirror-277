
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



class InputChatUploadedPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputChatPhoto`.

    Details:
        - Layer: ``181``
        - ID: ``BDCDAEC0``

file (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video (:obj:`InputFile<typegram.api.ayiin.InputFile>`, *optional*):
                    N/A
                
        video_start_ts (``float`` ``64-bit``, *optional*):
                    N/A
                
        video_emoji_markup (:obj:`VideoSize<typegram.api.ayiin.VideoSize>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0xbdcdaec0
    QUALNAME = "functions.types.InputChatPhoto"

    def __init__(self, *, file: "ayiin.InputFile" = None, video: "ayiin.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "ayiin.VideoSize" = None) -> None:
        
                self.file = file  # InputFile
        
                self.video = video  # InputFile
        
                self.video_start_ts = video_start_ts  # double
        
                self.video_emoji_markup = video_emoji_markup  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChatUploadedPhoto":
        
        flags = Int.read(b)
        
        file = Object.read(b) if flags & (1 << 0) else None
        
        video = Object.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = Object.read(b) if flags & (1 << 3) else None
        
        return InputChatUploadedPhoto(file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()