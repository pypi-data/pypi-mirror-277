
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



class DocumentAttributeVideo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DocumentAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``D38FF1C2``

duration (``float`` ``64-bit``):
                    N/A
                
        w (``int`` ``32-bit``):
                    N/A
                
        h (``int`` ``32-bit``):
                    N/A
                
        round_message (``bool``, *optional*):
                    N/A
                
        supports_streaming (``bool``, *optional*):
                    N/A
                
        nosound (``bool``, *optional*):
                    N/A
                
        preload_prefix_size (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["duration", "w", "h", "round_message", "supports_streaming", "nosound", "preload_prefix_size"]

    ID = 0xd38ff1c2
    QUALNAME = "types.documentAttributeVideo"

    def __init__(self, *, duration: float, w: int, h: int, round_message: Optional[bool] = None, supports_streaming: Optional[bool] = None, nosound: Optional[bool] = None, preload_prefix_size: Optional[int] = None) -> None:
        
                self.duration = duration  # double
        
                self.w = w  # int
        
                self.h = h  # int
        
                self.round_message = round_message  # true
        
                self.supports_streaming = supports_streaming  # true
        
                self.nosound = nosound  # true
        
                self.preload_prefix_size = preload_prefix_size  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeVideo":
        
        flags = Int.read(b)
        
        round_message = True if flags & (1 << 0) else False
        supports_streaming = True if flags & (1 << 1) else False
        nosound = True if flags & (1 << 3) else False
        duration = Double.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        preload_prefix_size = Int.read(b) if flags & (1 << 2) else None
        return DocumentAttributeVideo(duration=duration, w=w, h=h, round_message=round_message, supports_streaming=supports_streaming, nosound=nosound, preload_prefix_size=preload_prefix_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Double(self.duration))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        if self.preload_prefix_size is not None:
            b.write(Int(self.preload_prefix_size))
        
        return b.getvalue()