
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



class GetBotCallbackAnswer(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9342CA07``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        game (``bool``, *optional*):
                    N/A
                
        data (``bytes``, *optional*):
                    N/A
                
        password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.BotCallbackAnswer<typegram.api.ayiin.messages.BotCallbackAnswer>`
    """

    __slots__: List[str] = ["peer", "msg_id", "game", "data", "password"]

    ID = 0x9342ca07
    QUALNAME = "functions.functionsmessages.BotCallbackAnswer"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, game: Optional[bool] = None, data: Optional[bytes] = None, password: "ayiin.InputCheckPasswordSRP" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.game = game  # true
        
                self.data = data  # bytes
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotCallbackAnswer":
        
        flags = Int.read(b)
        
        game = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        password = Object.read(b) if flags & (1 << 2) else None
        
        return GetBotCallbackAnswer(peer=peer, msg_id=msg_id, game=game, data=data, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.password is not None:
            b.write(self.password.write())
        
        return b.getvalue()