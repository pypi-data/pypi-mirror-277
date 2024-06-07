
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



class UpdateBusinessGreetingMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``66CDAFC4``

message (:obj:`InputBusinessGreetingMessage<typegram.api.ayiin.InputBusinessGreetingMessage>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["message"]

    ID = 0x66cdafc4
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, message: "ayiin.InputBusinessGreetingMessage" = None) -> None:
        
                self.message = message  # InputBusinessGreetingMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessGreetingMessage":
        
        flags = Int.read(b)
        
        message = Object.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessGreetingMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()