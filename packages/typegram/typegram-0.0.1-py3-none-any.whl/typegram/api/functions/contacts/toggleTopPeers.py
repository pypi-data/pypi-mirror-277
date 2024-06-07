
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



class ToggleTopPeers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8514BDDA``

enabled (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["enabled"]

    ID = 0x8514bdda
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, enabled: bool) -> None:
        
                self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleTopPeers":
        # No flags
        
        enabled = Bool.read(b)
        
        return ToggleTopPeers(enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()