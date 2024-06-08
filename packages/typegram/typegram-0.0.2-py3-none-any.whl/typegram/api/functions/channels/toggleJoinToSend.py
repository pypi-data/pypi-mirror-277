
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



class ToggleJoinToSend(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E4CB9580``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        enabled (``bool``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0xe4cb9580
    QUALNAME = "functions.channels.toggleJoinToSend"

    def __init__(self, *, channel: "api.ayiin.InputChannel", enabled: bool) -> None:
        
                self.channel = channel  # InputChannel
        
                self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleJoinToSend":
        # No flags
        
        channel = Object.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleJoinToSend(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()