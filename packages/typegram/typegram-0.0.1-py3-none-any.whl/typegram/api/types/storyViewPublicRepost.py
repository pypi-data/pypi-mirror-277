
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



class StoryViewPublicRepost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryView`.

    Details:
        - Layer: ``181``
        - ID: ``BD74CF49``

peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        story (:obj:`StoryItem<typegram.api.ayiin.StoryItem>`):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        blocked_my_stories_from (``bool``, *optional*):
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

    __slots__: List[str] = ["peer_id", "story", "blocked", "blocked_my_stories_from"]

    ID = 0xbd74cf49
    QUALNAME = "functions.types.StoryView"

    def __init__(self, *, peer_id: "ayiin.Peer", story: "ayiin.StoryItem", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        
                self.peer_id = peer_id  # Peer
        
                self.story = story  # StoryItem
        
                self.blocked = blocked  # true
        
                self.blocked_my_stories_from = blocked_my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViewPublicRepost":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        peer_id = Object.read(b)
        
        story = Object.read(b)
        
        return StoryViewPublicRepost(peer_id=peer_id, story=story, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        b.write(self.story.write())
        
        return b.getvalue()