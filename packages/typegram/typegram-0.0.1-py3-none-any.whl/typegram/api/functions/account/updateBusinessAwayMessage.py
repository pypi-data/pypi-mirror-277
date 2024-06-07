
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

from typegram.api import ayiin, functions
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class UpdateBusinessAwayMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A26A7FA5``

message (:obj:`InputBusinessAwayMessage<typegram.api.ayiin.InputBusinessAwayMessage>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["message"]

    ID = 0xa26a7fa5
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, message: "ayiin.InputBusinessAwayMessage" = None) -> None:
        
                self.message = message  # InputBusinessAwayMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessAwayMessage":
        
        flags = Int.read(b)
        
        message = Object.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessAwayMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()