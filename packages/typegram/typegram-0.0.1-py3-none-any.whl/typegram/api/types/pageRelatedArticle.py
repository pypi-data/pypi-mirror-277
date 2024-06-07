
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



class PageRelatedArticle(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageRelatedArticle`.

    Details:
        - Layer: ``181``
        - ID: ``B390DC08``

url (``str``):
                    N/A
                
        webpage_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
        photo_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        author (``str``, *optional*):
                    N/A
                
        published_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["url", "webpage_id", "title", "description", "photo_id", "author", "published_date"]

    ID = 0xb390dc08
    QUALNAME = "functions.types.PageRelatedArticle"

    def __init__(self, *, url: str, webpage_id: int, title: Optional[str] = None, description: Optional[str] = None, photo_id: Optional[int] = None, author: Optional[str] = None, published_date: Optional[int] = None) -> None:
        
                self.url = url  # string
        
                self.webpage_id = webpage_id  # long
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.photo_id = photo_id  # long
        
                self.author = author  # string
        
                self.published_date = published_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageRelatedArticle":
        
        flags = Int.read(b)
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo_id = Long.read(b) if flags & (1 << 2) else None
        author = String.read(b) if flags & (1 << 3) else None
        published_date = Int.read(b) if flags & (1 << 4) else None
        return PageRelatedArticle(url=url, webpage_id=webpage_id, title=title, description=description, photo_id=photo_id, author=author, published_date=published_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo_id is not None:
            b.write(Long(self.photo_id))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.published_date is not None:
            b.write(Int(self.published_date))
        
        return b.getvalue()