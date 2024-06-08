
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



class AvailableReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AvailableReaction`.

    Details:
        - Layer: ``181``
        - ID: ``C077EC01``

reaction (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
        static_icon (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        appear_animation (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        select_animation (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        activate_animation (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        effect_animation (:obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        inactive (``bool``, *optional*):
                    N/A
                
        premium (``bool``, *optional*):
                    N/A
                
        around_animation (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        center_icon (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["reaction", "title", "static_icon", "appear_animation", "select_animation", "activate_animation", "effect_animation", "inactive", "premium", "around_animation", "center_icon"]

    ID = 0xc077ec01
    QUALNAME = "types.availableReaction"

    def __init__(self, *, reaction: str, title: str, static_icon: "api.ayiin.Document", appear_animation: "api.ayiin.Document", select_animation: "api.ayiin.Document", activate_animation: "api.ayiin.Document", effect_animation: "api.ayiin.Document", inactive: Optional[bool] = None, premium: Optional[bool] = None, around_animation: "api.ayiin.Document" = None, center_icon: "api.ayiin.Document" = None) -> None:
        
                self.reaction = reaction  # string
        
                self.title = title  # string
        
                self.static_icon = static_icon  # Document
        
                self.appear_animation = appear_animation  # Document
        
                self.select_animation = select_animation  # Document
        
                self.activate_animation = activate_animation  # Document
        
                self.effect_animation = effect_animation  # Document
        
                self.inactive = inactive  # true
        
                self.premium = premium  # true
        
                self.around_animation = around_animation  # Document
        
                self.center_icon = center_icon  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReaction":
        
        flags = Int.read(b)
        
        inactive = True if flags & (1 << 0) else False
        premium = True if flags & (1 << 2) else False
        reaction = String.read(b)
        
        title = String.read(b)
        
        static_icon = Object.read(b)
        
        appear_animation = Object.read(b)
        
        select_animation = Object.read(b)
        
        activate_animation = Object.read(b)
        
        effect_animation = Object.read(b)
        
        around_animation = Object.read(b) if flags & (1 << 1) else None
        
        center_icon = Object.read(b) if flags & (1 << 1) else None
        
        return AvailableReaction(reaction=reaction, title=title, static_icon=static_icon, appear_animation=appear_animation, select_animation=select_animation, activate_animation=activate_animation, effect_animation=effect_animation, inactive=inactive, premium=premium, around_animation=around_animation, center_icon=center_icon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.reaction))
        
        b.write(String(self.title))
        
        b.write(self.static_icon.write())
        
        b.write(self.appear_animation.write())
        
        b.write(self.select_animation.write())
        
        b.write(self.activate_animation.write())
        
        b.write(self.effect_animation.write())
        
        if self.around_animation is not None:
            b.write(self.around_animation.write())
        
        if self.center_icon is not None:
            b.write(self.center_icon.write())
        
        return b.getvalue()