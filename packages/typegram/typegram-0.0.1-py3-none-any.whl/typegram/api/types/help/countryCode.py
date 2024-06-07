
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



class CountryCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.CountryCode`.

    Details:
        - Layer: ``181``
        - ID: ``4203C5EF``

country_code (``str``):
                    N/A
                
        prefixes (List of ``str``, *optional*):
                    N/A
                
        patterns (List of ``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["country_code", "prefixes", "patterns"]

    ID = 0x4203c5ef
    QUALNAME = "functions.typeshelp.CountryCode"

    def __init__(self, *, country_code: str, prefixes: Optional[List[str]] = None, patterns: Optional[List[str]] = None) -> None:
        
                self.country_code = country_code  # string
        
                self.prefixes = prefixes  # string
        
                self.patterns = patterns  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CountryCode":
        
        flags = Int.read(b)
        
        country_code = String.read(b)
        
        prefixes = Object.read(b, String) if flags & (1 << 0) else []
        
        patterns = Object.read(b, String) if flags & (1 << 1) else []
        
        return CountryCode(country_code=country_code, prefixes=prefixes, patterns=patterns)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.country_code))
        
        if self.prefixes is not None:
            b.write(Vector(self.prefixes, String))
        
        if self.patterns is not None:
            b.write(Vector(self.patterns, String))
        
        return b.getvalue()