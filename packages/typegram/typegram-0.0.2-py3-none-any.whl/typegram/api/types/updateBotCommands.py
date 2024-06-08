
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



class UpdateBotCommands(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``4D712F2E``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        bot_id (``int`` ``64-bit``):
                    N/A
                
        commands (List of :obj:`BotCommand<typegram.api.ayiin.BotCommand>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "bot_id", "commands"]

    ID = 0x4d712f2e
    QUALNAME = "types.updateBotCommands"

    def __init__(self, *, peer: "api.ayiin.Peer", bot_id: int, commands: List["api.ayiin.BotCommand"]) -> None:
        
                self.peer = peer  # Peer
        
                self.bot_id = bot_id  # long
        
                self.commands = commands  # BotCommand

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotCommands":
        # No flags
        
        peer = Object.read(b)
        
        bot_id = Long.read(b)
        
        commands = Object.read(b)
        
        return UpdateBotCommands(peer=peer, bot_id=bot_id, commands=commands)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.bot_id))
        
        b.write(Vector(self.commands))
        
        return b.getvalue()