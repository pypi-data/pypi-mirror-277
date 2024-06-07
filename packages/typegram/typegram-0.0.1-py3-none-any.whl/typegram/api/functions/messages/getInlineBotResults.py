
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



class GetInlineBotResults(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``514E999D``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        query (``str``):
                    N/A
                
        offset (``str``):
                    N/A
                
        geo_point (:obj:`InputGeoPoint<typegram.api.ayiin.InputGeoPoint>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.BotResults<typegram.api.ayiin.messages.BotResults>`
    """

    __slots__: List[str] = ["bot", "peer", "query", "offset", "geo_point"]

    ID = 0x514e999d
    QUALNAME = "functions.functionsmessages.BotResults"

    def __init__(self, *, bot: "ayiin.InputUser", peer: "ayiin.InputPeer", query: str, offset: str, geo_point: "ayiin.InputGeoPoint" = None) -> None:
        
                self.bot = bot  # InputUser
        
                self.peer = peer  # InputPeer
        
                self.query = query  # string
        
                self.offset = offset  # string
        
                self.geo_point = geo_point  # InputGeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineBotResults":
        
        flags = Int.read(b)
        
        bot = Object.read(b)
        
        peer = Object.read(b)
        
        geo_point = Object.read(b) if flags & (1 << 0) else None
        
        query = String.read(b)
        
        offset = String.read(b)
        
        return GetInlineBotResults(bot=bot, peer=peer, query=query, offset=offset, geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        b.write(String(self.query))
        
        b.write(String(self.offset))
        
        return b.getvalue()