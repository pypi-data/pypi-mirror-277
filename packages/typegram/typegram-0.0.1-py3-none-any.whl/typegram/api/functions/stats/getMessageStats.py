
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



class GetMessageStats(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B6E0A3F5``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`stats.MessageStats<typegram.api.ayiin.stats.MessageStats>`
    """

    __slots__: List[str] = ["channel", "msg_id", "dark"]

    ID = 0xb6e0a3f5
    QUALNAME = "functions.functionsstats.MessageStats"

    def __init__(self, *, channel: "ayiin.InputChannel", msg_id: int, dark: Optional[bool] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.msg_id = msg_id  # int
        
                self.dark = dark  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = Object.read(b)
        
        msg_id = Int.read(b)
        
        return GetMessageStats(channel=channel, msg_id=msg_id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()