
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



class SetChatWallPaper(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8FFACAE1``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        for_both (``bool``, *optional*):
                    N/A
                
        revert (``bool``, *optional*):
                    N/A
                
        wallpaper (:obj:`InputWallPaper<typegram.api.ayiin.InputWallPaper>`, *optional*):
                    N/A
                
        settings (:obj:`WallPaperSettings<typegram.api.ayiin.WallPaperSettings>`, *optional*):
                    N/A
                
        id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "for_both", "revert", "wallpaper", "settings", "id"]

    ID = 0x8ffacae1
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: "ayiin.InputWallPaper" = None, settings: "ayiin.WallPaperSettings" = None, id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.for_both = for_both  # true
        
                self.revert = revert  # true
        
                self.wallpaper = wallpaper  # InputWallPaper
        
                self.settings = settings  # WallPaperSettings
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatWallPaper":
        
        flags = Int.read(b)
        
        for_both = True if flags & (1 << 3) else False
        revert = True if flags & (1 << 4) else False
        peer = Object.read(b)
        
        wallpaper = Object.read(b) if flags & (1 << 0) else None
        
        settings = Object.read(b) if flags & (1 << 2) else None
        
        id = Int.read(b) if flags & (1 << 1) else None
        return SetChatWallPaper(peer=peer, for_both=for_both, revert=revert, wallpaper=wallpaper, settings=settings, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        if self.id is not None:
            b.write(Int(self.id))
        
        return b.getvalue()