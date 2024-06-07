
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



class AutoDownloadSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AutoDownloadSettings`.

    Details:
        - Layer: ``181``
        - ID: ``BAA57628``

photo_size_max (``int`` ``32-bit``):
                    N/A
                
        video_size_max (``int`` ``64-bit``):
                    N/A
                
        file_size_max (``int`` ``64-bit``):
                    N/A
                
        video_upload_maxbitrate (``int`` ``32-bit``):
                    N/A
                
        small_queue_active_operations_max (``int`` ``32-bit``):
                    N/A
                
        large_queue_active_operations_max (``int`` ``32-bit``):
                    N/A
                
        disabled (``bool``, *optional*):
                    N/A
                
        video_preload_large (``bool``, *optional*):
                    N/A
                
        audio_preload_next (``bool``, *optional*):
                    N/A
                
        phonecalls_less_data (``bool``, *optional*):
                    N/A
                
        stories_preload (``bool``, *optional*):
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

    __slots__: List[str] = ["photo_size_max", "video_size_max", "file_size_max", "video_upload_maxbitrate", "small_queue_active_operations_max", "large_queue_active_operations_max", "disabled", "video_preload_large", "audio_preload_next", "phonecalls_less_data", "stories_preload"]

    ID = 0xbaa57628
    QUALNAME = "functions.types.AutoDownloadSettings"

    def __init__(self, *, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int, small_queue_active_operations_max: int, large_queue_active_operations_max: int, disabled: Optional[bool] = None, video_preload_large: Optional[bool] = None, audio_preload_next: Optional[bool] = None, phonecalls_less_data: Optional[bool] = None, stories_preload: Optional[bool] = None) -> None:
        
                self.photo_size_max = photo_size_max  # int
        
                self.video_size_max = video_size_max  # long
        
                self.file_size_max = file_size_max  # long
        
                self.video_upload_maxbitrate = video_upload_maxbitrate  # int
        
                self.small_queue_active_operations_max = small_queue_active_operations_max  # int
        
                self.large_queue_active_operations_max = large_queue_active_operations_max  # int
        
                self.disabled = disabled  # true
        
                self.video_preload_large = video_preload_large  # true
        
                self.audio_preload_next = audio_preload_next  # true
        
                self.phonecalls_less_data = phonecalls_less_data  # true
        
                self.stories_preload = stories_preload  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoDownloadSettings":
        
        flags = Int.read(b)
        
        disabled = True if flags & (1 << 0) else False
        video_preload_large = True if flags & (1 << 1) else False
        audio_preload_next = True if flags & (1 << 2) else False
        phonecalls_less_data = True if flags & (1 << 3) else False
        stories_preload = True if flags & (1 << 4) else False
        photo_size_max = Int.read(b)
        
        video_size_max = Long.read(b)
        
        file_size_max = Long.read(b)
        
        video_upload_maxbitrate = Int.read(b)
        
        small_queue_active_operations_max = Int.read(b)
        
        large_queue_active_operations_max = Int.read(b)
        
        return AutoDownloadSettings(photo_size_max=photo_size_max, video_size_max=video_size_max, file_size_max=file_size_max, video_upload_maxbitrate=video_upload_maxbitrate, small_queue_active_operations_max=small_queue_active_operations_max, large_queue_active_operations_max=large_queue_active_operations_max, disabled=disabled, video_preload_large=video_preload_large, audio_preload_next=audio_preload_next, phonecalls_less_data=phonecalls_less_data, stories_preload=stories_preload)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.photo_size_max))
        
        b.write(Long(self.video_size_max))
        
        b.write(Long(self.file_size_max))
        
        b.write(Int(self.video_upload_maxbitrate))
        
        b.write(Int(self.small_queue_active_operations_max))
        
        b.write(Int(self.large_queue_active_operations_max))
        
        return b.getvalue()