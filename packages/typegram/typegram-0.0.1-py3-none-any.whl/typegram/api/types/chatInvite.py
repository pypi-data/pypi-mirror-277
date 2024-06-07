
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



class ChatInvite(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatInvite`.

    Details:
        - Layer: ``181``
        - ID: ``CDE0EC40``

title (``str``):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`):
                    N/A
                
        participants_count (``int`` ``32-bit``):
                    N/A
                
        color (``int`` ``32-bit``):
                    N/A
                
        channel (``bool``, *optional*):
                    N/A
                
        broadcast (``bool``, *optional*):
                    N/A
                
        public (``bool``, *optional*):
                    N/A
                
        megagroup (``bool``, *optional*):
                    N/A
                
        request_needed (``bool``, *optional*):
                    N/A
                
        verified (``bool``, *optional*):
                    N/A
                
        scam (``bool``, *optional*):
                    N/A
                
        fake (``bool``, *optional*):
                    N/A
                
        about (``str``, *optional*):
                    N/A
                
        participants (List of :obj:`User<typegram.api.ayiin.User>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

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

    __slots__: List[str] = ["title", "photo", "participants_count", "color", "channel", "broadcast", "public", "megagroup", "request_needed", "verified", "scam", "fake", "about", "participants"]

    ID = 0xcde0ec40
    QUALNAME = "functions.types.ChatInvite"

    def __init__(self, *, title: str, photo: "ayiin.Photo", participants_count: int, color: int, channel: Optional[bool] = None, broadcast: Optional[bool] = None, public: Optional[bool] = None, megagroup: Optional[bool] = None, request_needed: Optional[bool] = None, verified: Optional[bool] = None, scam: Optional[bool] = None, fake: Optional[bool] = None, about: Optional[str] = None, participants: Optional[List["ayiin.User"]] = None) -> None:
        
                self.title = title  # string
        
                self.photo = photo  # Photo
        
                self.participants_count = participants_count  # int
        
                self.color = color  # int
        
                self.channel = channel  # true
        
                self.broadcast = broadcast  # true
        
                self.public = public  # true
        
                self.megagroup = megagroup  # true
        
                self.request_needed = request_needed  # true
        
                self.verified = verified  # true
        
                self.scam = scam  # true
        
                self.fake = fake  # true
        
                self.about = about  # string
        
                self.participants = participants  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvite":
        
        flags = Int.read(b)
        
        channel = True if flags & (1 << 0) else False
        broadcast = True if flags & (1 << 1) else False
        public = True if flags & (1 << 2) else False
        megagroup = True if flags & (1 << 3) else False
        request_needed = True if flags & (1 << 6) else False
        verified = True if flags & (1 << 7) else False
        scam = True if flags & (1 << 8) else False
        fake = True if flags & (1 << 9) else False
        title = String.read(b)
        
        about = String.read(b) if flags & (1 << 5) else None
        photo = Object.read(b)
        
        participants_count = Int.read(b)
        
        participants = Object.read(b) if flags & (1 << 4) else []
        
        color = Int.read(b)
        
        return ChatInvite(title=title, photo=photo, participants_count=participants_count, color=color, channel=channel, broadcast=broadcast, public=public, megagroup=megagroup, request_needed=request_needed, verified=verified, scam=scam, fake=fake, about=about, participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        if self.participants is not None:
            b.write(Vector(self.participants))
        
        b.write(Int(self.color))
        
        return b.getvalue()