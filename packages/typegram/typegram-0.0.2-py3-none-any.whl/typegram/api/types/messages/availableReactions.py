
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



class AvailableReactions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.AvailableReactions`.

    Details:
        - Layer: ``181``
        - ID: ``768E3AAD``

hash (``int`` ``32-bit``):
                    N/A
                
        reactions (List of :obj:`AvailableReaction<typegram.api.ayiin.AvailableReaction>`):
                    N/A
                
    Functions:
        This object can be returned by 27 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAvailableReactions
    """

    __slots__: List[str] = ["hash", "reactions"]

    ID = 0x768e3aad
    QUALNAME = "types.messages.availableReactions"

    def __init__(self, *, hash: int, reactions: List["api.ayiin.AvailableReaction"]) -> None:
        
                self.hash = hash  # int
        
                self.reactions = reactions  # AvailableReaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReactions":
        # No flags
        
        hash = Int.read(b)
        
        reactions = Object.read(b)
        
        return AvailableReactions(hash=hash, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.reactions))
        
        return b.getvalue()