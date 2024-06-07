
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



class GetNotifySettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``12B3AD31``

peer (:obj:`InputNotifyPeer<typegram.api.ayiin.InputNotifyPeer>`):
                    N/A
                
    Returns:
        :obj:`PeerNotifySettings<typegram.api.ayiin.PeerNotifySettings>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0x12b3ad31
    QUALNAME = "functions.functions.PeerNotifySettings"

    def __init__(self, *, peer: "ayiin.InputNotifyPeer") -> None:
        
                self.peer = peer  # InputNotifyPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNotifySettings":
        # No flags
        
        peer = Object.read(b)
        
        return GetNotifySettings(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()