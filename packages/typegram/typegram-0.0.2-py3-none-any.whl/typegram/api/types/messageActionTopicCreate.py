
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



class MessageActionTopicCreate(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``D999256``

title (``str``):
                    N/A
                
        icon_color (``int`` ``32-bit``):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["title", "icon_color", "icon_emoji_id"]

    ID = 0xd999256
    QUALNAME = "types.messageActionTopicCreate"

    def __init__(self, *, title: str, icon_color: int, icon_emoji_id: Optional[int] = None) -> None:
        
                self.title = title  # string
        
                self.icon_color = icon_color  # int
        
                self.icon_emoji_id = icon_emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTopicCreate":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b)
        
        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return MessageActionTopicCreate(title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        return b.getvalue()