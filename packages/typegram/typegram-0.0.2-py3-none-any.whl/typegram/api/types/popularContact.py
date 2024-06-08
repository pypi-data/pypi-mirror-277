
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



class PopularContact(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PopularContact`.

    Details:
        - Layer: ``181``
        - ID: ``5CE14175``

client_id (``int`` ``64-bit``):
                    N/A
                
        importers (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["client_id", "importers"]

    ID = 0x5ce14175
    QUALNAME = "types.popularContact"

    def __init__(self, *, client_id: int, importers: int) -> None:
        
                self.client_id = client_id  # long
        
                self.importers = importers  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PopularContact":
        # No flags
        
        client_id = Long.read(b)
        
        importers = Int.read(b)
        
        return PopularContact(client_id=client_id, importers=importers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.client_id))
        
        b.write(Int(self.importers))
        
        return b.getvalue()