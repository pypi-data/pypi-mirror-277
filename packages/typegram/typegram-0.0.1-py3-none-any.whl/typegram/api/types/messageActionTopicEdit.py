
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



class MessageActionTopicEdit(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C0944820``

title (``str``, *optional*):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        closed (``bool``, *optional*):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xc0944820
    QUALNAME = "functions.types.MessageAction"

    def __init__(self, *, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None) -> None:
        
                self.title = title  # string
        
                self.icon_emoji_id = icon_emoji_id  # long
        
                self.closed = closed  # Bool
        
                self.hidden = hidden  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTopicEdit":
        
        flags = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return MessageActionTopicEdit(title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        if self.closed is not None:
            b.write(Bool(self.closed))
        
        if self.hidden is not None:
            b.write(Bool(self.hidden))
        
        return b.getvalue()