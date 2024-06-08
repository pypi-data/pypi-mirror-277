
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



class StoryReactionPublicForward(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryReaction`.

    Details:
        - Layer: ``181``
        - ID: ``BBAB2643``

message (:obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
    """

    __slots__: List[str] = ["message"]

    ID = 0xbbab2643
    QUALNAME = "types.storyReactionPublicForward"

    def __init__(self, *, message: "api.ayiin.Message") -> None:
        
                self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionPublicForward":
        # No flags
        
        message = Object.read(b)
        
        return StoryReactionPublicForward(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.message.write())
        
        return b.getvalue()