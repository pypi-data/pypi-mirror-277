
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



class PollAnswerVoters(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PollAnswerVoters`.

    Details:
        - Layer: ``181``
        - ID: ``3B6DDAD2``

option (``bytes``):
                    N/A
                
        voters (``int`` ``32-bit``):
                    N/A
                
        chosen (``bool``, *optional*):
                    N/A
                
        correct (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["option", "voters", "chosen", "correct"]

    ID = 0x3b6ddad2
    QUALNAME = "types.pollAnswerVoters"

    def __init__(self, *, option: bytes, voters: int, chosen: Optional[bool] = None, correct: Optional[bool] = None) -> None:
        
                self.option = option  # bytes
        
                self.voters = voters  # int
        
                self.chosen = chosen  # true
        
                self.correct = correct  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswerVoters":
        
        flags = Int.read(b)
        
        chosen = True if flags & (1 << 0) else False
        correct = True if flags & (1 << 1) else False
        option = Bytes.read(b)
        
        voters = Int.read(b)
        
        return PollAnswerVoters(option=option, voters=voters, chosen=chosen, correct=correct)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Bytes(self.option))
        
        b.write(Int(self.voters))
        
        return b.getvalue()