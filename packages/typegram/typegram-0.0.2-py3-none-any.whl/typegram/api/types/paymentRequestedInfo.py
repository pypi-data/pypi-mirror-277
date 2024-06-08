
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



class PaymentRequestedInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PaymentRequestedInfo`.

    Details:
        - Layer: ``181``
        - ID: ``909C3F94``

name (``str``, *optional*):
                    N/A
                
        phone (``str``, *optional*):
                    N/A
                
        email (``str``, *optional*):
                    N/A
                
        shipping_address (:obj:`PostAddress<typegram.api.ayiin.PostAddress>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["name", "phone", "email", "shipping_address"]

    ID = 0x909c3f94
    QUALNAME = "types.paymentRequestedInfo"

    def __init__(self, *, name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, shipping_address: "api.ayiin.PostAddress" = None) -> None:
        
                self.name = name  # string
        
                self.phone = phone  # string
        
                self.email = email  # string
        
                self.shipping_address = shipping_address  # PostAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentRequestedInfo":
        
        flags = Int.read(b)
        
        name = String.read(b) if flags & (1 << 0) else None
        phone = String.read(b) if flags & (1 << 1) else None
        email = String.read(b) if flags & (1 << 2) else None
        shipping_address = Object.read(b) if flags & (1 << 3) else None
        
        return PaymentRequestedInfo(name=name, phone=phone, email=email, shipping_address=shipping_address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.name is not None:
            b.write(String(self.name))
        
        if self.phone is not None:
            b.write(String(self.phone))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.shipping_address is not None:
            b.write(self.shipping_address.write())
        
        return b.getvalue()