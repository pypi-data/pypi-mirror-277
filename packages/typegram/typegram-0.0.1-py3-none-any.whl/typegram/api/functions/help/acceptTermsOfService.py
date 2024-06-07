
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



class AcceptTermsOfService(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``EE72F79A``

id (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xee72f79a
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, id: "ayiin.DataJSON") -> None:
        
                self.id = id  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptTermsOfService":
        # No flags
        
        id = Object.read(b)
        
        return AcceptTermsOfService(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()