
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



class InputPaymentCredentialsSaved(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPaymentCredentials`.

    Details:
        - Layer: ``181``
        - ID: ``C10EB2CF``

id (``str``):
                    N/A
                
        tmp_password (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["id", "tmp_password"]

    ID = 0xc10eb2cf
    QUALNAME = "types.inputPaymentCredentialsSaved"

    def __init__(self, *, id: str, tmp_password: bytes) -> None:
        
                self.id = id  # string
        
                self.tmp_password = tmp_password  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPaymentCredentialsSaved":
        # No flags
        
        id = String.read(b)
        
        tmp_password = Bytes.read(b)
        
        return InputPaymentCredentialsSaved(id=id, tmp_password=tmp_password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(Bytes(self.tmp_password))
        
        return b.getvalue()