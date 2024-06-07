
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



class GetArchivedStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``57F17692``

offset_id (``int`` ``64-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        masks (``bool``, *optional*):
                    N/A
                
        emojis (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.ArchivedStickers<typegram.api.ayiin.messages.ArchivedStickers>`
    """

    __slots__: List[str] = ["offset_id", "limit", "masks", "emojis"]

    ID = 0x57f17692
    QUALNAME = "functions.functionsmessages.ArchivedStickers"

    def __init__(self, *, offset_id: int, limit: int, masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        
                self.offset_id = offset_id  # long
        
                self.limit = limit  # int
        
                self.masks = masks  # true
        
                self.emojis = emojis  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetArchivedStickers":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        offset_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetArchivedStickers(offset_id=offset_id, limit=limit, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()