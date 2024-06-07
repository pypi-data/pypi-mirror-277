
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



class RequestCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``42FF96ED``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        random_id (``int`` ``32-bit``):
                    N/A
                
        g_a_hash (``bytes``):
                    N/A
                
        protocol (:obj:`PhoneCallProtocol<typegram.api.ayiin.PhoneCallProtocol>`):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`phone.PhoneCall<typegram.api.ayiin.phone.PhoneCall>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a_hash", "protocol", "video"]

    ID = 0x42ff96ed
    QUALNAME = "functions.functionsphone.PhoneCall"

    def __init__(self, *, user_id: "ayiin.InputUser", random_id: int, g_a_hash: bytes, protocol: "ayiin.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.random_id = random_id  # int
        
                self.g_a_hash = g_a_hash  # bytes
        
                self.protocol = protocol  # PhoneCallProtocol
        
                self.video = video  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestCall":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        user_id = Object.read(b)
        
        random_id = Int.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = Object.read(b)
        
        return RequestCall(user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()