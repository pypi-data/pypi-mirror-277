
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



class GetCollectibleInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BE1E85BA``

collectible (:obj:`InputCollectible<typegram.api.ayiin.InputCollectible>`):
                    N/A
                
    Returns:
        :obj:`fragment.CollectibleInfo<typegram.api.ayiin.fragment.CollectibleInfo>`
    """

    __slots__: List[str] = ["collectible"]

    ID = 0xbe1e85ba
    QUALNAME = "functions.functionsfragment.CollectibleInfo"

    def __init__(self, *, collectible: "ayiin.InputCollectible") -> None:
        
                self.collectible = collectible  # InputCollectible

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCollectibleInfo":
        # No flags
        
        collectible = Object.read(b)
        
        return GetCollectibleInfo(collectible=collectible)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.collectible.write())
        
        return b.getvalue()