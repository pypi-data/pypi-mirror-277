
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



class SavedRingtones(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.SavedRingtones`.

    Details:
        - Layer: ``181``
        - ID: ``C1E92CC5``

hash (``int`` ``64-bit``):
                    N/A
                
        ringtones (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getSavedRingtones
    """

    __slots__: List[str] = ["hash", "ringtones"]

    ID = 0xc1e92cc5
    QUALNAME = "types.account.savedRingtones"

    def __init__(self, *, hash: int, ringtones: List["api.ayiin.Document"]) -> None:
        
                self.hash = hash  # long
        
                self.ringtones = ringtones  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedRingtones":
        # No flags
        
        hash = Long.read(b)
        
        ringtones = Object.read(b)
        
        return SavedRingtones(hash=hash, ringtones=ringtones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.ringtones))
        
        return b.getvalue()