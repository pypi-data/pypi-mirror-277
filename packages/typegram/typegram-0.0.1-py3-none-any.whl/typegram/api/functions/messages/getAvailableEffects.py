
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



class GetAvailableEffects(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DEA20A39``

hash (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.AvailableEffects<typegram.api.ayiin.messages.AvailableEffects>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xdea20a39
    QUALNAME = "functions.functionsmessages.AvailableEffects"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAvailableEffects":
        # No flags
        
        hash = Int.read(b)
        
        return GetAvailableEffects(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()