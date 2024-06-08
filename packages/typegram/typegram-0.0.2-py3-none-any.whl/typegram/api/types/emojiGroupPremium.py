
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



class EmojiGroupPremium(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiGroup`.

    Details:
        - Layer: ``181``
        - ID: ``93BCF34``

title (``str``):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["title", "icon_emoji_id"]

    ID = 0x93bcf34
    QUALNAME = "types.emojiGroupPremium"

    def __init__(self, *, title: str, icon_emoji_id: int) -> None:
        
                self.title = title  # string
        
                self.icon_emoji_id = icon_emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroupPremium":
        # No flags
        
        title = String.read(b)
        
        icon_emoji_id = Long.read(b)
        
        return EmojiGroupPremium(title=title, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Long(self.icon_emoji_id))
        
        return b.getvalue()