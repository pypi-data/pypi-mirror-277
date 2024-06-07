
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



class GetGameHighScores(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E822649D``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`messages.HighScores<typegram.api.ayiin.messages.HighScores>`
    """

    __slots__: List[str] = ["peer", "id", "user_id"]

    ID = 0xe822649d
    QUALNAME = "functions.functionsmessages.HighScores"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, user_id: "ayiin.InputUser") -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGameHighScores":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        user_id = Object.read(b)
        
        return GetGameHighScores(peer=peer, id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.user_id.write())
        
        return b.getvalue()