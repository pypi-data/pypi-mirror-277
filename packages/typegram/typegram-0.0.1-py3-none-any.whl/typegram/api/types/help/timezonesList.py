
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



class TimezonesList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.TimezonesList`.

    Details:
        - Layer: ``181``
        - ID: ``7B74ED71``

timezones (List of :obj:`Timezone<typegram.api.ayiin.Timezone>`):
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

    __slots__: List[str] = ["timezones", "hash"]

    ID = 0x7b74ed71
    QUALNAME = "functions.typeshelp.TimezonesList"

    def __init__(self, *, timezones: List["ayiin.Timezone"], hash: int) -> None:
        
                self.timezones = timezones  # Timezone
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TimezonesList":
        # No flags
        
        timezones = Object.read(b)
        
        hash = Int.read(b)
        
        return TimezonesList(timezones=timezones, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.timezones))
        
        b.write(Int(self.hash))
        
        return b.getvalue()