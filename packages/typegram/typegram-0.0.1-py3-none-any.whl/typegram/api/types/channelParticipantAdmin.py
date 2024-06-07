
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



class ChannelParticipantAdmin(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``34C3BB53``

user_id (``int`` ``64-bit``):
                    N/A
                
        promoted_by (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`):
                    N/A
                
        can_edit (``bool``, *optional*):
                    N/A
                
        is_self (``bool``, *optional*):
                    N/A
                
        inviter_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        rank (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["user_id", "promoted_by", "date", "admin_rights", "can_edit", "is_self", "inviter_id", "rank"]

    ID = 0x34c3bb53
    QUALNAME = "functions.types.ChannelParticipant"

    def __init__(self, *, user_id: int, promoted_by: int, date: int, admin_rights: "ayiin.ChatAdminRights", can_edit: Optional[bool] = None, is_self: Optional[bool] = None, inviter_id: Optional[int] = None, rank: Optional[str] = None) -> None:
        
                self.user_id = user_id  # long
        
                self.promoted_by = promoted_by  # long
        
                self.date = date  # int
        
                self.admin_rights = admin_rights  # ChatAdminRights
        
                self.can_edit = can_edit  # true
        
                self.is_self = is_self  # true
        
                self.inviter_id = inviter_id  # long
        
                self.rank = rank  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantAdmin":
        
        flags = Int.read(b)
        
        can_edit = True if flags & (1 << 0) else False
        is_self = True if flags & (1 << 1) else False
        user_id = Long.read(b)
        
        inviter_id = Long.read(b) if flags & (1 << 1) else None
        promoted_by = Long.read(b)
        
        date = Int.read(b)
        
        admin_rights = Object.read(b)
        
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantAdmin(user_id=user_id, promoted_by=promoted_by, date=date, admin_rights=admin_rights, can_edit=can_edit, is_self=is_self, inviter_id=inviter_id, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        if self.inviter_id is not None:
            b.write(Long(self.inviter_id))
        
        b.write(Long(self.promoted_by))
        
        b.write(Int(self.date))
        
        b.write(self.admin_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()