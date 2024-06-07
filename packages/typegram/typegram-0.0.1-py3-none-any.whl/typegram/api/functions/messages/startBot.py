
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



class StartBot(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E6DF7378``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        start_param (``str``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["bot", "peer", "random_id", "start_param"]

    ID = 0xe6df7378
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, bot: "ayiin.InputUser", peer: "ayiin.InputPeer", random_id: int, start_param: str) -> None:
        
                self.bot = bot  # InputUser
        
                self.peer = peer  # InputPeer
        
                self.random_id = random_id  # long
        
                self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StartBot":
        # No flags
        
        bot = Object.read(b)
        
        peer = Object.read(b)
        
        random_id = Long.read(b)
        
        start_param = String.read(b)
        
        return StartBot(bot=bot, peer=peer, random_id=random_id, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(String(self.start_param))
        
        return b.getvalue()