
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



class GetMessagePublicForwards(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``5F150144``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        offset (``str``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`stats.PublicForwards<typegram.api.ayiin.stats.PublicForwards>`
    """

    __slots__: List[str] = ["channel", "msg_id", "offset", "limit"]

    ID = 0x5f150144
    QUALNAME = "functions.functionsstats.PublicForwards"

    def __init__(self, *, channel: "ayiin.InputChannel", msg_id: int, offset: str, limit: int) -> None:
        
                self.channel = channel  # InputChannel
        
                self.msg_id = msg_id  # int
        
                self.offset = offset  # string
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessagePublicForwards":
        # No flags
        
        channel = Object.read(b)
        
        msg_id = Int.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetMessagePublicForwards(channel=channel, msg_id=msg_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()