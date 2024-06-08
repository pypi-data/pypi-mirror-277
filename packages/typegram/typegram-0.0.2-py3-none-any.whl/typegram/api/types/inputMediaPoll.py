
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



class InputMediaPoll(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``F94E5F1``

poll (:obj:`Poll<typegram.api.ayiin.Poll>`):
                    N/A
                
        correct_answers (List of ``bytes``, *optional*):
                    N/A
                
        solution (``str``, *optional*):
                    N/A
                
        solution_entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["poll", "correct_answers", "solution", "solution_entities"]

    ID = 0xf94e5f1
    QUALNAME = "types.inputMediaPoll"

    def __init__(self, *, poll: "api.ayiin.Poll", correct_answers: Optional[List[bytes]] = None, solution: Optional[str] = None, solution_entities: Optional[List["api.ayiin.MessageEntity"]] = None) -> None:
        
                self.poll = poll  # Poll
        
                self.correct_answers = correct_answers  # bytes
        
                self.solution = solution  # string
        
                self.solution_entities = solution_entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPoll":
        
        flags = Int.read(b)
        
        poll = Object.read(b)
        
        correct_answers = Object.read(b, Bytes) if flags & (1 << 0) else []
        
        solution = String.read(b) if flags & (1 << 1) else None
        solution_entities = Object.read(b) if flags & (1 << 1) else []
        
        return InputMediaPoll(poll=poll, correct_answers=correct_answers, solution=solution, solution_entities=solution_entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        if self.correct_answers is not None:
            b.write(Vector(self.correct_answers, Bytes))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()