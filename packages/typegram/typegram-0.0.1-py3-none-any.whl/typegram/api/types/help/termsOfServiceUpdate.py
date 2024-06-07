
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



class TermsOfServiceUpdate(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``181``
        - ID: ``28ECF961``

expires (``int`` ``32-bit``):
                    N/A
                
        terms_of_service (:obj:`help.TermsOfService<typegram.api.ayiin.help.TermsOfService>`):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

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

    __slots__: List[str] = ["expires", "terms_of_service"]

    ID = 0x28ecf961
    QUALNAME = "functions.typeshelp.TermsOfServiceUpdate"

    def __init__(self, *, expires: int, terms_of_service: "ayiinhelp.TermsOfService") -> None:
        
                self.expires = expires  # int
        
                self.terms_of_service = terms_of_service  # help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfServiceUpdate":
        # No flags
        
        expires = Int.read(b)
        
        terms_of_service = Object.read(b)
        
        return TermsOfServiceUpdate(expires=expires, terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        b.write(self.terms_of_service.write())
        
        return b.getvalue()