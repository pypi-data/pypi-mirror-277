
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



class StickerKeyword(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StickerKeyword`.

    Details:
        - Layer: ``181``
        - ID: ``FCFEB29C``

document_id (``int`` ``64-bit``):
                    N/A
                
        keyword (List of ``str``):
                    N/A
                
    """

    __slots__: List[str] = ["document_id", "keyword"]

    ID = 0xfcfeb29c
    QUALNAME = "types.stickerKeyword"

    def __init__(self, *, document_id: int, keyword: List[str]) -> None:
        
                self.document_id = document_id  # long
        
                self.keyword = keyword  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerKeyword":
        # No flags
        
        document_id = Long.read(b)
        
        keyword = Object.read(b, String)
        
        return StickerKeyword(document_id=document_id, keyword=keyword)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(Vector(self.keyword, String))
        
        return b.getvalue()