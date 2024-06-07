
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



class UpdateColor(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D8AA3671``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        for_profile (``bool``, *optional*):
                    N/A
                
        color (``int`` ``32-bit``, *optional*):
                    N/A
                
        background_emoji_id (``int`` ``64-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "for_profile", "color", "background_emoji_id"]

    ID = 0xd8aa3671
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", for_profile: Optional[bool] = None, color: Optional[int] = None, background_emoji_id: Optional[int] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.for_profile = for_profile  # true
        
                self.color = color  # int
        
                self.background_emoji_id = background_emoji_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateColor":
        
        flags = Int.read(b)
        
        for_profile = True if flags & (1 << 1) else False
        channel = Object.read(b)
        
        color = Int.read(b) if flags & (1 << 2) else None
        background_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return UpdateColor(channel=channel, for_profile=for_profile, color=color, background_emoji_id=background_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        if self.color is not None:
            b.write(Int(self.color))
        
        if self.background_emoji_id is not None:
            b.write(Long(self.background_emoji_id))
        
        return b.getvalue()