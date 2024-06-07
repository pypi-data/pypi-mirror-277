
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



class GetMessageEditData(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FDA68D36``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.MessageEditData<typegram.api.ayiin.messages.MessageEditData>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0xfda68d36
    QUALNAME = "functions.functionsmessages.MessageEditData"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageEditData":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        return GetMessageEditData(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()