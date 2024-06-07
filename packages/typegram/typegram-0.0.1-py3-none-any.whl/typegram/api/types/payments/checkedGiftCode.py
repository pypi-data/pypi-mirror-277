
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



class CheckedGiftCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.CheckedGiftCode`.

    Details:
        - Layer: ``181``
        - ID: ``284A1096``

date (``int`` ``32-bit``):
                    N/A
                
        months (``int`` ``32-bit``):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        via_giveaway (``bool``, *optional*):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        giveaway_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        to_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        used_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.PaymentReceipt
            payments.ValidatedRequestedInfo
            payments.PaymentResult
            payments.BankCardData
            payments.ExportedInvoice
            payments.CheckedGiftCode
            payments.GiveawayInfo
            payments.StarsStatus
    """

    __slots__: List[str] = ["date", "months", "chats", "users", "via_giveaway", "from_id", "giveaway_msg_id", "to_id", "used_date"]

    ID = 0x284a1096
    QUALNAME = "functions.typespayments.CheckedGiftCode"

    def __init__(self, *, date: int, months: int, chats: List["ayiin.Chat"], users: List["ayiin.User"], via_giveaway: Optional[bool] = None, from_id: "ayiin.Peer" = None, giveaway_msg_id: Optional[int] = None, to_id: Optional[int] = None, used_date: Optional[int] = None) -> None:
        
                self.date = date  # int
        
                self.months = months  # int
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.via_giveaway = via_giveaway  # true
        
                self.from_id = from_id  # Peer
        
                self.giveaway_msg_id = giveaway_msg_id  # int
        
                self.to_id = to_id  # long
        
                self.used_date = used_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckedGiftCode":
        
        flags = Int.read(b)
        
        via_giveaway = True if flags & (1 << 2) else False
        from_id = Object.read(b) if flags & (1 << 4) else None
        
        giveaway_msg_id = Int.read(b) if flags & (1 << 3) else None
        to_id = Long.read(b) if flags & (1 << 0) else None
        date = Int.read(b)
        
        months = Int.read(b)
        
        used_date = Int.read(b) if flags & (1 << 1) else None
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return CheckedGiftCode(date=date, months=months, chats=chats, users=users, via_giveaway=via_giveaway, from_id=from_id, giveaway_msg_id=giveaway_msg_id, to_id=to_id, used_date=used_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.giveaway_msg_id is not None:
            b.write(Int(self.giveaway_msg_id))
        
        if self.to_id is not None:
            b.write(Long(self.to_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.months))
        
        if self.used_date is not None:
            b.write(Int(self.used_date))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()