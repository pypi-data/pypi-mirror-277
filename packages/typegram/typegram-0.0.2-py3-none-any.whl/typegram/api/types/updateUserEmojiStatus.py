
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



class UpdateUserEmojiStatus(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``28373599``

user_id (``int`` ``64-bit``):
                    N/A
                
        emoji_status (:obj:`EmojiStatus<typegram.api.ayiin.EmojiStatus>`):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "emoji_status"]

    ID = 0x28373599
    QUALNAME = "types.updateUserEmojiStatus"

    def __init__(self, *, user_id: int, emoji_status: "api.ayiin.EmojiStatus") -> None:
        
                self.user_id = user_id  # long
        
                self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserEmojiStatus":
        # No flags
        
        user_id = Long.read(b)
        
        emoji_status = Object.read(b)
        
        return UpdateUserEmojiStatus(user_id=user_id, emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.emoji_status.write())
        
        return b.getvalue()