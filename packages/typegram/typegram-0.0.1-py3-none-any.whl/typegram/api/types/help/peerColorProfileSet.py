
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



class PeerColorProfileSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PeerColorSet`.

    Details:
        - Layer: ``181``
        - ID: ``767D61EB``

palette_colors (List of ``int`` ``32-bit``):
                    N/A
                
        bg_colors (List of ``int`` ``32-bit``):
                    N/A
                
        story_colors (List of ``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["palette_colors", "bg_colors", "story_colors"]

    ID = 0x767d61eb
    QUALNAME = "functions.typeshelp.PeerColorSet"

    def __init__(self, *, palette_colors: List[int], bg_colors: List[int], story_colors: List[int]) -> None:
        
                self.palette_colors = palette_colors  # int
        
                self.bg_colors = bg_colors  # int
        
                self.story_colors = story_colors  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorProfileSet":
        # No flags
        
        palette_colors = Object.read(b, Int)
        
        bg_colors = Object.read(b, Int)
        
        story_colors = Object.read(b, Int)
        
        return PeerColorProfileSet(palette_colors=palette_colors, bg_colors=bg_colors, story_colors=story_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.palette_colors, Int))
        
        b.write(Vector(self.bg_colors, Int))
        
        b.write(Vector(self.story_colors, Int))
        
        return b.getvalue()