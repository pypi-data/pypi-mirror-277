
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



class PassportConfig(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PassportConfig`.

    Details:
        - Layer: ``181``
        - ID: ``A098D6AF``

hash (``int`` ``32-bit``):
                    N/A
                
        countries_langs (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["hash", "countries_langs"]

    ID = 0xa098d6af
    QUALNAME = "functions.typeshelp.PassportConfig"

    def __init__(self, *, hash: int, countries_langs: "ayiin.DataJSON") -> None:
        
                self.hash = hash  # int
        
                self.countries_langs = countries_langs  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PassportConfig":
        # No flags
        
        hash = Int.read(b)
        
        countries_langs = Object.read(b)
        
        return PassportConfig(hash=hash, countries_langs=countries_langs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(self.countries_langs.write())
        
        return b.getvalue()