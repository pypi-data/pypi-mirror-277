
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



class BotInlineMessageMediaVenue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``8A86659C``

geo (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`):
                    N/A
                
        title (``str``):
                    N/A
                
        address (``str``):
                    N/A
                
        provider (``str``):
                    N/A
                
        venue_id (``str``):
                    N/A
                
        venue_type (``str``):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["geo", "title", "address", "provider", "venue_id", "venue_type", "reply_markup"]

    ID = 0x8a86659c
    QUALNAME = "types.botInlineMessageMediaVenue"

    def __init__(self, *, geo: "api.ayiin.GeoPoint", title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: "api.ayiin.ReplyMarkup" = None) -> None:
        
                self.geo = geo  # GeoPoint
        
                self.title = title  # string
        
                self.address = address  # string
        
                self.provider = provider  # string
        
                self.venue_id = venue_id  # string
        
                self.venue_type = venue_type  # string
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaVenue":
        
        flags = Int.read(b)
        
        geo = Object.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaVenue(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.geo.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()