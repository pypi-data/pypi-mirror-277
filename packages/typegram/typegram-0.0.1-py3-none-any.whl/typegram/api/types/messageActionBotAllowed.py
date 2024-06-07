
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



class MessageActionBotAllowed(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C516D679``

attach_menu (``bool``, *optional*):
                    N/A
                
        from_request (``bool``, *optional*):
                    N/A
                
        domain (``str``, *optional*):
                    N/A
                
        app (:obj:`BotApp<typegram.api.ayiin.BotApp>`, *optional*):
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

    __slots__: List[str] = ["attach_menu", "from_request", "domain", "app"]

    ID = 0xc516d679
    QUALNAME = "functions.types.MessageAction"

    def __init__(self, *, attach_menu: Optional[bool] = None, from_request: Optional[bool] = None, domain: Optional[str] = None, app: "ayiin.BotApp" = None) -> None:
        
                self.attach_menu = attach_menu  # true
        
                self.from_request = from_request  # true
        
                self.domain = domain  # string
        
                self.app = app  # BotApp

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionBotAllowed":
        
        flags = Int.read(b)
        
        attach_menu = True if flags & (1 << 1) else False
        from_request = True if flags & (1 << 3) else False
        domain = String.read(b) if flags & (1 << 0) else None
        app = Object.read(b) if flags & (1 << 2) else None
        
        return MessageActionBotAllowed(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.domain is not None:
            b.write(String(self.domain))
        
        if self.app is not None:
            b.write(self.app.write())
        
        return b.getvalue()