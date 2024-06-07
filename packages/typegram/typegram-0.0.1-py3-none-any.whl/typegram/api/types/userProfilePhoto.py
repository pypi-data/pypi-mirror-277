
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



class UserProfilePhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.UserProfilePhoto`.

    Details:
        - Layer: ``181``
        - ID: ``82D1F706``

photo_id (``int`` ``64-bit``):
                    N/A
                
        dc_id (``int`` ``32-bit``):
                    N/A
                
        has_video (``bool``, *optional*):
                    N/A
                
        personal (``bool``, *optional*):
                    N/A
                
        stripped_thumb (``bytes``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["photo_id", "dc_id", "has_video", "personal", "stripped_thumb"]

    ID = 0x82d1f706
    QUALNAME = "functions.types.UserProfilePhoto"

    def __init__(self, *, photo_id: int, dc_id: int, has_video: Optional[bool] = None, personal: Optional[bool] = None, stripped_thumb: Optional[bytes] = None) -> None:
        
                self.photo_id = photo_id  # long
        
                self.dc_id = dc_id  # int
        
                self.has_video = has_video  # true
        
                self.personal = personal  # true
        
                self.stripped_thumb = stripped_thumb  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserProfilePhoto":
        
        flags = Int.read(b)
        
        has_video = True if flags & (1 << 0) else False
        personal = True if flags & (1 << 2) else False
        photo_id = Long.read(b)
        
        stripped_thumb = Bytes.read(b) if flags & (1 << 1) else None
        dc_id = Int.read(b)
        
        return UserProfilePhoto(photo_id=photo_id, dc_id=dc_id, has_video=has_video, personal=personal, stripped_thumb=stripped_thumb)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        if self.stripped_thumb is not None:
            b.write(Bytes(self.stripped_thumb))
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()