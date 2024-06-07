
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



class ChatAdminRights(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatAdminRights`.

    Details:
        - Layer: ``181``
        - ID: ``5FB224D5``

change_info (``bool``, *optional*):
                    N/A
                
        post_messages (``bool``, *optional*):
                    N/A
                
        edit_messages (``bool``, *optional*):
                    N/A
                
        delete_messages (``bool``, *optional*):
                    N/A
                
        ban_users (``bool``, *optional*):
                    N/A
                
        invite_users (``bool``, *optional*):
                    N/A
                
        pin_messages (``bool``, *optional*):
                    N/A
                
        add_admins (``bool``, *optional*):
                    N/A
                
        anonymous (``bool``, *optional*):
                    N/A
                
        manage_call (``bool``, *optional*):
                    N/A
                
        other (``bool``, *optional*):
                    N/A
                
        manage_topics (``bool``, *optional*):
                    N/A
                
        post_stories (``bool``, *optional*):
                    N/A
                
        edit_stories (``bool``, *optional*):
                    N/A
                
        delete_stories (``bool``, *optional*):
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

    __slots__: List[str] = ["change_info", "post_messages", "edit_messages", "delete_messages", "ban_users", "invite_users", "pin_messages", "add_admins", "anonymous", "manage_call", "other", "manage_topics", "post_stories", "edit_stories", "delete_stories"]

    ID = 0x5fb224d5
    QUALNAME = "functions.types.ChatAdminRights"

    def __init__(self, *, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None, post_stories: Optional[bool] = None, edit_stories: Optional[bool] = None, delete_stories: Optional[bool] = None) -> None:
        
                self.change_info = change_info  # true
        
                self.post_messages = post_messages  # true
        
                self.edit_messages = edit_messages  # true
        
                self.delete_messages = delete_messages  # true
        
                self.ban_users = ban_users  # true
        
                self.invite_users = invite_users  # true
        
                self.pin_messages = pin_messages  # true
        
                self.add_admins = add_admins  # true
        
                self.anonymous = anonymous  # true
        
                self.manage_call = manage_call  # true
        
                self.other = other  # true
        
                self.manage_topics = manage_topics  # true
        
                self.post_stories = post_stories  # true
        
                self.edit_stories = edit_stories  # true
        
                self.delete_stories = delete_stories  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminRights":
        
        flags = Int.read(b)
        
        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        anonymous = True if flags & (1 << 10) else False
        manage_call = True if flags & (1 << 11) else False
        other = True if flags & (1 << 12) else False
        manage_topics = True if flags & (1 << 13) else False
        post_stories = True if flags & (1 << 14) else False
        edit_stories = True if flags & (1 << 15) else False
        delete_stories = True if flags & (1 << 16) else False
        return ChatAdminRights(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages, delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users, pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous, manage_call=manage_call, other=other, manage_topics=manage_topics, post_stories=post_stories, edit_stories=edit_stories, delete_stories=delete_stories)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()