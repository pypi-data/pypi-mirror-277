
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



class PhoneCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``30535AF5``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        admin_id (``int`` ``64-bit``):
                    N/A
                
        participant_id (``int`` ``64-bit``):
                    N/A
                
        g_a_or_b (``bytes``):
                    N/A
                
        key_fingerprint (``int`` ``64-bit``):
                    N/A
                
        protocol (:obj:`PhoneCallProtocol<typegram.api.ayiin.PhoneCallProtocol>`):
                    N/A
                
        connections (List of :obj:`PhoneConnection<typegram.api.ayiin.PhoneConnection>`):
                    N/A
                
        start_date (``int`` ``32-bit``):
                    N/A
                
        p2p_allowed (``bool``, *optional*):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
        custom_parameters (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

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

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint", "protocol", "connections", "start_date", "p2p_allowed", "video", "custom_parameters"]

    ID = 0x30535af5
    QUALNAME = "functions.types.PhoneCall"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol: "ayiin.PhoneCallProtocol", connections: List["ayiin.PhoneConnection"], start_date: int, p2p_allowed: Optional[bool] = None, video: Optional[bool] = None, custom_parameters: "ayiin.DataJSON" = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.date = date  # int
        
                self.admin_id = admin_id  # long
        
                self.participant_id = participant_id  # long
        
                self.g_a_or_b = g_a_or_b  # bytes
        
                self.key_fingerprint = key_fingerprint  # long
        
                self.protocol = protocol  # PhoneCallProtocol
        
                self.connections = connections  # PhoneConnection
        
                self.start_date = start_date  # int
        
                self.p2p_allowed = p2p_allowed  # true
        
                self.video = video  # true
        
                self.custom_parameters = custom_parameters  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCall":
        
        flags = Int.read(b)
        
        p2p_allowed = True if flags & (1 << 5) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a_or_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = Object.read(b)
        
        connections = Object.read(b)
        
        start_date = Int.read(b)
        
        custom_parameters = Object.read(b) if flags & (1 << 7) else None
        
        return PhoneCall(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections, start_date=start_date, p2p_allowed=p2p_allowed, video=video, custom_parameters=custom_parameters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a_or_b))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        b.write(Vector(self.connections))
        
        b.write(Int(self.start_date))
        
        if self.custom_parameters is not None:
            b.write(self.custom_parameters.write())
        
        return b.getvalue()