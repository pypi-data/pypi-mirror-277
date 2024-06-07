
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



class DcOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DcOption`.

    Details:
        - Layer: ``181``
        - ID: ``18B7A10D``

id (``int`` ``32-bit``):
                    N/A
                
        ip_address (``str``):
                    N/A
                
        port (``int`` ``32-bit``):
                    N/A
                
        ipv6 (``bool``, *optional*):
                    N/A
                
        media_only (``bool``, *optional*):
                    N/A
                
        tcpo_only (``bool``, *optional*):
                    N/A
                
        cdn (``bool``, *optional*):
                    N/A
                
        static (``bool``, *optional*):
                    N/A
                
        this_port_only (``bool``, *optional*):
                    N/A
                
        secret (``bytes``, *optional*):
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

    __slots__: List[str] = ["id", "ip_address", "port", "ipv6", "media_only", "tcpo_only", "cdn", "static", "this_port_only", "secret"]

    ID = 0x18b7a10d
    QUALNAME = "functions.types.DcOption"

    def __init__(self, *, id: int, ip_address: str, port: int, ipv6: Optional[bool] = None, media_only: Optional[bool] = None, tcpo_only: Optional[bool] = None, cdn: Optional[bool] = None, static: Optional[bool] = None, this_port_only: Optional[bool] = None, secret: Optional[bytes] = None) -> None:
        
                self.id = id  # int
        
                self.ip_address = ip_address  # string
        
                self.port = port  # int
        
                self.ipv6 = ipv6  # true
        
                self.media_only = media_only  # true
        
                self.tcpo_only = tcpo_only  # true
        
                self.cdn = cdn  # true
        
                self.static = static  # true
        
                self.this_port_only = this_port_only  # true
        
                self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DcOption":
        
        flags = Int.read(b)
        
        ipv6 = True if flags & (1 << 0) else False
        media_only = True if flags & (1 << 1) else False
        tcpo_only = True if flags & (1 << 2) else False
        cdn = True if flags & (1 << 3) else False
        static = True if flags & (1 << 4) else False
        this_port_only = True if flags & (1 << 5) else False
        id = Int.read(b)
        
        ip_address = String.read(b)
        
        port = Int.read(b)
        
        secret = Bytes.read(b) if flags & (1 << 10) else None
        return DcOption(id=id, ip_address=ip_address, port=port, ipv6=ipv6, media_only=media_only, tcpo_only=tcpo_only, cdn=cdn, static=static, this_port_only=this_port_only, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.ip_address))
        
        b.write(Int(self.port))
        
        if self.secret is not None:
            b.write(Bytes(self.secret))
        
        return b.getvalue()