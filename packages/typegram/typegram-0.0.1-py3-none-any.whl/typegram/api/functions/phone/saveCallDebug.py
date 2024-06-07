
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



class SaveCallDebug(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``277ADD7E``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        debug (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "debug"]

    ID = 0x277add7e
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", debug: "ayiin.DataJSON") -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.debug = debug  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveCallDebug":
        # No flags
        
        peer = Object.read(b)
        
        debug = Object.read(b)
        
        return SaveCallDebug(peer=peer, debug=debug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.debug.write())
        
        return b.getvalue()