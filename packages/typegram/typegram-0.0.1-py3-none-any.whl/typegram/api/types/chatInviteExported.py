
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



class ChatInviteExported(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ExportedChatInvite`.

    Details:
        - Layer: ``181``
        - ID: ``AB4A819``

link (``str``):
                    N/A
                
        admin_id (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        revoked (``bool``, *optional*):
                    N/A
                
        permanent (``bool``, *optional*):
                    N/A
                
        request_needed (``bool``, *optional*):
                    N/A
                
        start_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        expire_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        usage_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        usage (``int`` ``32-bit``, *optional*):
                    N/A
                
        requested (``int`` ``32-bit``, *optional*):
                    N/A
                
        title (``str``, *optional*):
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

    __slots__: List[str] = ["link", "admin_id", "date", "revoked", "permanent", "request_needed", "start_date", "expire_date", "usage_limit", "usage", "requested", "title"]

    ID = 0xab4a819
    QUALNAME = "functions.types.ExportedChatInvite"

    def __init__(self, *, link: str, admin_id: int, date: int, revoked: Optional[bool] = None, permanent: Optional[bool] = None, request_needed: Optional[bool] = None, start_date: Optional[int] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, usage: Optional[int] = None, requested: Optional[int] = None, title: Optional[str] = None) -> None:
        
                self.link = link  # string
        
                self.admin_id = admin_id  # long
        
                self.date = date  # int
        
                self.revoked = revoked  # true
        
                self.permanent = permanent  # true
        
                self.request_needed = request_needed  # true
        
                self.start_date = start_date  # int
        
                self.expire_date = expire_date  # int
        
                self.usage_limit = usage_limit  # int
        
                self.usage = usage  # int
        
                self.requested = requested  # int
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteExported":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 0) else False
        permanent = True if flags & (1 << 5) else False
        request_needed = True if flags & (1 << 6) else False
        link = String.read(b)
        
        admin_id = Long.read(b)
        
        date = Int.read(b)
        
        start_date = Int.read(b) if flags & (1 << 4) else None
        expire_date = Int.read(b) if flags & (1 << 1) else None
        usage_limit = Int.read(b) if flags & (1 << 2) else None
        usage = Int.read(b) if flags & (1 << 3) else None
        requested = Int.read(b) if flags & (1 << 7) else None
        title = String.read(b) if flags & (1 << 8) else None
        return ChatInviteExported(link=link, admin_id=admin_id, date=date, revoked=revoked, permanent=permanent, request_needed=request_needed, start_date=start_date, expire_date=expire_date, usage_limit=usage_limit, usage=usage, requested=requested, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.link))
        
        b.write(Long(self.admin_id))
        
        b.write(Int(self.date))
        
        if self.start_date is not None:
            b.write(Int(self.start_date))
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.usage is not None:
            b.write(Int(self.usage))
        
        if self.requested is not None:
            b.write(Int(self.requested))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()