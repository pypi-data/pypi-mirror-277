
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



class GetUserBoosts(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``39854D1F``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`premium.BoostsList<typegram.api.ayiin.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "user_id"]

    ID = 0x39854d1f
    QUALNAME = "functions.functionspremium.BoostsList"

    def __init__(self, *, peer: "ayiin.InputPeer", user_id: "ayiin.InputUser") -> None:
        
                self.peer = peer  # InputPeer
        
                self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUserBoosts":
        # No flags
        
        peer = Object.read(b)
        
        user_id = Object.read(b)
        
        return GetUserBoosts(peer=peer, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()