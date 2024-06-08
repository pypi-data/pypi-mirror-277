
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



class TranslateResult(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.TranslatedText`.

    Details:
        - Layer: ``181``
        - ID: ``33DB32F8``

result (List of :obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.translateText
    """

    __slots__: List[str] = ["result"]

    ID = 0x33db32f8
    QUALNAME = "types.messages.translateResult"

    def __init__(self, *, result: List["api.ayiin.TextWithEntities"]) -> None:
        
                self.result = result  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateResult":
        # No flags
        
        result = Object.read(b)
        
        return TranslateResult(result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.result))
        
        return b.getvalue()