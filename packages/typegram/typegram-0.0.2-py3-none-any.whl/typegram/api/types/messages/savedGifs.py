
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



class SavedGifs(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SavedGifs`.

    Details:
        - Layer: ``181``
        - ID: ``84A02A0D``

hash (``int`` ``64-bit``):
                    N/A
                
        gifs (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getSavedGifs
    """

    __slots__: List[str] = ["hash", "gifs"]

    ID = 0x84a02a0d
    QUALNAME = "types.messages.savedGifs"

    def __init__(self, *, hash: int, gifs: List["api.ayiin.Document"]) -> None:
        
                self.hash = hash  # long
        
                self.gifs = gifs  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedGifs":
        # No flags
        
        hash = Long.read(b)
        
        gifs = Object.read(b)
        
        return SavedGifs(hash=hash, gifs=gifs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.gifs))
        
        return b.getvalue()