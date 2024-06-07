
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



class ChatFull(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatFull`.

    Details:
        - Layer: ``181``
        - ID: ``2633421B``

id (``int`` ``64-bit``):
                    N/A
                
        about (``str``):
                    N/A
                
        participants (:obj:`ChatParticipants<typegram.api.ayiin.ChatParticipants>`):
                    N/A
                
        notify_settings (:obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`):
                    N/A
                
        can_set_username (``bool``, *optional*):
                    N/A
                
        has_scheduled (``bool``, *optional*):
                    N/A
                
        translations_disabled (``bool``, *optional*):
                    N/A
                
        chat_photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        exported_invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`, *optional*):
                    N/A
                
        bot_info (List of :obj:`BotInfo<typegram.api.ayiin.BotInfo>`, *optional*):
                    N/A
                
        pinned_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        folder_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`, *optional*):
                    N/A
                
        ttl_period (``int`` ``32-bit``, *optional*):
                    N/A
                
        groupcall_default_join_as (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        theme_emoticon (``str``, *optional*):
                    N/A
                
        requests_pending (``int`` ``32-bit``, *optional*):
                    N/A
                
        recent_requesters (List of ``int`` ``64-bit``, *optional*):
                    N/A
                
        available_reactions (:obj:`ChatReactions<typegram.api.ayiin.ChatReactions>`, *optional*):
                    N/A
                
        reactions_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

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

    __slots__: List[str] = ["id", "about", "participants", "notify_settings", "can_set_username", "has_scheduled", "translations_disabled", "chat_photo", "exported_invite", "bot_info", "pinned_msg_id", "folder_id", "call", "ttl_period", "groupcall_default_join_as", "theme_emoticon", "requests_pending", "recent_requesters", "available_reactions", "reactions_limit"]

    ID = 0x2633421b
    QUALNAME = "functions.types.ChatFull"

    def __init__(self, *, id: int, about: str, participants: "ayiin.ChatParticipants", notify_settings: "ayiin.PeerNotifySettings", can_set_username: Optional[bool] = None, has_scheduled: Optional[bool] = None, translations_disabled: Optional[bool] = None, chat_photo: "ayiin.Photo" = None, exported_invite: "ayiin.ExportedChatInvite" = None, bot_info: Optional[List["ayiin.BotInfo"]] = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, call: "ayiin.InputGroupCall" = None, ttl_period: Optional[int] = None, groupcall_default_join_as: "ayiin.Peer" = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, available_reactions: "ayiin.ChatReactions" = None, reactions_limit: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.about = about  # string
        
                self.participants = participants  # ChatParticipants
        
                self.notify_settings = notify_settings  # PeerNotifySettings
        
                self.can_set_username = can_set_username  # true
        
                self.has_scheduled = has_scheduled  # true
        
                self.translations_disabled = translations_disabled  # true
        
                self.chat_photo = chat_photo  # Photo
        
                self.exported_invite = exported_invite  # ExportedChatInvite
        
                self.bot_info = bot_info  # BotInfo
        
                self.pinned_msg_id = pinned_msg_id  # int
        
                self.folder_id = folder_id  # int
        
                self.call = call  # InputGroupCall
        
                self.ttl_period = ttl_period  # int
        
                self.groupcall_default_join_as = groupcall_default_join_as  # Peer
        
                self.theme_emoticon = theme_emoticon  # string
        
                self.requests_pending = requests_pending  # int
        
                self.recent_requesters = recent_requesters  # long
        
                self.available_reactions = available_reactions  # ChatReactions
        
                self.reactions_limit = reactions_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatFull":
        
        flags = Int.read(b)
        
        can_set_username = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 8) else False
        translations_disabled = True if flags & (1 << 19) else False
        id = Long.read(b)
        
        about = String.read(b)
        
        participants = Object.read(b)
        
        chat_photo = Object.read(b) if flags & (1 << 2) else None
        
        notify_settings = Object.read(b)
        
        exported_invite = Object.read(b) if flags & (1 << 13) else None
        
        bot_info = Object.read(b) if flags & (1 << 3) else []
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        call = Object.read(b) if flags & (1 << 12) else None
        
        ttl_period = Int.read(b) if flags & (1 << 14) else None
        groupcall_default_join_as = Object.read(b) if flags & (1 << 15) else None
        
        theme_emoticon = String.read(b) if flags & (1 << 16) else None
        requests_pending = Int.read(b) if flags & (1 << 17) else None
        recent_requesters = Object.read(b, Long) if flags & (1 << 17) else []
        
        available_reactions = Object.read(b) if flags & (1 << 18) else None
        
        reactions_limit = Int.read(b) if flags & (1 << 20) else None
        return ChatFull(id=id, about=about, participants=participants, notify_settings=notify_settings, can_set_username=can_set_username, has_scheduled=has_scheduled, translations_disabled=translations_disabled, chat_photo=chat_photo, exported_invite=exported_invite, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id, call=call, ttl_period=ttl_period, groupcall_default_join_as=groupcall_default_join_as, theme_emoticon=theme_emoticon, requests_pending=requests_pending, recent_requesters=recent_requesters, available_reactions=available_reactions, reactions_limit=reactions_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.about))
        
        b.write(self.participants.write())
        
        if self.chat_photo is not None:
            b.write(self.chat_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.exported_invite is not None:
            b.write(self.exported_invite.write())
        
        if self.bot_info is not None:
            b.write(Vector(self.bot_info))
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.call is not None:
            b.write(self.call.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        if self.groupcall_default_join_as is not None:
            b.write(self.groupcall_default_join_as.write())
        
        if self.theme_emoticon is not None:
            b.write(String(self.theme_emoticon))
        
        if self.requests_pending is not None:
            b.write(Int(self.requests_pending))
        
        if self.recent_requesters is not None:
            b.write(Vector(self.recent_requesters, Long))
        
        if self.available_reactions is not None:
            b.write(self.available_reactions.write())
        
        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))
        
        return b.getvalue()