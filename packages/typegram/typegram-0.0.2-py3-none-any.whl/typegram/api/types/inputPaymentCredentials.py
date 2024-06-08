
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



class InputPaymentCredentials(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPaymentCredentials`.

    Details:
        - Layer: ``181``
        - ID: ``3417D728``

data (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        save (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["data", "save"]

    ID = 0x3417d728
    QUALNAME = "types.inputPaymentCredentials"

    def __init__(self, *, data: "api.ayiin.DataJSON", save: Optional[bool] = None) -> None:
        
                self.data = data  # DataJSON
        
                self.save = save  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentials":
        
        flags = Int.read(b)
        
        save = True if flags & (1 << 0) else False
        data = Object.read(b)
        
        return InputPaymentCredentials(data=data, save=save)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.data.write())
        
        return b.getvalue()