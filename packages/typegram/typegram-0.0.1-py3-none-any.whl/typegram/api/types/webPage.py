
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



class WebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebPage`.

    Details:
        - Layer: ``181``
        - ID: ``E89C45B2``

id (``int`` ``64-bit``):
                    N/A
                
        url (``str``):
                    N/A
                
        display_url (``str``):
                    N/A
                
        hash (``int`` ``32-bit``):
                    N/A
                
        has_large_media (``bool``, *optional*):
                    N/A
                
        type (``str``, *optional*):
                    N/A
                
        site_name (``str``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        description (``str``, *optional*):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        embed_url (``str``, *optional*):
                    N/A
                
        embed_type (``str``, *optional*):
                    N/A
                
        embed_width (``int`` ``32-bit``, *optional*):
                    N/A
                
        embed_height (``int`` ``32-bit``, *optional*):
                    N/A
                
        duration (``int`` ``32-bit``, *optional*):
                    N/A
                
        author (``str``, *optional*):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        cached_page (:obj:`Page<typegram.api.ayiin.Page>`, *optional*):
                    N/A
                
        attributes (List of :obj:`WebPageAttribute<typegram.api.ayiin.WebPageAttribute>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

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

    __slots__: List[str] = ["id", "url", "display_url", "hash", "has_large_media", "type", "site_name", "title", "description", "photo", "embed_url", "embed_type", "embed_width", "embed_height", "duration", "author", "document", "cached_page", "attributes"]

    ID = 0xe89c45b2
    QUALNAME = "functions.types.WebPage"

    def __init__(self, *, id: int, url: str, display_url: str, hash: int, has_large_media: Optional[bool] = None, type: Optional[str] = None, site_name: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "ayiin.Photo" = None, embed_url: Optional[str] = None, embed_type: Optional[str] = None, embed_width: Optional[int] = None, embed_height: Optional[int] = None, duration: Optional[int] = None, author: Optional[str] = None, document: "ayiin.Document" = None, cached_page: "ayiin.Page" = None, attributes: Optional[List["ayiin.WebPageAttribute"]] = None) -> None:
        
                self.id = id  # long
        
                self.url = url  # string
        
                self.display_url = display_url  # string
        
                self.hash = hash  # int
        
                self.has_large_media = has_large_media  # true
        
                self.type = type  # string
        
                self.site_name = site_name  # string
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.photo = photo  # Photo
        
                self.embed_url = embed_url  # string
        
                self.embed_type = embed_type  # string
        
                self.embed_width = embed_width  # int
        
                self.embed_height = embed_height  # int
        
                self.duration = duration  # int
        
                self.author = author  # string
        
                self.document = document  # Document
        
                self.cached_page = cached_page  # Page
        
                self.attributes = attributes  # WebPageAttribute

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPage":
        
        flags = Int.read(b)
        
        has_large_media = True if flags & (1 << 13) else False
        id = Long.read(b)
        
        url = String.read(b)
        
        display_url = String.read(b)
        
        hash = Int.read(b)
        
        type = String.read(b) if flags & (1 << 0) else None
        site_name = String.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        photo = Object.read(b) if flags & (1 << 4) else None
        
        embed_url = String.read(b) if flags & (1 << 5) else None
        embed_type = String.read(b) if flags & (1 << 5) else None
        embed_width = Int.read(b) if flags & (1 << 6) else None
        embed_height = Int.read(b) if flags & (1 << 6) else None
        duration = Int.read(b) if flags & (1 << 7) else None
        author = String.read(b) if flags & (1 << 8) else None
        document = Object.read(b) if flags & (1 << 9) else None
        
        cached_page = Object.read(b) if flags & (1 << 10) else None
        
        attributes = Object.read(b) if flags & (1 << 12) else []
        
        return WebPage(id=id, url=url, display_url=display_url, hash=hash, has_large_media=has_large_media, type=type, site_name=site_name, title=title, description=description, photo=photo, embed_url=embed_url, embed_type=embed_type, embed_width=embed_width, embed_height=embed_height, duration=duration, author=author, document=document, cached_page=cached_page, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.url))
        
        b.write(String(self.display_url))
        
        b.write(Int(self.hash))
        
        if self.type is not None:
            b.write(String(self.type))
        
        if self.site_name is not None:
            b.write(String(self.site_name))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.embed_url is not None:
            b.write(String(self.embed_url))
        
        if self.embed_type is not None:
            b.write(String(self.embed_type))
        
        if self.embed_width is not None:
            b.write(Int(self.embed_width))
        
        if self.embed_height is not None:
            b.write(Int(self.embed_height))
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.cached_page is not None:
            b.write(self.cached_page.write())
        
        if self.attributes is not None:
            b.write(Vector(self.attributes))
        
        return b.getvalue()