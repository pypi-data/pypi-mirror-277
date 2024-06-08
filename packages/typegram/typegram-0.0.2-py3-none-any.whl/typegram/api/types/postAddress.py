
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class PostAddress(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PostAddress`.

    Details:
        - Layer: ``181``
        - ID: ``1E8CAAEB``

street_line1 (``str``):
                    N/A
                
        street_line2 (``str``):
                    N/A
                
        city (``str``):
                    N/A
                
        state (``str``):
                    N/A
                
        country_iso2 (``str``):
                    N/A
                
        post_code (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["street_line1", "street_line2", "city", "state", "country_iso2", "post_code"]

    ID = 0x1e8caaeb
    QUALNAME = "types.postAddress"

    def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str) -> None:
        
                self.street_line1 = street_line1  # string
        
                self.street_line2 = street_line2  # string
        
                self.city = city  # string
        
                self.state = state  # string
        
                self.country_iso2 = country_iso2  # string
        
                self.post_code = post_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostAddress":
        # No flags
        
        street_line1 = String.read(b)
        
        street_line2 = String.read(b)
        
        city = String.read(b)
        
        state = String.read(b)
        
        country_iso2 = String.read(b)
        
        post_code = String.read(b)
        
        return PostAddress(street_line1=street_line1, street_line2=street_line2, city=city, state=state, country_iso2=country_iso2, post_code=post_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.street_line1))
        
        b.write(String(self.street_line2))
        
        b.write(String(self.city))
        
        b.write(String(self.state))
        
        b.write(String(self.country_iso2))
        
        b.write(String(self.post_code))
        
        return b.getvalue()