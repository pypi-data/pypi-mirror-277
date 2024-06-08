
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



class AvailableEffects(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.AvailableEffects`.

    Details:
        - Layer: ``181``
        - ID: ``BDDB616E``

hash (``int`` ``32-bit``):
                    N/A
                
        effects (List of :obj:`AvailableEffect<typegram.api.ayiin.AvailableEffect>`):
                    N/A
                
        documents (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAvailableEffects
    """

    __slots__: List[str] = ["hash", "effects", "documents"]

    ID = 0xbddb616e
    QUALNAME = "types.messages.availableEffects"

    def __init__(self, *, hash: int, effects: List["api.ayiin.AvailableEffect"], documents: List["api.ayiin.Document"]) -> None:
        
                self.hash = hash  # int
        
                self.effects = effects  # AvailableEffect
        
                self.documents = documents  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableEffects":
        # No flags
        
        hash = Int.read(b)
        
        effects = Object.read(b)
        
        documents = Object.read(b)
        
        return AvailableEffects(hash=hash, effects=effects, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.effects))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()