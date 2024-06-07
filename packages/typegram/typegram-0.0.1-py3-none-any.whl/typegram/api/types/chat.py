
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



class Chat(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Chat`.

    Details:
        - Layer: ``181``
        - ID: ``41CBF256``

id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        photo (:obj:`ChatPhoto<typegram.api.ayiin.ChatPhoto>`):
                    N/A
                
        participants_count (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        version (``int`` ``32-bit``):
                    N/A
                
        creator (``bool``, *optional*):
                    N/A
                
        left (``bool``, *optional*):
                    N/A
                
        deactivated (``bool``, *optional*):
                    N/A
                
        call_active (``bool``, *optional*):
                    N/A
                
        call_not_empty (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        migrated_to (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`, *optional*):
                    N/A
                
        admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        default_banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 5 functions.

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

    __slots__: List[str] = ["id", "title", "photo", "participants_count", "date", "version", "creator", "left", "deactivated", "call_active", "call_not_empty", "noforwards", "migrated_to", "admin_rights", "default_banned_rights"]

    ID = 0x41cbf256
    QUALNAME = "functions.types.Chat"

    def __init__(self, *, id: int, title: str, photo: "ayiin.ChatPhoto", participants_count: int, date: int, version: int, creator: Optional[bool] = None, left: Optional[bool] = None, deactivated: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, noforwards: Optional[bool] = None, migrated_to: "ayiin.InputChannel" = None, admin_rights: "ayiin.ChatAdminRights" = None, default_banned_rights: "ayiin.ChatBannedRights" = None) -> None:
        
                self.id = id  # long
        
                self.title = title  # string
        
                self.photo = photo  # ChatPhoto
        
                self.participants_count = participants_count  # int
        
                self.date = date  # int
        
                self.version = version  # int
        
                self.creator = creator  # true
        
                self.left = left  # true
        
                self.deactivated = deactivated  # true
        
                self.call_active = call_active  # true
        
                self.call_not_empty = call_not_empty  # true
        
                self.noforwards = noforwards  # true
        
                self.migrated_to = migrated_to  # InputChannel
        
                self.admin_rights = admin_rights  # ChatAdminRights
        
                self.default_banned_rights = default_banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Chat":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        deactivated = True if flags & (1 << 5) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        noforwards = True if flags & (1 << 25) else False
        id = Long.read(b)
        
        title = String.read(b)
        
        photo = Object.read(b)
        
        participants_count = Int.read(b)
        
        date = Int.read(b)
        
        version = Int.read(b)
        
        migrated_to = Object.read(b) if flags & (1 << 6) else None
        
        admin_rights = Object.read(b) if flags & (1 << 14) else None
        
        default_banned_rights = Object.read(b) if flags & (1 << 18) else None
        
        return Chat(id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version, creator=creator, left=left, deactivated=deactivated, call_active=call_active, call_not_empty=call_not_empty, noforwards=noforwards, migrated_to=migrated_to, admin_rights=admin_rights, default_banned_rights=default_banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        b.write(Int(self.date))
        
        b.write(Int(self.version))
        
        if self.migrated_to is not None:
            b.write(self.migrated_to.write())
        
        if self.admin_rights is not None:
            b.write(self.admin_rights.write())
        
        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())
        
        return b.getvalue()