
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



class ReadDiscussion(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F731A9F4``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        read_max_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "read_max_id"]

    ID = 0xf731a9f4
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", msg_id: int, read_max_id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.read_max_id = read_max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadDiscussion":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        read_max_id = Int.read(b)
        
        return ReadDiscussion(peer=peer, msg_id=msg_id, read_max_id=read_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.read_max_id))
        
        return b.getvalue()