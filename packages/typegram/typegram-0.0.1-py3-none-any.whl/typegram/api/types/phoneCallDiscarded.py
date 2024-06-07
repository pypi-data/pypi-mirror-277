
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



class PhoneCallDiscarded(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``50CA4DE1``

id (``int`` ``64-bit``):
                    N/A
                
        need_rating (``bool``, *optional*):
                    N/A
                
        need_debug (``bool``, *optional*):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
        reason (:obj:`PhoneCallDiscardReason<typegram.api.ayiin.PhoneCallDiscardReason>`, *optional*):
                    N/A
                
        duration (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

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

    __slots__: List[str] = ["id", "need_rating", "need_debug", "video", "reason", "duration"]

    ID = 0x50ca4de1
    QUALNAME = "functions.types.PhoneCall"

    def __init__(self, *, id: int, need_rating: Optional[bool] = None, need_debug: Optional[bool] = None, video: Optional[bool] = None, reason: "ayiin.PhoneCallDiscardReason" = None, duration: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.need_rating = need_rating  # true
        
                self.need_debug = need_debug  # true
        
                self.video = video  # true
        
                self.reason = reason  # PhoneCallDiscardReason
        
                self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallDiscarded":
        
        flags = Int.read(b)
        
        need_rating = True if flags & (1 << 2) else False
        need_debug = True if flags & (1 << 3) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        reason = Object.read(b) if flags & (1 << 0) else None
        
        duration = Int.read(b) if flags & (1 << 1) else None
        return PhoneCallDiscarded(id=id, need_rating=need_rating, need_debug=need_debug, video=video, reason=reason, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.reason is not None:
            b.write(self.reason.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()