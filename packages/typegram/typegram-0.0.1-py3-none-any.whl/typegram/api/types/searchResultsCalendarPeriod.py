
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



class SearchResultsCalendarPeriod(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SearchResultsCalendarPeriod`.

    Details:
        - Layer: ``181``
        - ID: ``C9B0539F``

date (``int`` ``32-bit``):
                    N/A
                
        min_msg_id (``int`` ``32-bit``):
                    N/A
                
        max_msg_id (``int`` ``32-bit``):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 28 functions.

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

    __slots__: List[str] = ["date", "min_msg_id", "max_msg_id", "count"]

    ID = 0xc9b0539f
    QUALNAME = "functions.types.SearchResultsCalendarPeriod"

    def __init__(self, *, date: int, min_msg_id: int, max_msg_id: int, count: int) -> None:
        
                self.date = date  # int
        
                self.min_msg_id = min_msg_id  # int
        
                self.max_msg_id = max_msg_id  # int
        
                self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsCalendarPeriod":
        # No flags
        
        date = Int.read(b)
        
        min_msg_id = Int.read(b)
        
        max_msg_id = Int.read(b)
        
        count = Int.read(b)
        
        return SearchResultsCalendarPeriod(date=date, min_msg_id=min_msg_id, max_msg_id=max_msg_id, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(Int(self.min_msg_id))
        
        b.write(Int(self.max_msg_id))
        
        b.write(Int(self.count))
        
        return b.getvalue()