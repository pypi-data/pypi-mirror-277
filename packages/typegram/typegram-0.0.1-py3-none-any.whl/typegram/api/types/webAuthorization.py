
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



class WebAuthorization(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebAuthorization`.

    Details:
        - Layer: ``181``
        - ID: ``A6F8F452``

hash (``int`` ``64-bit``):
                    N/A
                
        bot_id (``int`` ``64-bit``):
                    N/A
                
        domain (``str``):
                    N/A
                
        browser (``str``):
                    N/A
                
        platform (``str``):
                    N/A
                
        date_created (``int`` ``32-bit``):
                    N/A
                
        date_active (``int`` ``32-bit``):
                    N/A
                
        ip (``str``):
                    N/A
                
        region (``str``):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["hash", "bot_id", "domain", "browser", "platform", "date_created", "date_active", "ip", "region"]

    ID = 0xa6f8f452
    QUALNAME = "functions.types.WebAuthorization"

    def __init__(self, *, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: int, date_active: int, ip: str, region: str) -> None:
        
                self.hash = hash  # long
        
                self.bot_id = bot_id  # long
        
                self.domain = domain  # string
        
                self.browser = browser  # string
        
                self.platform = platform  # string
        
                self.date_created = date_created  # int
        
                self.date_active = date_active  # int
        
                self.ip = ip  # string
        
                self.region = region  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorization":
        # No flags
        
        hash = Long.read(b)
        
        bot_id = Long.read(b)
        
        domain = String.read(b)
        
        browser = String.read(b)
        
        platform = String.read(b)
        
        date_created = Int.read(b)
        
        date_active = Int.read(b)
        
        ip = String.read(b)
        
        region = String.read(b)
        
        return WebAuthorization(hash=hash, bot_id=bot_id, domain=domain, browser=browser, platform=platform, date_created=date_created, date_active=date_active, ip=ip, region=region)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.domain))
        
        b.write(String(self.browser))
        
        b.write(String(self.platform))
        
        b.write(Int(self.date_created))
        
        b.write(Int(self.date_active))
        
        b.write(String(self.ip))
        
        b.write(String(self.region))
        
        return b.getvalue()