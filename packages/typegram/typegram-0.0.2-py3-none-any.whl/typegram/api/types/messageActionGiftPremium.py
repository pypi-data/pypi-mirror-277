
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class MessageActionGiftPremium(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C83D6AEC``

currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        months (``int`` ``32-bit``):
                    N/A
                
        crypto_currency (``str``, *optional*):
                    N/A
                
        crypto_amount (``int`` ``64-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["currency", "amount", "months", "crypto_currency", "crypto_amount"]

    ID = 0xc83d6aec
    QUALNAME = "types.messageActionGiftPremium"

    def __init__(self, *, currency: str, amount: int, months: int, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None) -> None:
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.months = months  # int
        
                self.crypto_currency = crypto_currency  # string
        
                self.crypto_amount = crypto_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftPremium":
        
        flags = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        months = Int.read(b)
        
        crypto_currency = String.read(b) if flags & (1 << 0) else None
        crypto_amount = Long.read(b) if flags & (1 << 0) else None
        return MessageActionGiftPremium(currency=currency, amount=amount, months=months, crypto_currency=crypto_currency, crypto_amount=crypto_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(Int(self.months))
        
        if self.crypto_currency is not None:
            b.write(String(self.crypto_currency))
        
        if self.crypto_amount is not None:
            b.write(Long(self.crypto_amount))
        
        return b.getvalue()