
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



class UpdateDcOptions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``8E5E9873``

dc_options (List of :obj:`DcOption<typegram.api.ayiin.DcOption>`):
                    N/A
                
    """

    __slots__: List[str] = ["dc_options"]

    ID = 0x8e5e9873
    QUALNAME = "types.updateDcOptions"

    def __init__(self, *, dc_options: List["api.ayiin.DcOption"]) -> None:
        
                self.dc_options = dc_options  # DcOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDcOptions":
        # No flags
        
        dc_options = Object.read(b)
        
        return UpdateDcOptions(dc_options=dc_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.dc_options))
        
        return b.getvalue()