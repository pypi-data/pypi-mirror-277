
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



class UpdateMessagePoll(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``ACA1657B``

poll_id (``int`` ``64-bit``):
                    N/A
                
        results (:obj:`PollResults<typegram.api.ayiin.PollResults>`):
                    N/A
                
        poll (:obj:`Poll<typegram.api.ayiin.Poll>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["poll_id", "results", "poll"]

    ID = 0xaca1657b
    QUALNAME = "types.updateMessagePoll"

    def __init__(self, *, poll_id: int, results: "api.ayiin.PollResults", poll: "api.ayiin.Poll" = None) -> None:
        
                self.poll_id = poll_id  # long
        
                self.results = results  # PollResults
        
                self.poll = poll  # Poll

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessagePoll":
        
        flags = Int.read(b)
        
        poll_id = Long.read(b)
        
        poll = Object.read(b) if flags & (1 << 0) else None
        
        results = Object.read(b)
        
        return UpdateMessagePoll(poll_id=poll_id, results=results, poll=poll)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.poll_id))
        
        if self.poll is not None:
            b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()