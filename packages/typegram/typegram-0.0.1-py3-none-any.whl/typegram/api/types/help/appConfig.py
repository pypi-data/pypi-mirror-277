
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



class AppConfig(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.AppConfig`.

    Details:
        - Layer: ``181``
        - ID: ``DD18782E``

hash (``int`` ``32-bit``):
                    N/A
                
        config (:obj:`JSONValue<typegram.api.ayiin.JSONValue>`):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["hash", "config"]

    ID = 0xdd18782e
    QUALNAME = "functions.typeshelp.AppConfig"

    def __init__(self, *, hash: int, config: "ayiin.JSONValue") -> None:
        
                self.hash = hash  # int
        
                self.config = config  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfig":
        # No flags
        
        hash = Int.read(b)
        
        config = Object.read(b)
        
        return AppConfig(hash=hash, config=config)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(self.config.write())
        
        return b.getvalue()