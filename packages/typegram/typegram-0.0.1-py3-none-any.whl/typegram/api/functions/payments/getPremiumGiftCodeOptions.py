
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



class GetPremiumGiftCodeOptions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2757BA54``

boost_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        List of :obj:`PremiumGiftCodeOption<typegram.api.ayiin.PremiumGiftCodeOption>`
    """

    __slots__: List[str] = ["boost_peer"]

    ID = 0x2757ba54
    QUALNAME = "functions.functions.Vector<PremiumGiftCodeOption>"

    def __init__(self, *, boost_peer: "ayiin.InputPeer" = None) -> None:
        
                self.boost_peer = boost_peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPremiumGiftCodeOptions":
        
        flags = Int.read(b)
        
        boost_peer = Object.read(b) if flags & (1 << 0) else None
        
        return GetPremiumGiftCodeOptions(boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        return b.getvalue()