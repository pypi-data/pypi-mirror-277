
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



class PhoneConnection(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhoneConnection`.

    Details:
        - Layer: ``181``
        - ID: ``9CC123C7``

id (``int`` ``64-bit``):
                    N/A
                
        ip (``str``):
                    N/A
                
        ipv6 (``str``):
                    N/A
                
        port (``int`` ``32-bit``):
                    N/A
                
        peer_tag (``bytes``):
                    N/A
                
        tcp (``bool``, *optional*):
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

    __slots__: List[str] = ["id", "ip", "ipv6", "port", "peer_tag", "tcp"]

    ID = 0x9cc123c7
    QUALNAME = "functions.types.PhoneConnection"

    def __init__(self, *, id: int, ip: str, ipv6: str, port: int, peer_tag: bytes, tcp: Optional[bool] = None) -> None:
        
                self.id = id  # long
        
                self.ip = ip  # string
        
                self.ipv6 = ipv6  # string
        
                self.port = port  # int
        
                self.peer_tag = peer_tag  # bytes
        
                self.tcp = tcp  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneConnection":
        
        flags = Int.read(b)
        
        tcp = True if flags & (1 << 0) else False
        id = Long.read(b)
        
        ip = String.read(b)
        
        ipv6 = String.read(b)
        
        port = Int.read(b)
        
        peer_tag = Bytes.read(b)
        
        return PhoneConnection(id=id, ip=ip, ipv6=ipv6, port=port, peer_tag=peer_tag, tcp=tcp)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.ip))
        
        b.write(String(self.ipv6))
        
        b.write(Int(self.port))
        
        b.write(Bytes(self.peer_tag))
        
        return b.getvalue()