
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



class PeerColorSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PeerColorSet`.

    Details:
        - Layer: ``181``
        - ID: ``26219A58``

colors (List of ``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["colors"]

    ID = 0x26219a58
    QUALNAME = "types.help.peerColorSet"

    def __init__(self, *, colors: List[int]) -> None:
        
                self.colors = colors  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorSet":
        # No flags
        
        colors = Object.read(b, Int)
        
        return PeerColorSet(colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.colors, Int))
        
        return b.getvalue()