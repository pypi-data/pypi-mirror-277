
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



class InputPaymentCredentialsGooglePay(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPaymentCredentials`.

    Details:
        - Layer: ``181``
        - ID: ``8AC32801``

payment_token (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    """

    __slots__: List[str] = ["payment_token"]

    ID = 0x8ac32801
    QUALNAME = "types.inputPaymentCredentialsGooglePay"

    def __init__(self, *, payment_token: "api.ayiin.DataJSON") -> None:
        
                self.payment_token = payment_token  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentialsGooglePay":
        # No flags
        
        payment_token = Object.read(b)
        
        return InputPaymentCredentialsGooglePay(payment_token=payment_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.payment_token.write())
        
        return b.getvalue()