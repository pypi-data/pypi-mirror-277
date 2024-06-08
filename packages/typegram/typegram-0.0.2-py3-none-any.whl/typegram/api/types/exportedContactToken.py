
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



class ExportedContactToken(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ExportedContactToken`.

    Details:
        - Layer: ``181``
        - ID: ``41BF109B``

url (``str``):
                    N/A
                
        expires (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["url", "expires"]

    ID = 0x41bf109b
    QUALNAME = "types.exportedContactToken"

    def __init__(self, *, url: str, expires: int) -> None:
        
                self.url = url  # string
        
                self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedContactToken":
        # No flags
        
        url = String.read(b)
        
        expires = Int.read(b)
        
        return ExportedContactToken(url=url, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.expires))
        
        return b.getvalue()