
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



class ForumTopic(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ForumTopic`.

    Details:
        - Layer: ``181``
        - ID: ``71701DA9``

id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        icon_color (``int`` ``32-bit``):
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
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        notify_settings (:obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`):
                    N/A
                
        my (``bool``, *optional*):
                    N/A
                
        closed (``bool``, *optional*):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        short (``bool``, *optional*):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        draft (:obj:`DraftMessage<typegram.api.ayiin.DraftMessage>`, *optional*):
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

    __slots__: List[str] = ["id", "date", "title", "icon_color", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "from_id", "notify_settings", "my", "closed", "pinned", "short", "hidden", "icon_emoji_id", "draft"]

    ID = 0x71701da9
    QUALNAME = "functions.types.ForumTopic"

    def __init__(self, *, id: int, date: int, title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, from_id: "ayiin.Peer", notify_settings: "ayiin.PeerNotifySettings", my: Optional[bool] = None, closed: Optional[bool] = None, pinned: Optional[bool] = None, short: Optional[bool] = None, hidden: Optional[bool] = None, icon_emoji_id: Optional[int] = None, draft: "ayiin.DraftMessage" = None) -> None:
        
                self.id = id  # int
        
                self.date = date  # int
        
                self.title = title  # string
        
                self.icon_color = icon_color  # int
        
                self.top_message = top_message  # int
        
                self.read_inbox_max_id = read_inbox_max_id  # int
        
                self.read_outbox_max_id = read_outbox_max_id  # int
        
                self.unread_count = unread_count  # int
        
                self.unread_mentions_count = unread_mentions_count  # int
        
                self.unread_reactions_count = unread_reactions_count  # int
        
                self.from_id = from_id  # Peer
        
                self.notify_settings = notify_settings  # PeerNotifySettings
        
                self.my = my  # true
        
                self.closed = closed  # true
        
                self.pinned = pinned  # true
        
                self.short = short  # true
        
                self.hidden = hidden  # true
        
                self.icon_emoji_id = icon_emoji_id  # long
        
                self.draft = draft  # DraftMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopic":
        
        flags = Int.read(b)
        
        my = True if flags & (1 << 1) else False
        closed = True if flags & (1 << 2) else False
        pinned = True if flags & (1 << 3) else False
        short = True if flags & (1 << 5) else False
        hidden = True if flags & (1 << 6) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b)
        
        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        from_id = Object.read(b)
        
        notify_settings = Object.read(b)
        
        draft = Object.read(b) if flags & (1 << 4) else None
        
        return ForumTopic(id=id, date=date, title=title, icon_color=icon_color, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, from_id=from_id, notify_settings=notify_settings, my=my, closed=closed, pinned=pinned, short=short, hidden=hidden, icon_emoji_id=icon_emoji_id, draft=draft)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        b.write(String(self.title))
        
        b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(self.from_id.write())
        
        b.write(self.notify_settings.write())
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        return b.getvalue()