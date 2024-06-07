
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



class MyBoost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MyBoost`.

    Details:
        - Layer: ``181``
        - ID: ``C448415C``

slot (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        expires (``int`` ``32-bit``):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        cooldown_until_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

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

    __slots__: List[str] = ["slot", "date", "expires", "peer", "cooldown_until_date"]

    ID = 0xc448415c
    QUALNAME = "functions.types.MyBoost"

    def __init__(self, *, slot: int, date: int, expires: int, peer: "ayiin.Peer" = None, cooldown_until_date: Optional[int] = None) -> None:
        
                self.slot = slot  # int
        
                self.date = date  # int
        
                self.expires = expires  # int
        
                self.peer = peer  # Peer
        
                self.cooldown_until_date = cooldown_until_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyBoost":
        
        flags = Int.read(b)
        
        slot = Int.read(b)
        
        peer = Object.read(b) if flags & (1 << 0) else None
        
        date = Int.read(b)
        
        expires = Int.read(b)
        
        cooldown_until_date = Int.read(b) if flags & (1 << 1) else None
        return MyBoost(slot=slot, date=date, expires=expires, peer=peer, cooldown_until_date=cooldown_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.slot))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        if self.cooldown_until_date is not None:
            b.write(Int(self.cooldown_until_date))
        
        return b.getvalue()