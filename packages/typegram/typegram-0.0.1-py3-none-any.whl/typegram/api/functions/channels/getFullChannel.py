
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



class GetFullChannel(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8736A09``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
    Returns:
        :obj:`messages.ChatFull<typegram.api.ayiin.messages.ChatFull>`
    """

    __slots__: List[str] = ["channel"]

    ID = 0x8736a09
    QUALNAME = "functions.functionsmessages.ChatFull"

    def __init__(self, *, channel: "ayiin.InputChannel") -> None:
        
                self.channel = channel  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFullChannel":
        # No flags
        
        channel = Object.read(b)
        
        return GetFullChannel(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        return b.getvalue()