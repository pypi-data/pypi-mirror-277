
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



class MessageReplies(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageReplies`.

    Details:
        - Layer: ``181``
        - ID: ``83D60FC2``

replies (``int`` ``32-bit``):
                    N/A
                
        replies_pts (``int`` ``32-bit``):
                    N/A
                
        comments (``bool``, *optional*):
                    N/A
                
        recent_repliers (List of :obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        channel_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        max_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        read_max_id (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["replies", "replies_pts", "comments", "recent_repliers", "channel_id", "max_id", "read_max_id"]

    ID = 0x83d60fc2
    QUALNAME = "functions.types.MessageReplies"

    def __init__(self, *, replies: int, replies_pts: int, comments: Optional[bool] = None, recent_repliers: Optional[List["ayiin.Peer"]] = None, channel_id: Optional[int] = None, max_id: Optional[int] = None, read_max_id: Optional[int] = None) -> None:
        
                self.replies = replies  # int
        
                self.replies_pts = replies_pts  # int
        
                self.comments = comments  # true
        
                self.recent_repliers = recent_repliers  # Peer
        
                self.channel_id = channel_id  # long
        
                self.max_id = max_id  # int
        
                self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReplies":
        
        flags = Int.read(b)
        
        comments = True if flags & (1 << 0) else False
        replies = Int.read(b)
        
        replies_pts = Int.read(b)
        
        recent_repliers = Object.read(b) if flags & (1 << 1) else []
        
        channel_id = Long.read(b) if flags & (1 << 0) else None
        max_id = Int.read(b) if flags & (1 << 2) else None
        read_max_id = Int.read(b) if flags & (1 << 3) else None
        return MessageReplies(replies=replies, replies_pts=replies_pts, comments=comments, recent_repliers=recent_repliers, channel_id=channel_id, max_id=max_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.replies))
        
        b.write(Int(self.replies_pts))
        
        if self.recent_repliers is not None:
            b.write(Vector(self.recent_repliers))
        
        if self.channel_id is not None:
            b.write(Long(self.channel_id))
        
        if self.max_id is not None:
            b.write(Int(self.max_id))
        
        if self.read_max_id is not None:
            b.write(Int(self.read_max_id))
        
        return b.getvalue()