
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



class GetWallPaper(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FC8DDBEA``

wallpaper (:obj:`InputWallPaper<typegram.api.ayiin.InputWallPaper>`):
                    N/A
                
    Returns:
        :obj:`WallPaper<typegram.api.ayiin.WallPaper>`
    """

    __slots__: List[str] = ["wallpaper"]

    ID = 0xfc8ddbea
    QUALNAME = "functions.functions.WallPaper"

    def __init__(self, *, wallpaper: "ayiin.InputWallPaper") -> None:
        
                self.wallpaper = wallpaper  # InputWallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWallPaper":
        # No flags
        
        wallpaper = Object.read(b)
        
        return GetWallPaper(wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()