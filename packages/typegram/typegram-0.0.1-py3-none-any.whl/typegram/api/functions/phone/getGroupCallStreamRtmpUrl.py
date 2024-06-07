
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



class GetGroupCallStreamRtmpUrl(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DEB3ABBF``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        revoke (``bool``):
                    N/A
                
    Returns:
        :obj:`phone.GroupCallStreamRtmpUrl<typegram.api.ayiin.phone.GroupCallStreamRtmpUrl>`
    """

    __slots__: List[str] = ["peer", "revoke"]

    ID = 0xdeb3abbf
    QUALNAME = "functions.functionsphone.GroupCallStreamRtmpUrl"

    def __init__(self, *, peer: "ayiin.InputPeer", revoke: bool) -> None:
        
                self.peer = peer  # InputPeer
        
                self.revoke = revoke  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamRtmpUrl":
        # No flags
        
        peer = Object.read(b)
        
        revoke = Bool.read(b)
        
        return GetGroupCallStreamRtmpUrl(peer=peer, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()