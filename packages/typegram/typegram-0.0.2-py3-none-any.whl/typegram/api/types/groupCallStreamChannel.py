
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



class GroupCallStreamChannel(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GroupCallStreamChannel`.

    Details:
        - Layer: ``181``
        - ID: ``80EB48AF``

channel (``int`` ``32-bit``):
                    N/A
                
        scale (``int`` ``32-bit``):
                    N/A
                
        last_timestamp_ms (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel", "scale", "last_timestamp_ms"]

    ID = 0x80eb48af
    QUALNAME = "types.groupCallStreamChannel"

    def __init__(self, *, channel: int, scale: int, last_timestamp_ms: int) -> None:
        
                self.channel = channel  # int
        
                self.scale = scale  # int
        
                self.last_timestamp_ms = last_timestamp_ms  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannel":
        # No flags
        
        channel = Int.read(b)
        
        scale = Int.read(b)
        
        last_timestamp_ms = Long.read(b)
        
        return GroupCallStreamChannel(channel=channel, scale=scale, last_timestamp_ms=last_timestamp_ms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.channel))
        
        b.write(Int(self.scale))
        
        b.write(Long(self.last_timestamp_ms))
        
        return b.getvalue()