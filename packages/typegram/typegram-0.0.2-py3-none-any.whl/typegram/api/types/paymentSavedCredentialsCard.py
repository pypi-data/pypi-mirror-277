
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



class PaymentSavedCredentialsCard(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PaymentSavedCredentials`.

    Details:
        - Layer: ``181``
        - ID: ``CDC27A1F``

id (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "title"]

    ID = 0xcdc27a1f
    QUALNAME = "types.paymentSavedCredentialsCard"

    def __init__(self, *, id: str, title: str) -> None:
        
                self.id = id  # string
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentSavedCredentialsCard":
        # No flags
        
        id = String.read(b)
        
        title = String.read(b)
        
        return PaymentSavedCredentialsCard(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()