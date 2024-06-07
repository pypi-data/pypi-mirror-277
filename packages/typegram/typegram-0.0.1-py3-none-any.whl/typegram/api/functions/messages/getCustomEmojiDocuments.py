
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



class GetCustomEmojiDocuments(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D9AB0F54``

document_id (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        List of :obj:`Document<typegram.api.ayiin.Document>`
    """

    __slots__: List[str] = ["document_id"]

    ID = 0xd9ab0f54
    QUALNAME = "functions.functions.Vector<Document>"

    def __init__(self, *, document_id: List[int]) -> None:
        
                self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCustomEmojiDocuments":
        # No flags
        
        document_id = Object.read(b, Long)
        
        return GetCustomEmojiDocuments(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.document_id, Long))
        
        return b.getvalue()