
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



class StoryViews(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryViews`.

    Details:
        - Layer: ``181``
        - ID: ``8D595CD6``

views_count (``int`` ``32-bit``):
                    N/A
                
        has_viewers (``bool``, *optional*):
                    N/A
                
        forwards_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        reactions (List of :obj:`ReactionCount<typegram.api.ayiin.ReactionCount>`, *optional*):
                    N/A
                
        reactions_count (``int`` ``32-bit``, *optional*):
                    N/A
                
        recent_viewers (List of ``int`` ``64-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

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

    __slots__: List[str] = ["views_count", "has_viewers", "forwards_count", "reactions", "reactions_count", "recent_viewers"]

    ID = 0x8d595cd6
    QUALNAME = "functions.types.StoryViews"

    def __init__(self, *, views_count: int, has_viewers: Optional[bool] = None, forwards_count: Optional[int] = None, reactions: Optional[List["ayiin.ReactionCount"]] = None, reactions_count: Optional[int] = None, recent_viewers: Optional[List[int]] = None) -> None:
        
                self.views_count = views_count  # int
        
                self.has_viewers = has_viewers  # true
        
                self.forwards_count = forwards_count  # int
        
                self.reactions = reactions  # ReactionCount
        
                self.reactions_count = reactions_count  # int
        
                self.recent_viewers = recent_viewers  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        
        flags = Int.read(b)
        
        has_viewers = True if flags & (1 << 1) else False
        views_count = Int.read(b)
        
        forwards_count = Int.read(b) if flags & (1 << 2) else None
        reactions = Object.read(b) if flags & (1 << 3) else []
        
        reactions_count = Int.read(b) if flags & (1 << 4) else None
        recent_viewers = Object.read(b, Long) if flags & (1 << 0) else []
        
        return StoryViews(views_count=views_count, has_viewers=has_viewers, forwards_count=forwards_count, reactions=reactions, reactions_count=reactions_count, recent_viewers=recent_viewers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.views_count))
        
        if self.forwards_count is not None:
            b.write(Int(self.forwards_count))
        
        if self.reactions is not None:
            b.write(Vector(self.reactions))
        
        if self.reactions_count is not None:
            b.write(Int(self.reactions_count))
        
        if self.recent_viewers is not None:
            b.write(Vector(self.recent_viewers, Long))
        
        return b.getvalue()