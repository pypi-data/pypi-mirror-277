
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



class CdnConfig(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.CdnConfig`.

    Details:
        - Layer: ``181``
        - ID: ``5725E40A``

public_keys (List of :obj:`CdnPublicKey<typegram.api.ayiin.CdnPublicKey>`):
                    N/A
                
    """

    __slots__: List[str] = ["public_keys"]

    ID = 0x5725e40a
    QUALNAME = "types.cdnConfig"

    def __init__(self, *, public_keys: List["api.ayiin.CdnPublicKey"]) -> None:
        
                self.public_keys = public_keys  # CdnPublicKey

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnConfig":
        # No flags
        
        public_keys = Object.read(b)
        
        return CdnConfig(public_keys=public_keys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.public_keys))
        
        return b.getvalue()