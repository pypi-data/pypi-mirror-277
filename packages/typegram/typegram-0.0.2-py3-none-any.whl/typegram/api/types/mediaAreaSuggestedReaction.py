
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



class MediaAreaSuggestedReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``14455871``

coordinates (:obj:`MediaAreaCoordinates<typegram.api.ayiin.MediaAreaCoordinates>`):
                    N/A
                
        reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
        flipped (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["coordinates", "reaction", "dark", "flipped"]

    ID = 0x14455871
    QUALNAME = "types.mediaAreaSuggestedReaction"

    def __init__(self, *, coordinates: "api.ayiin.MediaAreaCoordinates", reaction: "api.ayiin.Reaction", dark: Optional[bool] = None, flipped: Optional[bool] = None) -> None:
        
                self.coordinates = coordinates  # MediaAreaCoordinates
        
                self.reaction = reaction  # Reaction
        
                self.dark = dark  # true
        
                self.flipped = flipped  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaSuggestedReaction":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        flipped = True if flags & (1 << 1) else False
        coordinates = Object.read(b)
        
        reaction = Object.read(b)
        
        return MediaAreaSuggestedReaction(coordinates=coordinates, reaction=reaction, dark=dark, flipped=flipped)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.coordinates.write())
        
        b.write(self.reaction.write())
        
        return b.getvalue()