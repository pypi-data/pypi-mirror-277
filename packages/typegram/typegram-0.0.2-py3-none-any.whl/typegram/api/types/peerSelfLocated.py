
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



class PeerSelfLocated(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PeerLocated`.

    Details:
        - Layer: ``181``
        - ID: ``F8EC284B``

expires (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["expires"]

    ID = 0xf8ec284b
    QUALNAME = "types.peerSelfLocated"

    def __init__(self, *, expires: int) -> None:
        
                self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSelfLocated":
        # No flags
        
        expires = Int.read(b)
        
        return PeerSelfLocated(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        return b.getvalue()