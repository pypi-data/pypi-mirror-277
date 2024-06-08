
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



class SearchResultsPositions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SearchResultsPositions`.

    Details:
        - Layer: ``181``
        - ID: ``53B22BAF``

count (``int`` ``32-bit``):
                    N/A
                
        positions (List of :obj:`SearchResultsPosition<typegram.api.ayiin.SearchResultsPosition>`):
                    N/A
                
    Functions:
        This object can be returned by 31 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getSearchResultsPositions
    """

    __slots__: List[str] = ["count", "positions"]

    ID = 0x53b22baf
    QUALNAME = "types.messages.searchResultsPositions"

    def __init__(self, *, count: int, positions: List["api.ayiin.SearchResultsPosition"]) -> None:
        
                self.count = count  # int
        
                self.positions = positions  # SearchResultsPosition

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsPositions":
        # No flags
        
        count = Int.read(b)
        
        positions = Object.read(b)
        
        return SearchResultsPositions(count=count, positions=positions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.positions))
        
        return b.getvalue()