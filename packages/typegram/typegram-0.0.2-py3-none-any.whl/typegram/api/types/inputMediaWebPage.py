
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



class InputMediaWebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``C21B8849``

url (``str``):
                    N/A
                
        force_large_media (``bool``, *optional*):
                    N/A
                
        force_small_media (``bool``, *optional*):
                    N/A
                
        optional (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["url", "force_large_media", "force_small_media", "optional"]

    ID = 0xc21b8849
    QUALNAME = "types.inputMediaWebPage"

    def __init__(self, *, url: str, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None) -> None:
        
                self.url = url  # string
        
                self.force_large_media = force_large_media  # true
        
                self.force_small_media = force_small_media  # true
        
                self.optional = optional  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaWebPage":
        
        flags = Int.read(b)
        
        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        optional = True if flags & (1 << 2) else False
        url = String.read(b)
        
        return InputMediaWebPage(url=url, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        return b.getvalue()