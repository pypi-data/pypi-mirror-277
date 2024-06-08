
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



class InputMediaAreaVenue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``B282217F``

coordinates (:obj:`MediaAreaCoordinates<typegram.api.ayiin.MediaAreaCoordinates>`):
                    N/A
                
        query_id (``int`` ``64-bit``):
                    N/A
                
        result_id (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["coordinates", "query_id", "result_id"]

    ID = 0xb282217f
    QUALNAME = "types.inputMediaAreaVenue"

    def __init__(self, *, coordinates: "api.ayiin.MediaAreaCoordinates", query_id: int, result_id: str) -> None:
        
                self.coordinates = coordinates  # MediaAreaCoordinates
        
                self.query_id = query_id  # long
        
                self.result_id = result_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaVenue":
        # No flags
        
        coordinates = Object.read(b)
        
        query_id = Long.read(b)
        
        result_id = String.read(b)
        
        return InputMediaAreaVenue(coordinates=coordinates, query_id=query_id, result_id=result_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(Long(self.query_id))
        
        b.write(String(self.result_id))
        
        return b.getvalue()