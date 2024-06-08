
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



class DataJSON(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DataJSON`.

    Details:
        - Layer: ``181``
        - ID: ``7D748D04``

data (``str``):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            bots.sendCustomRequest
            bots.invokeWebViewCustomMethod
    """

    __slots__: List[str] = ["data"]

    ID = 0x7d748d04
    QUALNAME = "types.dataJSON"

    def __init__(self, *, data: str) -> None:
        
                self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DataJSON":
        # No flags
        
        data = String.read(b)
        
        return DataJSON(data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.data))
        
        return b.getvalue()