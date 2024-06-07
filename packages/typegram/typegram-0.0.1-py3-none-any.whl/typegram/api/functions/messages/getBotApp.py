
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



class GetBotApp(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``34FDC5C3``

app (:obj:`InputBotApp<typegram.api.ayiin.InputBotApp>`):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.BotApp<typegram.api.ayiin.messages.BotApp>`
    """

    __slots__: List[str] = ["app", "hash"]

    ID = 0x34fdc5c3
    QUALNAME = "functions.functionsmessages.BotApp"

    def __init__(self, *, app: "ayiin.InputBotApp", hash: int) -> None:
        
                self.app = app  # InputBotApp
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotApp":
        # No flags
        
        app = Object.read(b)
        
        hash = Long.read(b)
        
        return GetBotApp(app=app, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.app.write())
        
        b.write(Long(self.hash))
        
        return b.getvalue()