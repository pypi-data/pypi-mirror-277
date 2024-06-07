
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



class GroupCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GroupCall`.

    Details:
        - Layer: ``181``
        - ID: ``D597650C``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        participants_count (``int`` ``32-bit``):
                    N/A
                
        unmuted_video_limit (``int`` ``32-bit``):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
        join_muted (``bool``, *optional*):
                    N/A
                
        can_change_join_muted (``bool``, *optional*):
                    N/A
                
        join_date_asc (``bool``, *optional*):
                    N/A
                
        schedule_start_subscribed (``bool``, *optional*):
                    N/A
                
        can_start_video (``bool``, *optional*):
                    N/A
                
        record_video_active (``bool``, *optional*):
                    N/A
                
        rtmp_stream (``bool``, *optional*):
                    N/A
                
        listeners_hidden (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        stream_dc_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        record_start_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        schedule_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        unmuted_video_count (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

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

    __slots__: List[str] = ["id", "access_hash", "participants_count", "unmuted_video_limit", "version", "join_muted", "can_change_join_muted", "join_date_asc", "schedule_start_subscribed", "can_start_video", "record_video_active", "rtmp_stream", "listeners_hidden", "title", "stream_dc_id", "record_start_date", "schedule_date", "unmuted_video_count"]

    ID = 0xd597650c
    QUALNAME = "functions.types.GroupCall"

    def __init__(self, *, id: int, access_hash: int, participants_count: int, unmuted_video_limit: int, version: int, join_muted: Optional[bool] = None, can_change_join_muted: Optional[bool] = None, join_date_asc: Optional[bool] = None, schedule_start_subscribed: Optional[bool] = None, can_start_video: Optional[bool] = None, record_video_active: Optional[bool] = None, rtmp_stream: Optional[bool] = None, listeners_hidden: Optional[bool] = None, title: Optional[str] = None, stream_dc_id: Optional[int] = None, record_start_date: Optional[int] = None, schedule_date: Optional[int] = None, unmuted_video_count: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.participants_count = participants_count  # int
        
                self.unmuted_video_limit = unmuted_video_limit  # int
        
                self.version = version  # int
        
                self.join_muted = join_muted  # true
        
                self.can_change_join_muted = can_change_join_muted  # true
        
                self.join_date_asc = join_date_asc  # true
        
                self.schedule_start_subscribed = schedule_start_subscribed  # true
        
                self.can_start_video = can_start_video  # true
        
                self.record_video_active = record_video_active  # true
        
                self.rtmp_stream = rtmp_stream  # true
        
                self.listeners_hidden = listeners_hidden  # true
        
                self.title = title  # string
        
                self.stream_dc_id = stream_dc_id  # int
        
                self.record_start_date = record_start_date  # int
        
                self.schedule_date = schedule_date  # int
        
                self.unmuted_video_count = unmuted_video_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCall":
        
        flags = Int.read(b)
        
        join_muted = True if flags & (1 << 1) else False
        can_change_join_muted = True if flags & (1 << 2) else False
        join_date_asc = True if flags & (1 << 6) else False
        schedule_start_subscribed = True if flags & (1 << 8) else False
        can_start_video = True if flags & (1 << 9) else False
        record_video_active = True if flags & (1 << 11) else False
        rtmp_stream = True if flags & (1 << 12) else False
        listeners_hidden = True if flags & (1 << 13) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        participants_count = Int.read(b)
        
        title = String.read(b) if flags & (1 << 3) else None
        stream_dc_id = Int.read(b) if flags & (1 << 4) else None
        record_start_date = Int.read(b) if flags & (1 << 5) else None
        schedule_date = Int.read(b) if flags & (1 << 7) else None
        unmuted_video_count = Int.read(b) if flags & (1 << 10) else None
        unmuted_video_limit = Int.read(b)
        
        version = Int.read(b)
        
        return GroupCall(id=id, access_hash=access_hash, participants_count=participants_count, unmuted_video_limit=unmuted_video_limit, version=version, join_muted=join_muted, can_change_join_muted=can_change_join_muted, join_date_asc=join_date_asc, schedule_start_subscribed=schedule_start_subscribed, can_start_video=can_start_video, record_video_active=record_video_active, rtmp_stream=rtmp_stream, listeners_hidden=listeners_hidden, title=title, stream_dc_id=stream_dc_id, record_start_date=record_start_date, schedule_date=schedule_date, unmuted_video_count=unmuted_video_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.participants_count))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.stream_dc_id is not None:
            b.write(Int(self.stream_dc_id))
        
        if self.record_start_date is not None:
            b.write(Int(self.record_start_date))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.unmuted_video_count is not None:
            b.write(Int(self.unmuted_video_count))
        
        b.write(Int(self.unmuted_video_limit))
        
        b.write(Int(self.version))
        
        return b.getvalue()