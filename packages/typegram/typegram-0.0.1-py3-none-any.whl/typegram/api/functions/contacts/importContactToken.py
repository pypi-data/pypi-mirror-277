
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



class ImportContactToken(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``13005788``

token (``str``):
                    N/A
                
    Returns:
        :obj:`User<typegram.api.ayiin.User>`
    """

    __slots__: List[str] = ["token"]

    ID = 0x13005788
    QUALNAME = "functions.functions.User"

    def __init__(self, *, token: str) -> None:
        
                self.token = token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ImportContactToken":
        # No flags
        
        token = String.read(b)
        
        return ImportContactToken(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.token))
        
        return b.getvalue()