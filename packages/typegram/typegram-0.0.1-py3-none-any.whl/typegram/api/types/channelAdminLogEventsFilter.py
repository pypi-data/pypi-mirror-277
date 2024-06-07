
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



class ChannelAdminLogEventsFilter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventsFilter`.

    Details:
        - Layer: ``181``
        - ID: ``EA107AE4``

join (``bool``, *optional*):
                    N/A
                
        leave (``bool``, *optional*):
                    N/A
                
        invite (``bool``, *optional*):
                    N/A
                
        ban (``bool``, *optional*):
                    N/A
                
        unban (``bool``, *optional*):
                    N/A
                
        kick (``bool``, *optional*):
                    N/A
                
        unkick (``bool``, *optional*):
                    N/A
                
        promote (``bool``, *optional*):
                    N/A
                
        demote (``bool``, *optional*):
                    N/A
                
        info (``bool``, *optional*):
                    N/A
                
        settings (``bool``, *optional*):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        edit (``bool``, *optional*):
                    N/A
                
        delete (``bool``, *optional*):
                    N/A
                
        group_call (``bool``, *optional*):
                    N/A
                
        invites (``bool``, *optional*):
                    N/A
                
        send (``bool``, *optional*):
                    N/A
                
        forums (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 28 functions.

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

    __slots__: List[str] = ["join", "leave", "invite", "ban", "unban", "kick", "unkick", "promote", "demote", "info", "settings", "pinned", "edit", "delete", "group_call", "invites", "send", "forums"]

    ID = 0xea107ae4
    QUALNAME = "functions.types.ChannelAdminLogEventsFilter"

    def __init__(self, *, join: Optional[bool] = None, leave: Optional[bool] = None, invite: Optional[bool] = None, ban: Optional[bool] = None, unban: Optional[bool] = None, kick: Optional[bool] = None, unkick: Optional[bool] = None, promote: Optional[bool] = None, demote: Optional[bool] = None, info: Optional[bool] = None, settings: Optional[bool] = None, pinned: Optional[bool] = None, edit: Optional[bool] = None, delete: Optional[bool] = None, group_call: Optional[bool] = None, invites: Optional[bool] = None, send: Optional[bool] = None, forums: Optional[bool] = None) -> None:
        
                self.join = join  # true
        
                self.leave = leave  # true
        
                self.invite = invite  # true
        
                self.ban = ban  # true
        
                self.unban = unban  # true
        
                self.kick = kick  # true
        
                self.unkick = unkick  # true
        
                self.promote = promote  # true
        
                self.demote = demote  # true
        
                self.info = info  # true
        
                self.settings = settings  # true
        
                self.pinned = pinned  # true
        
                self.edit = edit  # true
        
                self.delete = delete  # true
        
                self.group_call = group_call  # true
        
                self.invites = invites  # true
        
                self.send = send  # true
        
                self.forums = forums  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventsFilter":
        
        flags = Int.read(b)
        
        join = True if flags & (1 << 0) else False
        leave = True if flags & (1 << 1) else False
        invite = True if flags & (1 << 2) else False
        ban = True if flags & (1 << 3) else False
        unban = True if flags & (1 << 4) else False
        kick = True if flags & (1 << 5) else False
        unkick = True if flags & (1 << 6) else False
        promote = True if flags & (1 << 7) else False
        demote = True if flags & (1 << 8) else False
        info = True if flags & (1 << 9) else False
        settings = True if flags & (1 << 10) else False
        pinned = True if flags & (1 << 11) else False
        edit = True if flags & (1 << 12) else False
        delete = True if flags & (1 << 13) else False
        group_call = True if flags & (1 << 14) else False
        invites = True if flags & (1 << 15) else False
        send = True if flags & (1 << 16) else False
        forums = True if flags & (1 << 17) else False
        return ChannelAdminLogEventsFilter(join=join, leave=leave, invite=invite, ban=ban, unban=unban, kick=kick, unkick=unkick, promote=promote, demote=demote, info=info, settings=settings, pinned=pinned, edit=edit, delete=delete, group_call=group_call, invites=invites, send=send, forums=forums)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()