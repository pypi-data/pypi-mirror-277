
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



class GetMultiWallPapers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``65AD71DC``

wallpapers (List of :obj:`InputWallPaper<typegram.api.ayiin.InputWallPaper>`):
                    N/A
                
    Returns:
        List of :obj:`WallPaper<typegram.api.ayiin.WallPaper>`
    """

    __slots__: List[str] = ["wallpapers"]

    ID = 0x65ad71dc
    QUALNAME = "functions.functions.Vector<WallPaper>"

    def __init__(self, *, wallpapers: List["ayiin.InputWallPaper"]) -> None:
        
                self.wallpapers = wallpapers  # InputWallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMultiWallPapers":
        # No flags
        
        wallpapers = Object.read(b)
        
        return GetMultiWallPapers(wallpapers=wallpapers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.wallpapers))
        
        return b.getvalue()