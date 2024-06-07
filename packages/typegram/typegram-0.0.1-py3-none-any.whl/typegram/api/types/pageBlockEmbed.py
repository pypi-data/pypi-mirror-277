
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



class PageBlockEmbed(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``A8718DC5``

caption (:obj:`PageCaption<typegram.api.ayiin.PageCaption>`):
                    N/A
                
        full_width (``bool``, *optional*):
                    N/A
                
        allow_scrolling (``bool``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        html (``str``, *optional*):
                    N/A
                
        poster_photo_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        w (``int`` ``32-bit``, *optional*):
                    N/A
                
        h (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["caption", "full_width", "allow_scrolling", "url", "html", "poster_photo_id", "w", "h"]

    ID = 0xa8718dc5
    QUALNAME = "functions.types.PageBlock"

    def __init__(self, *, caption: "ayiin.PageCaption", full_width: Optional[bool] = None, allow_scrolling: Optional[bool] = None, url: Optional[str] = None, html: Optional[str] = None, poster_photo_id: Optional[int] = None, w: Optional[int] = None, h: Optional[int] = None) -> None:
        
                self.caption = caption  # PageCaption
        
                self.full_width = full_width  # true
        
                self.allow_scrolling = allow_scrolling  # true
        
                self.url = url  # string
        
                self.html = html  # string
        
                self.poster_photo_id = poster_photo_id  # long
        
                self.w = w  # int
        
                self.h = h  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockEmbed":
        
        flags = Int.read(b)
        
        full_width = True if flags & (1 << 0) else False
        allow_scrolling = True if flags & (1 << 3) else False
        url = String.read(b) if flags & (1 << 1) else None
        html = String.read(b) if flags & (1 << 2) else None
        poster_photo_id = Long.read(b) if flags & (1 << 4) else None
        w = Int.read(b) if flags & (1 << 5) else None
        h = Int.read(b) if flags & (1 << 5) else None
        caption = Object.read(b)
        
        return PageBlockEmbed(caption=caption, full_width=full_width, allow_scrolling=allow_scrolling, url=url, html=html, poster_photo_id=poster_photo_id, w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.html is not None:
            b.write(String(self.html))
        
        if self.poster_photo_id is not None:
            b.write(Long(self.poster_photo_id))
        
        if self.w is not None:
            b.write(Int(self.w))
        
        if self.h is not None:
            b.write(Int(self.h))
        
        b.write(self.caption.write())
        
        return b.getvalue()