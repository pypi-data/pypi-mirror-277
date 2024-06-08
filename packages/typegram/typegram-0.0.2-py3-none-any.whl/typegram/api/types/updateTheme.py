
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



class UpdateTheme(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``8216FBA3``

theme (:obj:`Theme<typegram.api.ayiin.Theme>`):
                    N/A
                
    """

    __slots__: List[str] = ["theme"]

    ID = 0x8216fba3
    QUALNAME = "types.updateTheme"

    def __init__(self, *, theme: "api.ayiin.Theme") -> None:
        
                self.theme = theme  # Theme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTheme":
        # No flags
        
        theme = Object.read(b)
        
        return UpdateTheme(theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.theme.write())
        
        return b.getvalue()