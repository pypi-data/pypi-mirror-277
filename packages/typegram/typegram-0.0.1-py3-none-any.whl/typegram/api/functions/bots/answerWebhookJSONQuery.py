
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



class AnswerWebhookJSONQuery(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E6213F4D``

query_id (``int`` ``64-bit``):
                    N/A
                
        data (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "data"]

    ID = 0xe6213f4d
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, query_id: int, data: "ayiin.DataJSON") -> None:
        
                self.query_id = query_id  # long
        
                self.data = data  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AnswerWebhookJSONQuery":
        # No flags
        
        query_id = Long.read(b)
        
        data = Object.read(b)
        
        return AnswerWebhookJSONQuery(query_id=query_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.data.write())
        
        return b.getvalue()