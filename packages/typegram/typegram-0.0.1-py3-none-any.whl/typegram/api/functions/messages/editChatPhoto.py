
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



class EditChatPhoto(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``35DDD674``

chat_id (``int`` ``64-bit``):
                    N/A
                
        photo (:obj:`InputChatPhoto<typegram.api.ayiin.InputChatPhoto>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["chat_id", "photo"]

    ID = 0x35ddd674
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, chat_id: int, photo: "ayiin.InputChatPhoto") -> None:
        
                self.chat_id = chat_id  # long
        
                self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatPhoto":
        # No flags
        
        chat_id = Long.read(b)
        
        photo = Object.read(b)
        
        return EditChatPhoto(chat_id=chat_id, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.photo.write())
        
        return b.getvalue()