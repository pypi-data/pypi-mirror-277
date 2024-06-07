
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



class StartHistoryImport(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B43DF344``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        import_id (``int`` ``64-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "import_id"]

    ID = 0xb43df344
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", import_id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.import_id = import_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartHistoryImport":
        # No flags
        
        peer = Object.read(b)
        
        import_id = Long.read(b)
        
        return StartHistoryImport(peer=peer, import_id=import_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        return b.getvalue()