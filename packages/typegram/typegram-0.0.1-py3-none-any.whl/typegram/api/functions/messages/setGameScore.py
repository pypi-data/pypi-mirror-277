
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



class SetGameScore(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8EF8ECC0``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        score (``int`` ``32-bit``):
                    N/A
                
        edit_message (``bool``, *optional*):
                    N/A
                
        force (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "user_id", "score", "edit_message", "force"]

    ID = 0x8ef8ecc0
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, user_id: "ayiin.InputUser", score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.user_id = user_id  # InputUser
        
                self.score = score  # int
        
                self.edit_message = edit_message  # true
        
                self.force = force  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetGameScore":
        
        flags = Int.read(b)
        
        edit_message = True if flags & (1 << 0) else False
        force = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        user_id = Object.read(b)
        
        score = Int.read(b)
        
        return SetGameScore(peer=peer, id=id, user_id=user_id, score=score, edit_message=edit_message, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.score))
        
        return b.getvalue()