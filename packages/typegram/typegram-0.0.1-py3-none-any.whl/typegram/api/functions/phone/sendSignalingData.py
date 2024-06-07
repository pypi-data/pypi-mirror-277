
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



class SendSignalingData(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FF7A9383``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        data (``bytes``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "data"]

    ID = 0xff7a9383
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", data: bytes) -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendSignalingData":
        # No flags
        
        peer = Object.read(b)
        
        data = Bytes.read(b)
        
        return SendSignalingData(peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.data))
        
        return b.getvalue()