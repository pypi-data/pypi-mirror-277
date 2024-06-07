
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



class InputBusinessRecipients(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBusinessRecipients`.

    Details:
        - Layer: ``181``
        - ID: ``6F8B32AA``

existing_chats (``bool``, *optional*):
                    N/A
                
        new_chats (``bool``, *optional*):
                    N/A
                
        contacts (``bool``, *optional*):
                    N/A
                
        non_contacts (``bool``, *optional*):
                    N/A
                
        exclude_selected (``bool``, *optional*):
                    N/A
                
        users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

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

    __slots__: List[str] = ["existing_chats", "new_chats", "contacts", "non_contacts", "exclude_selected", "users"]

    ID = 0x6f8b32aa
    QUALNAME = "functions.types.InputBusinessRecipients"

    def __init__(self, *, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List["ayiin.InputUser"]] = None) -> None:
        
                self.existing_chats = existing_chats  # true
        
                self.new_chats = new_chats  # true
        
                self.contacts = contacts  # true
        
                self.non_contacts = non_contacts  # true
        
                self.exclude_selected = exclude_selected  # true
        
                self.users = users  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessRecipients":
        
        flags = Int.read(b)
        
        existing_chats = True if flags & (1 << 0) else False
        new_chats = True if flags & (1 << 1) else False
        contacts = True if flags & (1 << 2) else False
        non_contacts = True if flags & (1 << 3) else False
        exclude_selected = True if flags & (1 << 5) else False
        users = Object.read(b) if flags & (1 << 4) else []
        
        return InputBusinessRecipients(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.users is not None:
            b.write(Vector(self.users))
        
        return b.getvalue()