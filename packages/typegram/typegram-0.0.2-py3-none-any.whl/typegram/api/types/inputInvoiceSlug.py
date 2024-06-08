
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



class InputInvoiceSlug(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputInvoice`.

    Details:
        - Layer: ``181``
        - ID: ``C326CAEF``

slug (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["slug"]

    ID = 0xc326caef
    QUALNAME = "types.inputInvoiceSlug"

    def __init__(self, *, slug: str) -> None:
        
                self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceSlug":
        # No flags
        
        slug = String.read(b)
        
        return InputInvoiceSlug(slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        return b.getvalue()