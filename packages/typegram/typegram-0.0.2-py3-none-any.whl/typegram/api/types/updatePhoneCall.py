
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



class UpdatePhoneCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``AB0F6B1E``

phone_call (:obj:`PhoneCall<typegram.api.ayiin.PhoneCall>`):
                    N/A
                
    """

    __slots__: List[str] = ["phone_call"]

    ID = 0xab0f6b1e
    QUALNAME = "types.updatePhoneCall"

    def __init__(self, *, phone_call: "api.ayiin.PhoneCall") -> None:
        
                self.phone_call = phone_call  # PhoneCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePhoneCall":
        # No flags
        
        phone_call = Object.read(b)
        
        return UpdatePhoneCall(phone_call=phone_call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.phone_call.write())
        
        return b.getvalue()