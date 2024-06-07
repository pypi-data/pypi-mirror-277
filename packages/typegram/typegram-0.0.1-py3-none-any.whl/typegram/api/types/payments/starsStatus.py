
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



class StarsStatus(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.StarsStatus`.

    Details:
        - Layer: ``181``
        - ID: ``8CF4EE60``

balance (``int`` ``64-bit``):
                    N/A
                
        history (List of :obj:`StarsTransaction<typegram.api.ayiin.StarsTransaction>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

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

    __slots__: List[str] = ["balance", "history", "chats", "users", "next_offset"]

    ID = 0x8cf4ee60
    QUALNAME = "functions.typespayments.StarsStatus"

    def __init__(self, *, balance: int, history: List["ayiin.StarsTransaction"], chats: List["ayiin.Chat"], users: List["ayiin.User"], next_offset: Optional[str] = None) -> None:
        
                self.balance = balance  # long
        
                self.history = history  # StarsTransaction
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.next_offset = next_offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsStatus":
        
        flags = Int.read(b)
        
        balance = Long.read(b)
        
        history = Object.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return StarsStatus(balance=balance, history=history, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.balance))
        
        b.write(Vector(self.history))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()