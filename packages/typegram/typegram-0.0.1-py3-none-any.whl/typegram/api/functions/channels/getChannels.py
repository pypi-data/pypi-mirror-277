
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



class GetChannels(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A7F6BBB``

id (List of :obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
    Returns:
        :obj:`messages.Chats<typegram.api.ayiin.messages.Chats>`
    """

    __slots__: List[str] = ["id"]

    ID = 0xa7f6bbb
    QUALNAME = "functions.functionsmessages.Chats"

    def __init__(self, *, id: List["ayiin.InputChannel"]) -> None:
        
                self.id = id  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannels":
        # No flags
        
        id = Object.read(b)
        
        return GetChannels(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()