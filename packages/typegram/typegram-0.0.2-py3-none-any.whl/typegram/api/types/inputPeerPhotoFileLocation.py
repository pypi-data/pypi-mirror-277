
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



class InputPeerPhotoFileLocation(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``37257E99``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        photo_id (``int`` ``64-bit``):
                    N/A
                
        big (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "photo_id", "big"]

    ID = 0x37257e99
    QUALNAME = "types.inputPeerPhotoFileLocation"

    def __init__(self, *, peer: "api.ayiin.InputPeer", photo_id: int, big: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.photo_id = photo_id  # long
        
                self.big = big  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerPhotoFileLocation":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        photo_id = Long.read(b)
        
        return InputPeerPhotoFileLocation(peer=peer, photo_id=photo_id, big=big)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.photo_id))
        
        return b.getvalue()