
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



class Boost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Boost`.

    Details:
        - Layer: ``181``
        - ID: ``2A1C8C71``

id (``str``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        expires (``int`` ``32-bit``):
                    N/A
                
        gift (``bool``, *optional*):
                    N/A
                
        giveaway (``bool``, *optional*):
                    N/A
                
        unclaimed (``bool``, *optional*):
                    N/A
                
        user_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        giveaway_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        used_gift_slug (``str``, *optional*):
                    N/A
                
        multiplier (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 6 functions.

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

    __slots__: List[str] = ["id", "date", "expires", "gift", "giveaway", "unclaimed", "user_id", "giveaway_msg_id", "used_gift_slug", "multiplier"]

    ID = 0x2a1c8c71
    QUALNAME = "functions.types.Boost"

    def __init__(self, *, id: str, date: int, expires: int, gift: Optional[bool] = None, giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, user_id: Optional[int] = None, giveaway_msg_id: Optional[int] = None, used_gift_slug: Optional[str] = None, multiplier: Optional[int] = None) -> None:
        
                self.id = id  # string
        
                self.date = date  # int
        
                self.expires = expires  # int
        
                self.gift = gift  # true
        
                self.giveaway = giveaway  # true
        
                self.unclaimed = unclaimed  # true
        
                self.user_id = user_id  # long
        
                self.giveaway_msg_id = giveaway_msg_id  # int
        
                self.used_gift_slug = used_gift_slug  # string
        
                self.multiplier = multiplier  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Boost":
        
        flags = Int.read(b)
        
        gift = True if flags & (1 << 1) else False
        giveaway = True if flags & (1 << 2) else False
        unclaimed = True if flags & (1 << 3) else False
        id = String.read(b)
        
        user_id = Long.read(b) if flags & (1 << 0) else None
        giveaway_msg_id = Int.read(b) if flags & (1 << 2) else None
        date = Int.read(b)
        
        expires = Int.read(b)
        
        used_gift_slug = String.read(b) if flags & (1 << 4) else None
        multiplier = Int.read(b) if flags & (1 << 5) else None
        return Boost(id=id, date=date, expires=expires, gift=gift, giveaway=giveaway, unclaimed=unclaimed, user_id=user_id, giveaway_msg_id=giveaway_msg_id, used_gift_slug=used_gift_slug, multiplier=multiplier)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        if self.user_id is not None:
            b.write(Long(self.user_id))
        
        if self.giveaway_msg_id is not None:
            b.write(Int(self.giveaway_msg_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        if self.used_gift_slug is not None:
            b.write(String(self.used_gift_slug))
        
        if self.multiplier is not None:
            b.write(Int(self.multiplier))
        
        return b.getvalue()