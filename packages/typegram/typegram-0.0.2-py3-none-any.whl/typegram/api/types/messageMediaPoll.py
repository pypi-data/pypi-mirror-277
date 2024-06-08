
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



class MessageMediaPoll(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``4BD6E798``

poll (:obj:`Poll<typegram.api.ayiin.Poll>`):
                    N/A
                
        results (:obj:`PollResults<typegram.api.ayiin.PollResults>`):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getWebPagePreview
            messages.uploadMedia
            messages.uploadImportedMedia
    """

    __slots__: List[str] = ["poll", "results"]

    ID = 0x4bd6e798
    QUALNAME = "types.messageMediaPoll"

    def __init__(self, *, poll: "api.ayiin.Poll", results: "api.ayiin.PollResults") -> None:
        
                self.poll = poll  # Poll
        
                self.results = results  # PollResults

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaPoll":
        # No flags
        
        poll = Object.read(b)
        
        results = Object.read(b)
        
        return MessageMediaPoll(poll=poll, results=results)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()