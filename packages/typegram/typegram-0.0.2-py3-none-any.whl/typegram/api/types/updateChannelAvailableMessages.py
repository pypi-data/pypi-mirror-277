
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



class UpdateChannelAvailableMessages(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B23FC698``

channel_id (``int`` ``64-bit``):
                    N/A
                
        available_min_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["channel_id", "available_min_id"]

    ID = 0xb23fc698
    QUALNAME = "types.updateChannelAvailableMessages"

    def __init__(self, *, channel_id: int, available_min_id: int) -> None:
        
                self.channel_id = channel_id  # long
        
                self.available_min_id = available_min_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelAvailableMessages":
        # No flags
        
        channel_id = Long.read(b)
        
        available_min_id = Int.read(b)
        
        return UpdateChannelAvailableMessages(channel_id=channel_id, available_min_id=available_min_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.available_min_id))
        
        return b.getvalue()