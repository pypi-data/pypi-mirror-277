
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



class GetPeerMaxIDs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``535983C3``

id (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        List of ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id"]

    ID = 0x535983c3
    QUALNAME = "functions.functions.Vector<int>"

    def __init__(self, *, id: List["ayiin.InputPeer"]) -> None:
        
                self.id = id  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerMaxIDs":
        # No flags
        
        id = Object.read(b)
        
        return GetPeerMaxIDs(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()