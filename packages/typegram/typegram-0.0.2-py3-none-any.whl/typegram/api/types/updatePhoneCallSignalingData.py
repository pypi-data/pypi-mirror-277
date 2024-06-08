
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



class UpdatePhoneCallSignalingData(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``2661BF09``

phone_call_id (``int`` ``64-bit``):
                    N/A
                
        data (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["phone_call_id", "data"]

    ID = 0x2661bf09
    QUALNAME = "types.updatePhoneCallSignalingData"

    def __init__(self, *, phone_call_id: int, data: bytes) -> None:
        
                self.phone_call_id = phone_call_id  # long
        
                self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePhoneCallSignalingData":
        # No flags
        
        phone_call_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return UpdatePhoneCallSignalingData(phone_call_id=phone_call_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.phone_call_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()