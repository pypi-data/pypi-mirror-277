
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



class UpdateSavedReactionTag(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``60297DEC``

reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction", "title"]

    ID = 0x60297dec
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, reaction: "ayiin.Reaction", title: Optional[str] = None) -> None:
        
                self.reaction = reaction  # Reaction
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedReactionTag":
        
        flags = Int.read(b)
        
        reaction = Object.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        return UpdateSavedReactionTag(reaction=reaction, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()