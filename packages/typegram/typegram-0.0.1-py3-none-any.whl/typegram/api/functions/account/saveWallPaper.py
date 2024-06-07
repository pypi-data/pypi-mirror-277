
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



class SaveWallPaper(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6C5A5B37``

wallpaper (:obj:`InputWallPaper<typegram.api.ayiin.InputWallPaper>`):
                    N/A
                
        unsave (``bool``):
                    N/A
                
        settings (:obj:`WallPaperSettings<typegram.api.ayiin.WallPaperSettings>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["wallpaper", "unsave", "settings"]

    ID = 0x6c5a5b37
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, wallpaper: "ayiin.InputWallPaper", unsave: bool, settings: "ayiin.WallPaperSettings") -> None:
        
                self.wallpaper = wallpaper  # InputWallPaper
        
                self.unsave = unsave  # Bool
        
                self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveWallPaper":
        # No flags
        
        wallpaper = Object.read(b)
        
        unsave = Bool.read(b)
        
        settings = Object.read(b)
        
        return SaveWallPaper(wallpaper=wallpaper, unsave=unsave, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        b.write(Bool(self.unsave))
        
        b.write(self.settings.write())
        
        return b.getvalue()