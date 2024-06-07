
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



class ReadMessageContents(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``EAB5DC38``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "id"]

    ID = 0xeab5dc38
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", id: List[int]) -> None:
        
                self.channel = channel  # InputChannel
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadMessageContents":
        # No flags
        
        channel = Object.read(b)
        
        id = Object.read(b, Int)
        
        return ReadMessageContents(channel=channel, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()