
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



class StickerPack(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StickerPack`.

    Details:
        - Layer: ``181``
        - ID: ``12B299D4``

emoticon (``str``):
                    N/A
                
        documents (List of ``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["emoticon", "documents"]

    ID = 0x12b299d4
    QUALNAME = "types.stickerPack"

    def __init__(self, *, emoticon: str, documents: List[int]) -> None:
        
                self.emoticon = emoticon  # string
        
                self.documents = documents  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerPack":
        # No flags
        
        emoticon = String.read(b)
        
        documents = Object.read(b, Long)
        
        return StickerPack(emoticon=emoticon, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        b.write(Vector(self.documents, Long))
        
        return b.getvalue()