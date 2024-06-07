
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



class GetDeepLinkInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3FEDC75F``

path (``str``):
                    N/A
                
    Returns:
        :obj:`help.DeepLinkInfo<typegram.api.ayiin.help.DeepLinkInfo>`
    """

    __slots__: List[str] = ["path"]

    ID = 0x3fedc75f
    QUALNAME = "functions.functionshelp.DeepLinkInfo"

    def __init__(self, *, path: str) -> None:
        
                self.path = path  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDeepLinkInfo":
        # No flags
        
        path = String.read(b)
        
        return GetDeepLinkInfo(path=path)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.path))
        
        return b.getvalue()