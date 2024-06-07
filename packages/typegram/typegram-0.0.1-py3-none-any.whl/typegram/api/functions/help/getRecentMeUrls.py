
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



class GetRecentMeUrls(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3DC0F114``

referer (``str``):
                    N/A
                
    Returns:
        :obj:`help.RecentMeUrls<typegram.api.ayiin.help.RecentMeUrls>`
    """

    __slots__: List[str] = ["referer"]

    ID = 0x3dc0f114
    QUALNAME = "functions.functionshelp.RecentMeUrls"

    def __init__(self, *, referer: str) -> None:
        
                self.referer = referer  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentMeUrls":
        # No flags
        
        referer = String.read(b)
        
        return GetRecentMeUrls(referer=referer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.referer))
        
        return b.getvalue()