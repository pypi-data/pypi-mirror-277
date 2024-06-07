
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



class SearchPosts(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D19F987B``

hashtag (``str``):
                    N/A
                
        offset_rate (``int`` ``32-bit``):
                    N/A
                
        offset_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        offset_id (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.Messages<typegram.api.ayiin.messages.Messages>`
    """

    __slots__: List[str] = ["hashtag", "offset_rate", "offset_peer", "offset_id", "limit"]

    ID = 0xd19f987b
    QUALNAME = "functions.functionsmessages.Messages"

    def __init__(self, *, hashtag: str, offset_rate: int, offset_peer: "ayiin.InputPeer", offset_id: int, limit: int) -> None:
        
                self.hashtag = hashtag  # string
        
                self.offset_rate = offset_rate  # int
        
                self.offset_peer = offset_peer  # InputPeer
        
                self.offset_id = offset_id  # int
        
                self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchPosts":
        # No flags
        
        hashtag = String.read(b)
        
        offset_rate = Int.read(b)
        
        offset_peer = Object.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return SearchPosts(hashtag=hashtag, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.hashtag))
        
        b.write(Int(self.offset_rate))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()