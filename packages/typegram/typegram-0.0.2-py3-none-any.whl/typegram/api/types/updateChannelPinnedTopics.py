
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



class UpdateChannelPinnedTopics(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``FE198602``

channel_id (``int`` ``64-bit``):
                    N/A
                
        order (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "order"]

    ID = 0xfe198602
    QUALNAME = "types.updateChannelPinnedTopics"

    def __init__(self, *, channel_id: int, order: Optional[List[int]] = None) -> None:
        
                self.channel_id = channel_id  # long
        
                self.order = order  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelPinnedTopics":
        
        flags = Int.read(b)
        
        channel_id = Long.read(b)
        
        order = Object.read(b, Int) if flags & (1 << 0) else []
        
        return UpdateChannelPinnedTopics(channel_id=channel_id, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.order is not None:
            b.write(Vector(self.order, Int))
        
        return b.getvalue()