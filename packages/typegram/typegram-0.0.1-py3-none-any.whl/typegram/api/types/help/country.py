
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



class Country(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.Country`.

    Details:
        - Layer: ``181``
        - ID: ``C3878E23``

iso2 (``str``):
                    N/A
                
        default_name (``str``):
                    N/A
                
        country_codes (List of :obj:`help.CountryCode<typegram.api.ayiin.help.CountryCode>`):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
        name (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 12 functions.

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

    __slots__: List[str] = ["iso2", "default_name", "country_codes", "hidden", "name"]

    ID = 0xc3878e23
    QUALNAME = "functions.typeshelp.Country"

    def __init__(self, *, iso2: str, default_name: str, country_codes: List["ayiinhelp.CountryCode"], hidden: Optional[bool] = None, name: Optional[str] = None) -> None:
        
                self.iso2 = iso2  # string
        
                self.default_name = default_name  # string
        
                self.country_codes = country_codes  # help.CountryCode
        
                self.hidden = hidden  # true
        
                self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Country":
        
        flags = Int.read(b)
        
        hidden = True if flags & (1 << 0) else False
        iso2 = String.read(b)
        
        default_name = String.read(b)
        
        name = String.read(b) if flags & (1 << 1) else None
        country_codes = Object.read(b)
        
        return Country(iso2=iso2, default_name=default_name, country_codes=country_codes, hidden=hidden, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.iso2))
        
        b.write(String(self.default_name))
        
        if self.name is not None:
            b.write(String(self.name))
        
        b.write(Vector(self.country_codes))
        
        return b.getvalue()