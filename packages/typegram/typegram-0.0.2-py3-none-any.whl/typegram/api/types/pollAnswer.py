
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



class PollAnswer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PollAnswer`.

    Details:
        - Layer: ``181``
        - ID: ``FF16E2CA``

text (:obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`):
                    N/A
                
        option (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "option"]

    ID = 0xff16e2ca
    QUALNAME = "types.pollAnswer"

    def __init__(self, *, text: "api.ayiin.TextWithEntities", option: bytes) -> None:
        
                self.text = text  # TextWithEntities
        
                self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PollAnswer":
        # No flags
        
        text = Object.read(b)
        
        option = Bytes.read(b)
        
        return PollAnswer(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(Bytes(self.option))
        
        return b.getvalue()