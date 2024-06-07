
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



class GetInlineGameHighScores(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F635E1B``

id (:obj:`InputBotInlineMessageID<typegram.api.ayiin.InputBotInlineMessageID>`):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`messages.HighScores<typegram.api.ayiin.messages.HighScores>`
    """

    __slots__: List[str] = ["id", "user_id"]

    ID = 0xf635e1b
    QUALNAME = "functions.functionsmessages.HighScores"

    def __init__(self, *, id: "ayiin.InputBotInlineMessageID", user_id: "ayiin.InputUser") -> None:
        
                self.id = id  # InputBotInlineMessageID
        
                self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineGameHighScores":
        # No flags
        
        id = Object.read(b)
        
        user_id = Object.read(b)
        
        return GetInlineGameHighScores(id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()