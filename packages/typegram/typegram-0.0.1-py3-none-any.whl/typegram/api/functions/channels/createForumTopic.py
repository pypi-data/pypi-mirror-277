
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



class CreateForumTopic(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F40C0224``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        title (``str``):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        icon_color (``int`` ``32-bit``, *optional*):
                    N/A
                
        icon_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        send_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "title", "random_id", "icon_color", "icon_emoji_id", "send_as"]

    ID = 0xf40c0224
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", title: str, random_id: int, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, send_as: "ayiin.InputPeer" = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.title = title  # string
        
                self.random_id = random_id  # long
        
                self.icon_color = icon_color  # int
        
                self.icon_emoji_id = icon_emoji_id  # long
        
                self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateForumTopic":
        
        flags = Int.read(b)
        
        channel = Object.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 3) else None
        random_id = Long.read(b)
        
        send_as = Object.read(b) if flags & (1 << 2) else None
        
        return CreateForumTopic(channel=channel, title=title, random_id=random_id, icon_color=icon_color, icon_emoji_id=icon_emoji_id, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(String(self.title))
        
        if self.icon_color is not None:
            b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Long(self.random_id))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()