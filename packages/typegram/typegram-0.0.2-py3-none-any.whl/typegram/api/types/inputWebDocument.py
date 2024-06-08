
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



class InputWebDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputWebDocument`.

    Details:
        - Layer: ``181``
        - ID: ``9BED434D``

url (``str``):
                    N/A
                
        size (``int`` ``32-bit``):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        attributes (List of :obj:`DocumentAttribute<typegram.api.ayiin.DocumentAttribute>`):
                    N/A
                
    """

    __slots__: List[str] = ["url", "size", "mime_type", "attributes"]

    ID = 0x9bed434d
    QUALNAME = "types.inputWebDocument"

    def __init__(self, *, url: str, size: int, mime_type: str, attributes: List["api.ayiin.DocumentAttribute"]) -> None:
        
                self.url = url  # string
        
                self.size = size  # int
        
                self.mime_type = mime_type  # string
        
                self.attributes = attributes  # DocumentAttribute

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebDocument":
        # No flags
        
        url = String.read(b)
        
        size = Int.read(b)
        
        mime_type = String.read(b)
        
        attributes = Object.read(b)
        
        return InputWebDocument(url=url, size=size, mime_type=mime_type, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.size))
        
        b.write(String(self.mime_type))
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()