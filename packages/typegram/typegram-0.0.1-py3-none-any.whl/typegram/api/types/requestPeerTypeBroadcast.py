
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



class RequestPeerTypeBroadcast(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestPeerType`.

    Details:
        - Layer: ``181``
        - ID: ``339BEF6C``

creator (``bool``, *optional*):
                    N/A
                
        has_username (``bool``, *optional*):
                    N/A
                
        user_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        bot_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["creator", "has_username", "user_admin_rights", "bot_admin_rights"]

    ID = 0x339bef6c
    QUALNAME = "functions.types.RequestPeerType"

    def __init__(self, *, creator: Optional[bool] = None, has_username: Optional[bool] = None, user_admin_rights: "ayiin.ChatAdminRights" = None, bot_admin_rights: "ayiin.ChatAdminRights" = None) -> None:
        
                self.creator = creator  # true
        
                self.has_username = has_username  # Bool
        
                self.user_admin_rights = user_admin_rights  # ChatAdminRights
        
                self.bot_admin_rights = bot_admin_rights  # ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeBroadcast":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        has_username = Bool.read(b) if flags & (1 << 3) else None
        user_admin_rights = Object.read(b) if flags & (1 << 1) else None
        
        bot_admin_rights = Object.read(b) if flags & (1 << 2) else None
        
        return RequestPeerTypeBroadcast(creator=creator, has_username=has_username, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.has_username is not None:
            b.write(Bool(self.has_username))
        
        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())
        
        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())
        
        return b.getvalue()