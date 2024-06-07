
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



class PollResults(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PollResults`.

    Details:
        - Layer: ``181``
        - ID: ``7ADF2420``

min (``bool``, *optional*):
                    N/A
                
        results (List of :obj:`PollAnswerVoters<typegram.api.ayiin.PollAnswerVoters>`, *optional*):
                    N/A
                
        total_voters (``int`` ``32-bit``, *optional*):
                    N/A
                
        recent_voters (List of :obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        solution (``str``, *optional*):
                    N/A
                
        solution_entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 12 functions.

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

    __slots__: List[str] = ["min", "results", "total_voters", "recent_voters", "solution", "solution_entities"]

    ID = 0x7adf2420
    QUALNAME = "functions.types.PollResults"

    def __init__(self, *, min: Optional[bool] = None, results: Optional[List["ayiin.PollAnswerVoters"]] = None, total_voters: Optional[int] = None, recent_voters: Optional[List["ayiin.Peer"]] = None, solution: Optional[str] = None, solution_entities: Optional[List["ayiin.MessageEntity"]] = None) -> None:
        
                self.min = min  # true
        
                self.results = results  # PollAnswerVoters
        
                self.total_voters = total_voters  # int
        
                self.recent_voters = recent_voters  # Peer
        
                self.solution = solution  # string
        
                self.solution_entities = solution_entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollResults":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        results = Object.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = Object.read(b) if flags & (1 << 3) else []
        
        solution = String.read(b) if flags & (1 << 4) else None
        solution_entities = Object.read(b) if flags & (1 << 4) else []
        
        return PollResults(min=min, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()