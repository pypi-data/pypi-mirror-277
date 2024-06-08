
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



class InputMessagesFilterPhoneCalls(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessagesFilter`.

    Details:
        - Layer: ``181``
        - ID: ``80C99768``

missed (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["missed"]

    ID = 0x80c99768
    QUALNAME = "types.inputMessagesFilterPhoneCalls"

    def __init__(self, *, missed: Optional[bool] = None) -> None:
        
                self.missed = missed  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMessagesFilterPhoneCalls":
        
        flags = Int.read(b)
        
        missed = True if flags & (1 << 0) else False
        return InputMessagesFilterPhoneCalls(missed=missed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()