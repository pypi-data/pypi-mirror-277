
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



class EncryptedChatRequested(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EncryptedChat`.

    Details:
        - Layer: ``181``
        - ID: ``48F1D94C``

id (``int`` ``32-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        admin_id (``int`` ``64-bit``):
                    N/A
                
        participant_id (``int`` ``64-bit``):
                    N/A
                
        g_a (``bytes``):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a", "folder_id"]

    ID = 0x48f1d94c
    QUALNAME = "functions.types.EncryptedChat"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a: bytes, folder_id: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.access_hash = access_hash  # long
        
                self.date = date  # int
        
                self.admin_id = admin_id  # long
        
                self.participant_id = participant_id  # long
        
                self.g_a = g_a  # bytes
        
                self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChatRequested":
        
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 0) else None
        id = Int.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a = Bytes.read(b)
        
        return EncryptedChatRequested(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a=g_a, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(Int(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()