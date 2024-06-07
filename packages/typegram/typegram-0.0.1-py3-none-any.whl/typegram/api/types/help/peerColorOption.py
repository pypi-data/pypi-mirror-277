
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



class PeerColorOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PeerColorOption`.

    Details:
        - Layer: ``181``
        - ID: ``ADEC6EBE``

color_id (``int`` ``32-bit``):
                    N/A
                
        hidden (``bool``, *optional*):
                    N/A
                
        colors (:obj:`help.PeerColorSet<typegram.api.ayiin.help.PeerColorSet>`, *optional*):
                    N/A
                
        dark_colors (:obj:`help.PeerColorSet<typegram.api.ayiin.help.PeerColorSet>`, *optional*):
                    N/A
                
        channel_min_level (``int`` ``32-bit``, *optional*):
                    N/A
                
        group_min_level (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["color_id", "hidden", "colors", "dark_colors", "channel_min_level", "group_min_level"]

    ID = 0xadec6ebe
    QUALNAME = "functions.typeshelp.PeerColorOption"

    def __init__(self, *, color_id: int, hidden: Optional[bool] = None, colors: "ayiinhelp.PeerColorSet" = None, dark_colors: "ayiinhelp.PeerColorSet" = None, channel_min_level: Optional[int] = None, group_min_level: Optional[int] = None) -> None:
        
                self.color_id = color_id  # int
        
                self.hidden = hidden  # true
        
                self.colors = colors  # help.PeerColorSet
        
                self.dark_colors = dark_colors  # help.PeerColorSet
        
                self.channel_min_level = channel_min_level  # int
        
                self.group_min_level = group_min_level  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorOption":
        
        flags = Int.read(b)
        
        hidden = True if flags & (1 << 0) else False
        color_id = Int.read(b)
        
        colors = Object.read(b) if flags & (1 << 1) else None
        
        dark_colors = Object.read(b) if flags & (1 << 2) else None
        
        channel_min_level = Int.read(b) if flags & (1 << 3) else None
        group_min_level = Int.read(b) if flags & (1 << 4) else None
        return PeerColorOption(color_id=color_id, hidden=hidden, colors=colors, dark_colors=dark_colors, channel_min_level=channel_min_level, group_min_level=group_min_level)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.color_id))
        
        if self.colors is not None:
            b.write(self.colors.write())
        
        if self.dark_colors is not None:
            b.write(self.dark_colors.write())
        
        if self.channel_min_level is not None:
            b.write(Int(self.channel_min_level))
        
        if self.group_min_level is not None:
            b.write(Int(self.group_min_level))
        
        return b.getvalue()