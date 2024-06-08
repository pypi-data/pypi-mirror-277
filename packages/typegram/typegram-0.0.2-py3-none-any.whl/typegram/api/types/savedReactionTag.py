
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



class SavedReactionTag(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SavedReactionTag`.

    Details:
        - Layer: ``181``
        - ID: ``CB6FF828``

reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        count (``int`` ``32-bit``):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["reaction", "count", "title"]

    ID = 0xcb6ff828
    QUALNAME = "types.savedReactionTag"

    def __init__(self, *, reaction: "api.ayiin.Reaction", count: int, title: Optional[str] = None) -> None:
        
                self.reaction = reaction  # Reaction
        
                self.count = count  # int
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTag":
        
        flags = Int.read(b)
        
        reaction = Object.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        count = Int.read(b)
        
        return SavedReactionTag(reaction=reaction, count=count, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        b.write(Int(self.count))
        
        return b.getvalue()