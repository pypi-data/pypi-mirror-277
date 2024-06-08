
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



class UpdatePeerBlocked(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``EBE07752``

peer_id (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        blocked (``bool``, *optional*):
                    N/A
                
        blocked_my_stories_from (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer_id", "blocked", "blocked_my_stories_from"]

    ID = 0xebe07752
    QUALNAME = "types.updatePeerBlocked"

    def __init__(self, *, peer_id: "api.ayiin.Peer", blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None) -> None:
        
                self.peer_id = peer_id  # Peer
        
                self.blocked = blocked  # true
        
                self.blocked_my_stories_from = blocked_my_stories_from  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePeerBlocked":
        
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        blocked_my_stories_from = True if flags & (1 << 1) else False
        peer_id = Object.read(b)
        
        return UpdatePeerBlocked(peer_id=peer_id, blocked=blocked, blocked_my_stories_from=blocked_my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        return b.getvalue()