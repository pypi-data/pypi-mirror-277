
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



class EditCreator(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8F38CD1F``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "user_id", "password"]

    ID = 0x8f38cd1f
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", user_id: "ayiin.InputUser", password: "ayiin.InputCheckPasswordSRP") -> None:
        
                self.channel = channel  # InputChannel
        
                self.user_id = user_id  # InputUser
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditCreator":
        # No flags
        
        channel = Object.read(b)
        
        user_id = Object.read(b)
        
        password = Object.read(b)
        
        return EditCreator(channel=channel, user_id=user_id, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.user_id.write())
        
        b.write(self.password.write())
        
        return b.getvalue()