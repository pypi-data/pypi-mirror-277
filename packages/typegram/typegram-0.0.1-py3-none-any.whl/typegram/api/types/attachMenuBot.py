
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



class AttachMenuBot(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AttachMenuBot`.

    Details:
        - Layer: ``181``
        - ID: ``D90D8DFE``

bot_id (``int`` ``64-bit``):
                    N/A
                
        short_name (``str``):
                    N/A
                
        icons (List of :obj:`AttachMenuBotIcon<typegram.api.ayiin.AttachMenuBotIcon>`):
                    N/A
                
        inactive (``bool``, *optional*):
                    N/A
                
        has_settings (``bool``, *optional*):
                    N/A
                
        request_write_access (``bool``, *optional*):
                    N/A
                
        show_in_attach_menu (``bool``, *optional*):
                    N/A
                
        show_in_side_menu (``bool``, *optional*):
                    N/A
                
        side_menu_disclaimer_needed (``bool``, *optional*):
                    N/A
                
        peer_types (List of :obj:`AttachMenuPeerType<typegram.api.ayiin.AttachMenuPeerType>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["bot_id", "short_name", "icons", "inactive", "has_settings", "request_write_access", "show_in_attach_menu", "show_in_side_menu", "side_menu_disclaimer_needed", "peer_types"]

    ID = 0xd90d8dfe
    QUALNAME = "functions.types.AttachMenuBot"

    def __init__(self, *, bot_id: int, short_name: str, icons: List["ayiin.AttachMenuBotIcon"], inactive: Optional[bool] = None, has_settings: Optional[bool] = None, request_write_access: Optional[bool] = None, show_in_attach_menu: Optional[bool] = None, show_in_side_menu: Optional[bool] = None, side_menu_disclaimer_needed: Optional[bool] = None, peer_types: Optional[List["ayiin.AttachMenuPeerType"]] = None) -> None:
        
                self.bot_id = bot_id  # long
        
                self.short_name = short_name  # string
        
                self.icons = icons  # AttachMenuBotIcon
        
                self.inactive = inactive  # true
        
                self.has_settings = has_settings  # true
        
                self.request_write_access = request_write_access  # true
        
                self.show_in_attach_menu = show_in_attach_menu  # true
        
                self.show_in_side_menu = show_in_side_menu  # true
        
                self.side_menu_disclaimer_needed = side_menu_disclaimer_needed  # true
        
                self.peer_types = peer_types  # AttachMenuPeerType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBot":
        
        flags = Int.read(b)
        
        inactive = True if flags & (1 << 0) else False
        has_settings = True if flags & (1 << 1) else False
        request_write_access = True if flags & (1 << 2) else False
        show_in_attach_menu = True if flags & (1 << 3) else False
        show_in_side_menu = True if flags & (1 << 4) else False
        side_menu_disclaimer_needed = True if flags & (1 << 5) else False
        bot_id = Long.read(b)
        
        short_name = String.read(b)
        
        peer_types = Object.read(b) if flags & (1 << 3) else []
        
        icons = Object.read(b)
        
        return AttachMenuBot(bot_id=bot_id, short_name=short_name, icons=icons, inactive=inactive, has_settings=has_settings, request_write_access=request_write_access, show_in_attach_menu=show_in_attach_menu, show_in_side_menu=show_in_side_menu, side_menu_disclaimer_needed=side_menu_disclaimer_needed, peer_types=peer_types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.short_name))
        
        if self.peer_types is not None:
            b.write(Vector(self.peer_types))
        
        b.write(Vector(self.icons))
        
        return b.getvalue()