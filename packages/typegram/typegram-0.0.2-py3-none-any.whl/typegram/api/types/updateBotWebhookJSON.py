
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



class UpdateBotWebhookJSON(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``8317C0C3``

data (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    """

    __slots__: List[str] = ["data"]

    ID = 0x8317c0c3
    QUALNAME = "types.updateBotWebhookJSON"

    def __init__(self, *, data: "api.ayiin.DataJSON") -> None:
        
                self.data = data  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotWebhookJSON":
        # No flags
        
        data = Object.read(b)
        
        return UpdateBotWebhookJSON(data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.data.write())
        
        return b.getvalue()