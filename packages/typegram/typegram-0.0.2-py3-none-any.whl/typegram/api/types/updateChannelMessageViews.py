
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



class UpdateChannelMessageViews(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F226AC08``

channel_id (``int`` ``64-bit``):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        views (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "id", "views"]

    ID = 0xf226ac08
    QUALNAME = "types.updateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        
                self.channel_id = channel_id  # long
        
                self.id = id  # int
        
                self.views = views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        # No flags
        
        channel_id = Long.read(b)
        
        id = Int.read(b)
        
        views = Int.read(b)
        
        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.id))
        
        b.write(Int(self.views))
        
        return b.getvalue()