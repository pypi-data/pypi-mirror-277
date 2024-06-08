
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



class PromoDataEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PromoData`.

    Details:
        - Layer: ``181``
        - ID: ``98F6AC75``

expires (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["expires"]

    ID = 0x98f6ac75
    QUALNAME = "types.help.promoDataEmpty"

    def __init__(self, *, expires: int) -> None:
        
                self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PromoDataEmpty":
        # No flags
        
        expires = Int.read(b)
        
        return PromoDataEmpty(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        return b.getvalue()