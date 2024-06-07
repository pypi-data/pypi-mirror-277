
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



class Poll(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Poll`.

    Details:
        - Layer: ``181``
        - ID: ``58747131``

id (``int`` ``64-bit``):
                    N/A
                
        question (:obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`):
                    N/A
                
        answers (List of :obj:`PollAnswer<typegram.api.ayiin.PollAnswer>`):
                    N/A
                
        closed (``bool``, *optional*):
                    N/A
                
        public_voters (``bool``, *optional*):
                    N/A
                
        multiple_choice (``bool``, *optional*):
                    N/A
                
        quiz (``bool``, *optional*):
                    N/A
                
        close_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        close_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 5 functions.

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

    __slots__: List[str] = ["id", "question", "answers", "closed", "public_voters", "multiple_choice", "quiz", "close_period", "close_date"]

    ID = 0x58747131
    QUALNAME = "functions.types.Poll"

    def __init__(self, *, id: int, question: "ayiin.TextWithEntities", answers: List["ayiin.PollAnswer"], closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.question = question  # TextWithEntities
        
                self.answers = answers  # PollAnswer
        
                self.closed = closed  # true
        
                self.public_voters = public_voters  # true
        
                self.multiple_choice = multiple_choice  # true
        
                self.quiz = quiz  # true
        
                self.close_period = close_period  # int
        
                self.close_date = close_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Poll":
        
        id = Long.read(b)
        
        flags = Int.read(b)
        
        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        question = Object.read(b)
        
        answers = Object.read(b)
        
        close_period = Int.read(b) if flags & (1 << 4) else None
        close_date = Int.read(b) if flags & (1 << 5) else None
        return Poll(id=id, question=question, answers=answers, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, close_period=close_period, close_date=close_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.question.write())
        
        b.write(Vector(self.answers))
        
        if self.close_period is not None:
            b.write(Int(self.close_period))
        
        if self.close_date is not None:
            b.write(Int(self.close_date))
        
        return b.getvalue()