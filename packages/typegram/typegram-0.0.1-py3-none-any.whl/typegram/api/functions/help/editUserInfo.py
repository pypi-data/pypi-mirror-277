
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



class EditUserInfo(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``66B91B70``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        message (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
    Returns:
        :obj:`help.UserInfo<typegram.api.ayiin.help.UserInfo>`
    """

    __slots__: List[str] = ["user_id", "message", "entities"]

    ID = 0x66b91b70
    QUALNAME = "functions.functionshelp.UserInfo"

    def __init__(self, *, user_id: "ayiin.InputUser", message: str, entities: List["ayiin.MessageEntity"]) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.message = message  # string
        
                self.entities = entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditUserInfo":
        # No flags
        
        user_id = Object.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b)
        
        return EditUserInfo(user_id=user_id, message=message, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(String(self.message))
        
        b.write(Vector(self.entities))
        
        return b.getvalue()