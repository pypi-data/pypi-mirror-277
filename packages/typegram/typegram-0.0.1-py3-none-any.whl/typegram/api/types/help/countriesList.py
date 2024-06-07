
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



class CountriesList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.CountriesList`.

    Details:
        - Layer: ``181``
        - ID: ``87D0759E``

countries (List of :obj:`help.Country<typegram.api.ayiin.help.Country>`):
                    N/A
                
        hash (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["countries", "hash"]

    ID = 0x87d0759e
    QUALNAME = "functions.typeshelp.CountriesList"

    def __init__(self, *, countries: List["ayiinhelp.Country"], hash: int) -> None:
        
                self.countries = countries  # help.Country
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountriesList":
        # No flags
        
        countries = Object.read(b)
        
        hash = Int.read(b)
        
        return CountriesList(countries=countries, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.countries))
        
        b.write(Int(self.hash))
        
        return b.getvalue()