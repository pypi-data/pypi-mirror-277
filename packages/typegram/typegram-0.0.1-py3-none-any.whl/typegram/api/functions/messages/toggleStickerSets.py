
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



class ToggleStickerSets(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B5052FEA``

stickersets (List of :obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
        uninstall (``bool``, *optional*):
                    N/A
                
        archive (``bool``, *optional*):
                    N/A
                
        unarchive (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["stickersets", "uninstall", "archive", "unarchive"]

    ID = 0xb5052fea
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, stickersets: List["ayiin.InputStickerSet"], uninstall: Optional[bool] = None, archive: Optional[bool] = None, unarchive: Optional[bool] = None) -> None:
        
                self.stickersets = stickersets  # InputStickerSet
        
                self.uninstall = uninstall  # true
        
                self.archive = archive  # true
        
                self.unarchive = unarchive  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleStickerSets":
        
        flags = Int.read(b)
        
        uninstall = True if flags & (1 << 0) else False
        archive = True if flags & (1 << 1) else False
        unarchive = True if flags & (1 << 2) else False
        stickersets = Object.read(b)
        
        return ToggleStickerSets(stickersets=stickersets, uninstall=uninstall, archive=archive, unarchive=unarchive)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.stickersets))
        
        return b.getvalue()