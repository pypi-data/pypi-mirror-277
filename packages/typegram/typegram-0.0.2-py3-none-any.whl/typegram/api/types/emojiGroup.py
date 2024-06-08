
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



class EmojiGroup(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiGroup`.

    Details:
        - Layer: ``181``
        - ID: ``7A9ABDA9``

title (``str``):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``):
                    N/A
                
        emoticons (List of ``str``):
                    N/A
                
    """

    __slots__: List[str] = ["title", "icon_emoji_id", "emoticons"]

    ID = 0x7a9abda9
    QUALNAME = "types.emojiGroup"

    def __init__(self, *, title: str, icon_emoji_id: int, emoticons: List[str]) -> None:
        
                self.title = title  # string
        
                self.icon_emoji_id = icon_emoji_id  # long
        
                self.emoticons = emoticons  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroup":
        # No flags
        
        title = String.read(b)
        
        icon_emoji_id = Long.read(b)
        
        emoticons = Object.read(b, String)
        
        return EmojiGroup(title=title, icon_emoji_id=icon_emoji_id, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Long(self.icon_emoji_id))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()