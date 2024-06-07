
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



class PageBlockEmbedPost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``F259A80B``

url (``str``):
                    N/A
                
        webpage_id (``int`` ``64-bit``):
                    N/A
                
        author_photo_id (``int`` ``64-bit``):
                    N/A
                
        author (``str``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        blocks (List of :obj:`PageBlock<typegram.api.ayiin.PageBlock>`):
                    N/A
                
        caption (:obj:`PageCaption<typegram.api.ayiin.PageCaption>`):
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

    __slots__: List[str] = ["url", "webpage_id", "author_photo_id", "author", "date", "blocks", "caption"]

    ID = 0xf259a80b
    QUALNAME = "functions.types.PageBlock"

    def __init__(self, *, url: str, webpage_id: int, author_photo_id: int, author: str, date: int, blocks: List["ayiin.PageBlock"], caption: "ayiin.PageCaption") -> None:
        
                self.url = url  # string
        
                self.webpage_id = webpage_id  # long
        
                self.author_photo_id = author_photo_id  # long
        
                self.author = author  # string
        
                self.date = date  # int
        
                self.blocks = blocks  # PageBlock
        
                self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockEmbedPost":
        # No flags
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        author_photo_id = Long.read(b)
        
        author = String.read(b)
        
        date = Int.read(b)
        
        blocks = Object.read(b)
        
        caption = Object.read(b)
        
        return PageBlockEmbedPost(url=url, webpage_id=webpage_id, author_photo_id=author_photo_id, author=author, date=date, blocks=blocks, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        b.write(Long(self.author_photo_id))
        
        b.write(String(self.author))
        
        b.write(Int(self.date))
        
        b.write(Vector(self.blocks))
        
        b.write(self.caption.write())
        
        return b.getvalue()