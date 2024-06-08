
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



class PremiumGiftOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PremiumGiftOption`.

    Details:
        - Layer: ``181``
        - ID: ``74C34319``

months (``int`` ``32-bit``):
                    N/A
                
        currency (``str``):
                    N/A
                
        amount (``int`` ``64-bit``):
                    N/A
                
        bot_url (``str``):
                    N/A
                
        store_product (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "store_product"]

    ID = 0x74c34319
    QUALNAME = "types.premiumGiftOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: str, store_product: Optional[str] = None) -> None:
        
                self.months = months  # int
        
                self.currency = currency  # string
        
                self.amount = amount  # long
        
                self.bot_url = bot_url  # string
        
                self.store_product = store_product  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumGiftOption":
        
        flags = Int.read(b)
        
        months = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        bot_url = String.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumGiftOption(months=months, currency=currency, amount=amount, bot_url=bot_url, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.months))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.bot_url))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        return b.getvalue()