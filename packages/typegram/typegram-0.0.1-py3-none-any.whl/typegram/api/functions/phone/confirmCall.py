
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



class ConfirmCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2EFE1722``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        g_a (``bytes``):
                    N/A
                
        key_fingerprint (``int`` ``64-bit``):
                    N/A
                
        protocol (:obj:`PhoneCallProtocol<typegram.api.ayiin.PhoneCallProtocol>`):
                    N/A
                
    Returns:
        :obj:`phone.PhoneCall<typegram.api.ayiin.phone.PhoneCall>`
    """

    __slots__: List[str] = ["peer", "g_a", "key_fingerprint", "protocol"]

    ID = 0x2efe1722
    QUALNAME = "functions.functionsphone.PhoneCall"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", g_a: bytes, key_fingerprint: int, protocol: "ayiin.PhoneCallProtocol") -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.g_a = g_a  # bytes
        
                self.key_fingerprint = key_fingerprint  # long
        
                self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfirmCall":
        # No flags
        
        peer = Object.read(b)
        
        g_a = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = Object.read(b)
        
        return ConfirmCall(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_a))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        return b.getvalue()