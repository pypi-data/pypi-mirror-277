
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



class Dialog(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Dialog`.

    Details:
        - Layer: ``181``
        - ID: ``D58A08C6``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        top_message (``int`` ``32-bit``):
                    N/A
                
        read_inbox_max_id (``int`` ``32-bit``):
                    N/A
                
        read_outbox_max_id (``int`` ``32-bit``):
                    N/A
                
        unread_count (``int`` ``32-bit``):
                    N/A
                
        unread_mentions_count (``int`` ``32-bit``):
                    N/A
                
        unread_reactions_count (``int`` ``32-bit``):
                    N/A
                
        notify_settings (:obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        unread_mark (``bool``, *optional*):
                    N/A
                
        view_forum_as_messages (``bool``, *optional*):
                    N/A
                
        pts (``int`` ``32-bit``, *optional*):
                    N/A
                
        draft (:obj:`DraftMessage<typegram.api.ayiin.DraftMessage>`, *optional*):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 7 functions.

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

    __slots__: List[str] = ["peer", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "notify_settings", "pinned", "unread_mark", "view_forum_as_messages", "pts", "draft", "folder_id", "ttl_period"]

    ID = 0xd58a08c6
    QUALNAME = "functions.types.Dialog"

    def __init__(self, *, peer: "ayiin.Peer", top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, notify_settings: "ayiin.PeerNotifySettings", pinned: Optional[bool] = None, unread_mark: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, pts: Optional[int] = None, draft: "ayiin.DraftMessage" = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.top_message = top_message  # int
        
                self.read_inbox_max_id = read_inbox_max_id  # int
        
                self.read_outbox_max_id = read_outbox_max_id  # int
        
                self.unread_count = unread_count  # int
        
                self.unread_mentions_count = unread_mentions_count  # int
        
                self.unread_reactions_count = unread_reactions_count  # int
        
                self.notify_settings = notify_settings  # PeerNotifySettings
        
                self.pinned = pinned  # true
        
                self.unread_mark = unread_mark  # true
        
                self.view_forum_as_messages = view_forum_as_messages  # true
        
                self.pts = pts  # int
        
                self.draft = draft  # DraftMessage
        
                self.folder_id = folder_id  # int
        
                self.ttl_period = ttl_period  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dialog":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        unread_mark = True if flags & (1 << 3) else False
        view_forum_as_messages = True if flags & (1 << 6) else False
        peer = Object.read(b)
        
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        notify_settings = Object.read(b)
        
        pts = Int.read(b) if flags & (1 << 0) else None
        draft = Object.read(b) if flags & (1 << 1) else None
        
        folder_id = Int.read(b) if flags & (1 << 4) else None
        ttl_period = Int.read(b) if flags & (1 << 5) else None
        return Dialog(peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, notify_settings=notify_settings, pinned=pinned, unread_mark=unread_mark, view_forum_as_messages=view_forum_as_messages, pts=pts, draft=draft, folder_id=folder_id, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(self.notify_settings.write())
        
        if self.pts is not None:
            b.write(Int(self.pts))
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()