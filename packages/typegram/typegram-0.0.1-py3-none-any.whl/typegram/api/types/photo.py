
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



class Photo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Photo`.

    Details:
        - Layer: ``181``
        - ID: ``FB197A65``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        file_reference (``bytes``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        sizes (List of :obj:`PhotoSize<typegram.api.ayiin.PhotoSize>`):
                    N/A
                
        dc_id (``int`` ``32-bit``):
                    N/A
                
        has_stickers (``bool``, *optional*):
                    N/A
                
        video_sizes (List of :obj:`VideoSize<typegram.api.ayiin.VideoSize>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 6 functions.

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

    __slots__: List[str] = ["id", "access_hash", "file_reference", "date", "sizes", "dc_id", "has_stickers", "video_sizes"]

    ID = 0xfb197a65
    QUALNAME = "functions.types.Photo"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int, sizes: List["ayiin.PhotoSize"], dc_id: int, has_stickers: Optional[bool] = None, video_sizes: Optional[List["ayiin.VideoSize"]] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.file_reference = file_reference  # bytes
        
                self.date = date  # int
        
                self.sizes = sizes  # PhotoSize
        
                self.dc_id = dc_id  # int
        
                self.has_stickers = has_stickers  # true
        
                self.video_sizes = video_sizes  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Photo":
        
        flags = Int.read(b)
        
        has_stickers = True if flags & (1 << 0) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        date = Int.read(b)
        
        sizes = Object.read(b)
        
        video_sizes = Object.read(b) if flags & (1 << 1) else []
        
        dc_id = Int.read(b)
        
        return Photo(id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, dc_id=dc_id, has_stickers=has_stickers, video_sizes=video_sizes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(Int(self.date))
        
        b.write(Vector(self.sizes))
        
        if self.video_sizes is not None:
            b.write(Vector(self.video_sizes))
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()