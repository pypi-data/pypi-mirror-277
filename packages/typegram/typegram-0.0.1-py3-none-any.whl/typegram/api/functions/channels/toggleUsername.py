
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



class ToggleUsername(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``50F24105``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        username (``str``):
                    N/A
                
        active (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "username", "active"]

    ID = 0x50f24105
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", username: str, active: bool) -> None:
        
                self.channel = channel  # InputChannel
        
                self.username = username  # string
        
                self.active = active  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleUsername":
        # No flags
        
        channel = Object.read(b)
        
        username = String.read(b)
        
        active = Bool.read(b)
        
        return ToggleUsername(channel=channel, username=username, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(String(self.username))
        
        b.write(Bool(self.active))
        
        return b.getvalue()