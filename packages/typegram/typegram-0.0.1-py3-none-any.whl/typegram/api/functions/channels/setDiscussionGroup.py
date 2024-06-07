
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



class SetDiscussionGroup(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``40582BB2``

broadcast (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        group (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["broadcast", "group"]

    ID = 0x40582bb2
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, broadcast: "ayiin.InputChannel", group: "ayiin.InputChannel") -> None:
        
                self.broadcast = broadcast  # InputChannel
        
                self.group = group  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDiscussionGroup":
        # No flags
        
        broadcast = Object.read(b)
        
        group = Object.read(b)
        
        return SetDiscussionGroup(broadcast=broadcast, group=group)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.broadcast.write())
        
        b.write(self.group.write())
        
        return b.getvalue()