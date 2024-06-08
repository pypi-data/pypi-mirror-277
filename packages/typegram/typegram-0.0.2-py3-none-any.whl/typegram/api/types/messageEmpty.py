
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



class MessageEmpty(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Message`.

    Details:
        - Layer: ``181``
        - ID: ``90A6CA84``

id (``int`` ``32-bit``):
                    N/A
                
        peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "peer_id"]

    ID = 0x90a6ca84
    QUALNAME = "types.messageEmpty"

    def __init__(self, *, id: int, peer_id: "api.ayiin.Peer" = None) -> None:
        
                self.id = id  # int
        
                self.peer_id = peer_id  # Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEmpty":
        
        flags = Int.read(b)
        
        id = Int.read(b)
        
        peer_id = Object.read(b) if flags & (1 << 0) else None
        
        return MessageEmpty(id=id, peer_id=peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.peer_id is not None:
            b.write(self.peer_id.write())
        
        return b.getvalue()