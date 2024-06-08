
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



class UpdateBotDeleteBusinessMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``A02A982E``

connection_id (``str``):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        messages (List of ``int`` ``32-bit``):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["connection_id", "peer", "messages", "qts"]

    ID = 0xa02a982e
    QUALNAME = "types.updateBotDeleteBusinessMessage"

    def __init__(self, *, connection_id: str, peer: "api.ayiin.Peer", messages: List[int], qts: int) -> None:
        
                self.connection_id = connection_id  # string
        
                self.peer = peer  # Peer
        
                self.messages = messages  # int
        
                self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotDeleteBusinessMessage":
        # No flags
        
        connection_id = String.read(b)
        
        peer = Object.read(b)
        
        messages = Object.read(b, Int)
        
        qts = Int.read(b)
        
        return UpdateBotDeleteBusinessMessage(connection_id=connection_id, peer=peer, messages=messages, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.connection_id))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.qts))
        
        return b.getvalue()