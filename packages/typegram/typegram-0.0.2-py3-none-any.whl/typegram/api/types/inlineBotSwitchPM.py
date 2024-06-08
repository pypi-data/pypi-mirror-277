
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



class InlineBotSwitchPM(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InlineBotSwitchPM`.

    Details:
        - Layer: ``181``
        - ID: ``3C20629F``

text (``str``):
                    N/A
                
        start_param (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "start_param"]

    ID = 0x3c20629f
    QUALNAME = "types.inlineBotSwitchPM"

    def __init__(self, *, text: str, start_param: str) -> None:
        
                self.text = text  # string
        
                self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InlineBotSwitchPM":
        # No flags
        
        text = String.read(b)
        
        start_param = String.read(b)
        
        return InlineBotSwitchPM(text=text, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.start_param))
        
        return b.getvalue()