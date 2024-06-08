
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



class SecureSecretSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureSecretSettings`.

    Details:
        - Layer: ``181``
        - ID: ``1527BCAC``

secure_algo (:obj:`SecurePasswordKdfAlgo<typegram.api.ayiin.SecurePasswordKdfAlgo>`):
                    N/A
                
        secure_secret (``bytes``):
                    N/A
                
        secure_secret_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["secure_algo", "secure_secret", "secure_secret_id"]

    ID = 0x1527bcac
    QUALNAME = "types.secureSecretSettings"

    def __init__(self, *, secure_algo: "api.ayiin.SecurePasswordKdfAlgo", secure_secret: bytes, secure_secret_id: int) -> None:
        
                self.secure_algo = secure_algo  # SecurePasswordKdfAlgo
        
                self.secure_secret = secure_secret  # bytes
        
                self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureSecretSettings":
        # No flags
        
        secure_algo = Object.read(b)
        
        secure_secret = Bytes.read(b)
        
        secure_secret_id = Long.read(b)
        
        return SecureSecretSettings(secure_algo=secure_algo, secure_secret=secure_secret, secure_secret_id=secure_secret_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.secure_algo.write())
        
        b.write(Bytes(self.secure_secret))
        
        b.write(Long(self.secure_secret_id))
        
        return b.getvalue()