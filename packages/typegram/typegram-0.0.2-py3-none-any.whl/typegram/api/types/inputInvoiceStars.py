
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



class InputInvoiceStars(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputInvoice`.

    Details:
        - Layer: ``181``
        - ID: ``1DA33AD8``

option (:obj:`StarsTopupOption<typegram.api.ayiin.StarsTopupOption>`):
                    N/A
                
    """

    __slots__: List[str] = ["option"]

    ID = 0x1da33ad8
    QUALNAME = "types.inputInvoiceStars"

    def __init__(self, *, option: "api.ayiin.StarsTopupOption") -> None:
        
                self.option = option  # StarsTopupOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStars":
        # No flags
        
        option = Object.read(b)
        
        return InputInvoiceStars(option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.option.write())
        
        return b.getvalue()