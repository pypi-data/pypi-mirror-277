
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



class UpdateEmojiStatus(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FBD3DE6B``

emoji_status (:obj:`EmojiStatus<typegram.api.ayiin.EmojiStatus>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["emoji_status"]

    ID = 0xfbd3de6b
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, emoji_status: "ayiin.EmojiStatus") -> None:
        
                self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiStatus":
        # No flags
        
        emoji_status = Object.read(b)
        
        return UpdateEmojiStatus(emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.emoji_status.write())
        
        return b.getvalue()