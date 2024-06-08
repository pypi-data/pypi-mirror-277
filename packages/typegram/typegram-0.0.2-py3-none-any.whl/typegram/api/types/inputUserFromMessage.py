
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



class InputUserFromMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputUser`.

    Details:
        - Layer: ``181``
        - ID: ``1DA448E2``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "msg_id", "user_id"]

    ID = 0x1da448e2
    QUALNAME = "types.inputUserFromMessage"

    def __init__(self, *, peer: "api.ayiin.InputPeer", msg_id: int, user_id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputUserFromMessage":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        user_id = Long.read(b)
        
        return InputUserFromMessage(peer=peer, msg_id=msg_id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()