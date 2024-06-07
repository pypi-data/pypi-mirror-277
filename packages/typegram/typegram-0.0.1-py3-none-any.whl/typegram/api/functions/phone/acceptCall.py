
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



class AcceptCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3BD2B4A0``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        g_b (``bytes``):
                    N/A
                
        protocol (:obj:`PhoneCallProtocol<typegram.api.ayiin.PhoneCallProtocol>`):
                    N/A
                
    Returns:
        :obj:`phone.PhoneCall<typegram.api.ayiin.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "g_b", "protocol"]

    ID = 0x3bd2b4a0
    QUALNAME = "functions.functionsphone.PhoneCall"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", g_b: bytes, protocol: "ayiin.PhoneCallProtocol") -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.g_b = g_b  # bytes
        
                self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptCall":
        # No flags
        
        peer = Object.read(b)
        
        g_b = Bytes.read(b)
        
        protocol = Object.read(b)
        
        return AcceptCall(peer=peer, g_b=g_b, protocol=protocol)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_b))
        
        b.write(self.protocol.write())
        
        return b.getvalue()