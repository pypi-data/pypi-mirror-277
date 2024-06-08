
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



class UpdateBotCallbackQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B9CFC48D``

query_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        chat_instance (``int`` ``64-bit``):
                    N/A
                
        data (``bytes``, *optional*):
                    N/A
                
        game_short_name (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["query_id", "user_id", "peer", "msg_id", "chat_instance", "data", "game_short_name"]

    ID = 0xb9cfc48d
    QUALNAME = "types.updateBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, peer: "api.ayiin.Peer", msg_id: int, chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.user_id = user_id  # long
        
                self.peer = peer  # Peer
        
                self.msg_id = msg_id  # int
        
                self.chat_instance = chat_instance  # long
        
                self.data = data  # bytes
        
                self.game_short_name = game_short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotCallbackQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        chat_instance = Long.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        game_short_name = String.read(b) if flags & (1 << 1) else None
        return UpdateBotCallbackQuery(query_id=query_id, user_id=user_id, peer=peer, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.chat_instance))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.game_short_name is not None:
            b.write(String(self.game_short_name))
        
        return b.getvalue()