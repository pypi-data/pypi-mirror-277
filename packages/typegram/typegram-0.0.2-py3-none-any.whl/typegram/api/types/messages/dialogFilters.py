
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



class DialogFilters(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.DialogFilters`.

    Details:
        - Layer: ``181``
        - ID: ``2AD93719``

filters (List of :obj:`DialogFilter<typegram.api.ayiin.DialogFilter>`):
                    N/A
                
        tags_enabled (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["filters", "tags_enabled"]

    ID = 0x2ad93719
    QUALNAME = "types.messages.dialogFilters"

    def __init__(self, *, filters: List["api.ayiin.DialogFilter"], tags_enabled: Optional[bool] = None) -> None:
        
                self.filters = filters  # DialogFilter
        
                self.tags_enabled = tags_enabled  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilters":
        
        flags = Int.read(b)
        
        tags_enabled = True if flags & (1 << 0) else False
        filters = Object.read(b)
        
        return DialogFilters(filters=filters, tags_enabled=tags_enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.filters))
        
        return b.getvalue()