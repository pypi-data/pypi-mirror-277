
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



class PeerColors(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PeerColors`.

    Details:
        - Layer: ``181``
        - ID: ``F8ED08``

hash (``int`` ``32-bit``):
                    N/A
                
        colors (List of :obj:`help.PeerColorOption<typegram.api.ayiin.help.PeerColorOption>`):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["hash", "colors"]

    ID = 0xf8ed08
    QUALNAME = "functions.typeshelp.PeerColors"

    def __init__(self, *, hash: int, colors: List["ayiinhelp.PeerColorOption"]) -> None:
        
                self.hash = hash  # int
        
                self.colors = colors  # help.PeerColorOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColors":
        # No flags
        
        hash = Int.read(b)
        
        colors = Object.read(b)
        
        return PeerColors(hash=hash, colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.colors))
        
        return b.getvalue()