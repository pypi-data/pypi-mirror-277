
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



class ExportedAuthorization(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.auth.ExportedAuthorization`.

    Details:
        - Layer: ``181``
        - ID: ``B434E2B8``

id (``int`` ``64-bit``):
                    N/A
                
        bytes (``bytes``):
                    N/A
                
    Functions:
        This object can be returned by 26 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            auth.exportAuthorization
    """

    __slots__: List[str] = ["id", "bytes"]

    ID = 0xb434e2b8
    QUALNAME = "types.auth.exportedAuthorization"

    def __init__(self, *, id: int, bytes: bytes) -> None:
        
                self.id = id  # long
        
                self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedAuthorization":
        # No flags
        
        id = Long.read(b)
        
        bytes = Bytes.read(b)
        
        return ExportedAuthorization(id=id, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()