
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



class DialogFolder(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Dialog`.

    Details:
        - Layer: ``181``
        - ID: ``71BD134C``

folder (:obj:`Folder<typegram.api.ayiin.Folder>`):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        top_message (``int`` ``32-bit``):
                    N/A
                
        unread_muted_peers_count (``int`` ``32-bit``):
                    N/A
                
        unread_unmuted_peers_count (``int`` ``32-bit``):
                    N/A
                
        unread_muted_messages_count (``int`` ``32-bit``):
                    N/A
                
        unread_unmuted_messages_count (``int`` ``32-bit``):
                    N/A
                
        pinned (``bool``, *optional*):
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

    __slots__: List[str] = ["folder", "peer", "top_message", "unread_muted_peers_count", "unread_unmuted_peers_count", "unread_muted_messages_count", "unread_unmuted_messages_count", "pinned"]

    ID = 0x71bd134c
    QUALNAME = "functions.types.Dialog"

    def __init__(self, *, folder: "ayiin.Folder", peer: "ayiin.Peer", top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: Optional[bool] = None) -> None:
        
                self.folder = folder  # Folder
        
                self.peer = peer  # Peer
        
                self.top_message = top_message  # int
        
                self.unread_muted_peers_count = unread_muted_peers_count  # int
        
                self.unread_unmuted_peers_count = unread_unmuted_peers_count  # int
        
                self.unread_muted_messages_count = unread_muted_messages_count  # int
        
                self.unread_unmuted_messages_count = unread_unmuted_messages_count  # int
        
                self.pinned = pinned  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFolder":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        folder = Object.read(b)
        
        peer = Object.read(b)
        
        top_message = Int.read(b)
        
        unread_muted_peers_count = Int.read(b)
        
        unread_unmuted_peers_count = Int.read(b)
        
        unread_muted_messages_count = Int.read(b)
        
        unread_unmuted_messages_count = Int.read(b)
        
        return DialogFolder(folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.folder.write())
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.unread_muted_peers_count))
        
        b.write(Int(self.unread_unmuted_peers_count))
        
        b.write(Int(self.unread_muted_messages_count))
        
        b.write(Int(self.unread_unmuted_messages_count))
        
        return b.getvalue()