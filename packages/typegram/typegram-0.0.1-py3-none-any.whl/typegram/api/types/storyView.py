
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



class StoryView(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryView`.

    Details:
        - Layer: ``181``
        - ID: ``B0BDEAC5``

user_id (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        blocked_my_stories_from (``bool``, *optional*):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
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

    __slots__: List[str] = ["user_id", "date", "blocked", "blocked_my_stories_from", "reaction"]

    ID = 0xb0bdeac5
    QUALNAME = "functions.types.StoryView"

    def __init__(self, *, user_id: int, date: int, blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, reaction: "ayiin.Reaction" = None) -> None:
        
                self.user_id = user_id  # long
        
                self.date = date  # int
        
                self.blocked = blocked  # true
        
                self.blocked_my_stories_from = blocked_my_stories_from  # true
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryView":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        reaction = Object.read(b) if flags & (1 << 2) else None
        
        return StoryView(user_id=user_id, date=date, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        if self.reaction is not None:
            b.write(self.reaction.write())
        
        return b.getvalue()