
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



class HighScore(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.HighScore`.

    Details:
        - Layer: ``181``
        - ID: ``73A379EB``

pos (``int`` ``32-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        score (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["pos", "user_id", "score"]

    ID = 0x73a379eb
    QUALNAME = "types.highScore"

    def __init__(self, *, pos: int, user_id: int, score: int) -> None:
        
                self.pos = pos  # int
        
                self.user_id = user_id  # long
        
                self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HighScore":
        # No flags
        
        pos = Int.read(b)
        
        user_id = Long.read(b)
        
        score = Int.read(b)
        
        return HighScore(pos=pos, user_id=user_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pos))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.score))
        
        return b.getvalue()