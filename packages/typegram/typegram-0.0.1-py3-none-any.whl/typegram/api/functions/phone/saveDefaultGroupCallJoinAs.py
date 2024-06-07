
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



class SaveDefaultGroupCallJoinAs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``575E1F8C``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        join_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "join_as"]

    ID = 0x575e1f8c
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", join_as: "ayiin.InputPeer") -> None:
        
                self.peer = peer  # InputPeer
        
                self.join_as = join_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDefaultGroupCallJoinAs":
        # No flags
        
        peer = Object.read(b)
        
        join_as = Object.read(b)
        
        return SaveDefaultGroupCallJoinAs(peer=peer, join_as=join_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.join_as.write())
        
        return b.getvalue()