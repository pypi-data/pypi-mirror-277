
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



class GroupCallParticipant(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GroupCallParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``EBA636FE``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        source (``int`` ``32-bit``):
                    N/A
                
        muted (``bool``, *optional*):
                    N/A
                
        left (``bool``, *optional*):
                    N/A
                
        can_is_self_unmute (``bool``, *optional*):
                    N/A
                
        just_joined (``bool``, *optional*):
                    N/A
                
        versioned (``bool``, *optional*):
                    N/A
                
        min (``bool``, *optional*):
                    N/A
                
        muted_by_you (``bool``, *optional*):
                    N/A
                
        volume_by_admin (``bool``, *optional*):
                    N/A
                
        is_self (``bool``, *optional*):
                    N/A
                
        video_joined (``bool``, *optional*):
                    N/A
                
        active_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        volume (``int`` ``32-bit``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
        raise_hand_rating (``int`` ``64-bit``, *optional*):
                    N/A
                
        video (:obj:`GroupCallParticipantVideo<typegram.api.ayiin.GroupCallParticipantVideo>`, *optional*):
                    N/A
                
        presentation (:obj:`GroupCallParticipantVideo<typegram.api.ayiin.GroupCallParticipantVideo>`, *optional*):
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

    __slots__: List[str] = ["peer", "date", "source", "muted", "left", "can_is_self_unmute", "just_joined", "versioned", "min", "muted_by_you", "volume_by_admin", "is_self", "video_joined", "active_date", "volume", "about", "raise_hand_rating", "video", "presentation"]

    ID = 0xeba636fe
    QUALNAME = "functions.types.GroupCallParticipant"

    def __init__(self, *, peer: "ayiin.Peer", date: int, source: int, muted: Optional[bool] = None, left: Optional[bool] = None, can_is_self_unmute: Optional[bool] = None, just_joined: Optional[bool] = None, versioned: Optional[bool] = None, min: Optional[bool] = None, muted_by_you: Optional[bool] = None, volume_by_admin: Optional[bool] = None, is_self: Optional[bool] = None, video_joined: Optional[bool] = None, active_date: Optional[int] = None, volume: Optional[int] = None, about: Optional[str] = None, raise_hand_rating: Optional[int] = None, video: "ayiin.GroupCallParticipantVideo" = None, presentation: "ayiin.GroupCallParticipantVideo" = None) -> None:
        
                self.peer = peer  # Peer
        
                self.date = date  # int
        
                self.source = source  # int
        
                self.muted = muted  # true
        
                self.left = left  # true
        
                self.can_is_self_unmute = can_is_self_unmute  # true
        
                self.just_joined = just_joined  # true
        
                self.versioned = versioned  # true
        
                self.min = min  # true
        
                self.muted_by_you = muted_by_you  # true
        
                self.volume_by_admin = volume_by_admin  # true
        
                self.is_self = is_self  # true
        
                self.video_joined = video_joined  # true
        
                self.active_date = active_date  # int
        
                self.volume = volume  # int
        
                self.about = about  # string
        
                self.raise_hand_rating = raise_hand_rating  # long
        
                self.video = video  # GroupCallParticipantVideo
        
                self.presentation = presentation  # GroupCallParticipantVideo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipant":
        
        flags = Int.read(b)
        
        muted = True if flags & (1 << 0) else False
        left = True if flags & (1 << 1) else False
        can_is_self_unmute = True if flags & (1 << 2) else False
        just_joined = True if flags & (1 << 4) else False
        versioned = True if flags & (1 << 5) else False
        min = True if flags & (1 << 8) else False
        muted_by_you = True if flags & (1 << 9) else False
        volume_by_admin = True if flags & (1 << 10) else False
        is_self = True if flags & (1 << 12) else False
        video_joined = True if flags & (1 << 15) else False
        peer = Object.read(b)
        
        date = Int.read(b)
        
        active_date = Int.read(b) if flags & (1 << 3) else None
        source = Int.read(b)
        
        volume = Int.read(b) if flags & (1 << 7) else None
        about = String.read(b) if flags & (1 << 11) else None
        raise_hand_rating = Long.read(b) if flags & (1 << 13) else None
        video = Object.read(b) if flags & (1 << 6) else None
        
        presentation = Object.read(b) if flags & (1 << 14) else None
        
        return GroupCallParticipant(peer=peer, date=date, source=source, muted=muted, left=left, can_is_self_unmute=can_is_self_unmute, just_joined=just_joined, versioned=versioned, min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin, is_self=is_self, video_joined=video_joined, active_date=active_date, volume=volume, about=about, raise_hand_rating=raise_hand_rating, video=video, presentation=presentation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.date))
        
        if self.active_date is not None:
            b.write(Int(self.active_date))
        
        b.write(Int(self.source))
        
        if self.volume is not None:
            b.write(Int(self.volume))
        
        if self.about is not None:
            b.write(String(self.about))
        
        if self.raise_hand_rating is not None:
            b.write(Long(self.raise_hand_rating))
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.presentation is not None:
            b.write(self.presentation.write())
        
        return b.getvalue()