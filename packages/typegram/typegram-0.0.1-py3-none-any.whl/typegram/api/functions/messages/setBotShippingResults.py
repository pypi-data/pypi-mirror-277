
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



class SetBotShippingResults(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E5F672FA``

query_id (``int`` ``64-bit``):
                    N/A
                
        error (``str``, *optional*):
                    N/A
                
        shipping_options (List of :obj:`ShippingOption<typegram.api.ayiin.ShippingOption>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "error", "shipping_options"]

    ID = 0xe5f672fa
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, query_id: int, error: Optional[str] = None, shipping_options: Optional[List["ayiin.ShippingOption"]] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.error = error  # string
        
                self.shipping_options = shipping_options  # ShippingOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotShippingResults":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        shipping_options = Object.read(b) if flags & (1 << 1) else []
        
        return SetBotShippingResults(query_id=query_id, error=error, shipping_options=shipping_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        if self.shipping_options is not None:
            b.write(Vector(self.shipping_options))
        
        return b.getvalue()