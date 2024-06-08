
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



class AttachMenuBotIcon(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AttachMenuBotIcon`.

    Details:
        - Layer: ``181``
        - ID: ``B2A7386B``

name (``str``):
                    N/A
                
        icon (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        colors (List of :obj:`AttachMenuBotIconColor<typegram.api.ayiin.AttachMenuBotIconColor>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["name", "icon", "colors"]

    ID = 0xb2a7386b
    QUALNAME = "types.attachMenuBotIcon"

    def __init__(self, *, name: str, icon: "api.ayiin.Document", colors: Optional[List["api.ayiin.AttachMenuBotIconColor"]] = None) -> None:
        
                self.name = name  # string
        
                self.icon = icon  # Document
        
                self.colors = colors  # AttachMenuBotIconColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotIcon":
        
        flags = Int.read(b)
        
        name = String.read(b)
        
        icon = Object.read(b)
        
        colors = Object.read(b) if flags & (1 << 0) else []
        
        return AttachMenuBotIcon(name=name, icon=icon, colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(self.icon.write())
        
        if self.colors is not None:
            b.write(Vector(self.colors))
        
        return b.getvalue()