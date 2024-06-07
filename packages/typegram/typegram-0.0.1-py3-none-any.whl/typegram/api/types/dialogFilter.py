
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



class DialogFilter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DialogFilter`.

    Details:
        - Layer: ``181``
        - ID: ``5FB5523B``

id (``int`` ``32-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        pinned_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        include_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        exclude_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        contacts (``bool``, *optional*):
                    N/A
                
        non_contacts (``bool``, *optional*):
                    N/A
                
        groups (``bool``, *optional*):
                    N/A
                
        broadcasts (``bool``, *optional*):
                    N/A
                
        bots (``bool``, *optional*):
                    N/A
                
        exclude_muted (``bool``, *optional*):
                    N/A
                
        exclude_read (``bool``, *optional*):
                    N/A
                
        exclude_archived (``bool``, *optional*):
                    N/A
                
        emoticon (``str``, *optional*):
                    N/A
                
        color (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

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

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "exclude_peers", "contacts", "non_contacts", "groups", "broadcasts", "bots", "exclude_muted", "exclude_read", "exclude_archived", "emoticon", "color"]

    ID = 0x5fb5523b
    QUALNAME = "functions.types.DialogFilter"

    def __init__(self, *, id: int, title: str, pinned_peers: List["ayiin.InputPeer"], include_peers: List["ayiin.InputPeer"], exclude_peers: List["ayiin.InputPeer"], contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, groups: Optional[bool] = None, broadcasts: Optional[bool] = None, bots: Optional[bool] = None, exclude_muted: Optional[bool] = None, exclude_read: Optional[bool] = None, exclude_archived: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.title = title  # string
        
                self.pinned_peers = pinned_peers  # InputPeer
        
                self.include_peers = include_peers  # InputPeer
        
                self.exclude_peers = exclude_peers  # InputPeer
        
                self.contacts = contacts  # true
        
                self.non_contacts = non_contacts  # true
        
                self.groups = groups  # true
        
                self.broadcasts = broadcasts  # true
        
                self.bots = bots  # true
        
                self.exclude_muted = exclude_muted  # true
        
                self.exclude_read = exclude_read  # true
        
                self.exclude_archived = exclude_archived  # true
        
                self.emoticon = emoticon  # string
        
                self.color = color  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilter":
        
        flags = Int.read(b)
        
        contacts = True if flags & (1 << 0) else False
        non_contacts = True if flags & (1 << 1) else False
        groups = True if flags & (1 << 2) else False
        broadcasts = True if flags & (1 << 3) else False
        bots = True if flags & (1 << 4) else False
        exclude_muted = True if flags & (1 << 11) else False
        exclude_read = True if flags & (1 << 12) else False
        exclude_archived = True if flags & (1 << 13) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        emoticon = String.read(b) if flags & (1 << 25) else None
        color = Int.read(b) if flags & (1 << 27) else None
        pinned_peers = Object.read(b)
        
        include_peers = Object.read(b)
        
        exclude_peers = Object.read(b)
        
        return DialogFilter(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, exclude_peers=exclude_peers, contacts=contacts, non_contacts=non_contacts, groups=groups, broadcasts=broadcasts, bots=bots, exclude_muted=exclude_muted, exclude_read=exclude_read, exclude_archived=exclude_archived, emoticon=emoticon, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        if self.color is not None:
            b.write(Int(self.color))
        
        b.write(Vector(self.pinned_peers))
        
        b.write(Vector(self.include_peers))
        
        b.write(Vector(self.exclude_peers))
        
        return b.getvalue()