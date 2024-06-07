
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



class MessageReactions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageReactions`.

    Details:
        - Layer: ``181``
        - ID: ``4F2B9479``

results (List of :obj:`ReactionCount<typegram.api.ayiin.ReactionCount>`):
                    N/A
                
        min (``bool``, *optional*):
                    N/A
                
        can_see_list (``bool``, *optional*):
                    N/A
                
        reactions_as_tags (``bool``, *optional*):
                    N/A
                
        recent_reactions (List of :obj:`MessagePeerReaction<typegram.api.ayiin.MessagePeerReaction>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["results", "min", "can_see_list", "reactions_as_tags", "recent_reactions"]

    ID = 0x4f2b9479
    QUALNAME = "functions.types.MessageReactions"

    def __init__(self, *, results: List["ayiin.ReactionCount"], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List["ayiin.MessagePeerReaction"]] = None) -> None:
        
                self.results = results  # ReactionCount
        
                self.min = min  # true
        
                self.can_see_list = can_see_list  # true
        
                self.reactions_as_tags = reactions_as_tags  # true
        
                self.recent_reactions = recent_reactions  # MessagePeerReaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactions":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        can_see_list = True if flags & (1 << 2) else False
        reactions_as_tags = True if flags & (1 << 3) else False
        results = Object.read(b)
        
        recent_reactions = Object.read(b) if flags & (1 << 1) else []
        
        return MessageReactions(results=results, min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, recent_reactions=recent_reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.results))
        
        if self.recent_reactions is not None:
            b.write(Vector(self.recent_reactions))
        
        return b.getvalue()