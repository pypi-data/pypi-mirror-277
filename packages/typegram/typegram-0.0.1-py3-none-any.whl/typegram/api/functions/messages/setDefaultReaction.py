
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



class SetDefaultReaction(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4F47A016``

reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction"]

    ID = 0x4f47a016
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, reaction: "ayiin.Reaction") -> None:
        
                self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultReaction":
        # No flags
        
        reaction = Object.read(b)
        
        return SetDefaultReaction(reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.reaction.write())
        
        return b.getvalue()