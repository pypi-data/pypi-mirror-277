
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



class UpdateChannel(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``635B4C09``

channel_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id"]

    ID = 0x635b4c09
    QUALNAME = "types.updateChannel"

    def __init__(self, *, channel_id: int) -> None:
        
                self.channel_id = channel_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannel":
        # No flags
        
        channel_id = Long.read(b)
        
        return UpdateChannel(channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        return b.getvalue()