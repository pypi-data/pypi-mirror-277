
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



class UpdateReadHistoryInbox(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``9C974FDF``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        max_id (``int`` ``32-bit``):
                    N/A
                
        still_unread_count (``int`` ``32-bit``):
                    N/A
                
        pts (``int`` ``32-bit``):
                    N/A
                
        pts_count (``int`` ``32-bit``):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["peer", "max_id", "still_unread_count", "pts", "pts_count", "folder_id"]

    ID = 0x9c974fdf
    QUALNAME = "functions.types.Update"

    def __init__(self, *, peer: "ayiin.Peer", max_id: int, still_unread_count: int, pts: int, pts_count: int, folder_id: Optional[int] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.max_id = max_id  # int
        
                self.still_unread_count = still_unread_count  # int
        
                self.pts = pts  # int
        
                self.pts_count = pts_count  # int
        
                self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadHistoryInbox":
        
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 0) else None
        peer = Object.read(b)
        
        max_id = Int.read(b)
        
        still_unread_count = Int.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdateReadHistoryInbox(peer=peer, max_id=max_id, still_unread_count=still_unread_count, pts=pts, pts_count=pts_count, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.still_unread_count))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()