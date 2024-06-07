
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



class DeleteHistory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B08F922A``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        max_id (``int`` ``32-bit``):
                    N/A
                
        just_clear (``bool``, *optional*):
                    N/A
                
        revoke (``bool``, *optional*):
                    N/A
                
        min_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        max_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.AffectedHistory<typegram.api.ayiin.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "max_id", "just_clear", "revoke", "min_date", "max_date"]

    ID = 0xb08f922a
    QUALNAME = "functions.functionsmessages.AffectedHistory"

    def __init__(self, *, peer: "ayiin.InputPeer", max_id: int, just_clear: Optional[bool] = None, revoke: Optional[bool] = None, min_date: Optional[int] = None, max_date: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.max_id = max_id  # int
        
                self.just_clear = just_clear  # true
        
                self.revoke = revoke  # true
        
                self.min_date = min_date  # int
        
                self.max_date = max_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteHistory":
        
        flags = Int.read(b)
        
        just_clear = True if flags & (1 << 0) else False
        revoke = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        max_id = Int.read(b)
        
        min_date = Int.read(b) if flags & (1 << 2) else None
        max_date = Int.read(b) if flags & (1 << 3) else None
        return DeleteHistory(peer=peer, max_id=max_id, just_clear=just_clear, revoke=revoke, min_date=min_date, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        if self.min_date is not None:
            b.write(Int(self.min_date))
        
        if self.max_date is not None:
            b.write(Int(self.max_date))
        
        return b.getvalue()