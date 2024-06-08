
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



class UpdateStarsBalance(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``FB85198``

balance (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["balance"]

    ID = 0xfb85198
    QUALNAME = "types.updateStarsBalance"

    def __init__(self, *, balance: int) -> None:
        
                self.balance = balance  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateStarsBalance":
        # No flags
        
        balance = Long.read(b)
        
        return UpdateStarsBalance(balance=balance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.balance))
        
        return b.getvalue()