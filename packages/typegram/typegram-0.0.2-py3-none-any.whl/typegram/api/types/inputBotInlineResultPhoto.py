
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



class InputBotInlineResultPhoto(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBotInlineResult`.

    Details:
        - Layer: ``181``
        - ID: ``A8D864A7``

id (``str``):
                    N/A
                
        type (``str``):
                    N/A
                
        photo (:obj:`InputPhoto<typegram.api.ayiin.InputPhoto>`):
                    N/A
                
        send_message (:obj:`InputBotInlineMessage<typegram.api.ayiin.InputBotInlineMessage>`):
                    N/A
                
    """

    __slots__: List[str] = ["id", "type", "photo", "send_message"]

    ID = 0xa8d864a7
    QUALNAME = "types.inputBotInlineResultPhoto"

    def __init__(self, *, id: str, type: str, photo: "api.ayiin.InputPhoto", send_message: "api.ayiin.InputBotInlineMessage") -> None:
        
                self.id = id  # string
        
                self.type = type  # string
        
                self.photo = photo  # InputPhoto
        
                self.send_message = send_message  # InputBotInlineMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultPhoto":
        # No flags
        
        id = String.read(b)
        
        type = String.read(b)
        
        photo = Object.read(b)
        
        send_message = Object.read(b)
        
        return InputBotInlineResultPhoto(id=id, type=type, photo=photo, send_message=send_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        b.write(self.photo.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()