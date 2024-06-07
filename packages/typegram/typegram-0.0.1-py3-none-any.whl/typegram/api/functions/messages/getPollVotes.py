
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



class GetPollVotes(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B86E380E``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        option (``bytes``, *optional*):
                    N/A
                
        offset (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.VotesList<typegram.api.ayiin.messages.VotesList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "option", "offset"]

    ID = 0xb86e380e
    QUALNAME = "functions.functionsmessages.VotesList"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, limit: int, option: Optional[bytes] = None, offset: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.limit = limit  # int
        
                self.option = option  # bytes
        
                self.offset = offset  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPollVotes":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        option = Bytes.read(b) if flags & (1 << 0) else None
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetPollVotes(peer=peer, id=id, limit=limit, option=option, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.option is not None:
            b.write(Bytes(self.option))
        
        if self.offset is not None:
            b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()