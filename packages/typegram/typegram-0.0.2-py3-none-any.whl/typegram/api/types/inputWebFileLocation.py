
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



class InputWebFileLocation(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputWebFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``C239D686``

url (``str``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["url", "access_hash"]

    ID = 0xc239d686
    QUALNAME = "types.inputWebFileLocation"

    def __init__(self, *, url: str, access_hash: int) -> None:
        
                self.url = url  # string
        
                self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileLocation":
        # No flags
        
        url = String.read(b)
        
        access_hash = Long.read(b)
        
        return InputWebFileLocation(url=url, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()