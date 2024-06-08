
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



class PhoneConnectionWebrtc(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhoneConnection`.

    Details:
        - Layer: ``181``
        - ID: ``635FE375``

id (``int`` ``64-bit``):
                    N/A
                
        ip (``str``):
                    N/A
                
        ipv6 (``str``):
                    N/A
                
        port (``int`` ``32-bit``):
                    N/A
                
        username (``str``):
                    N/A
                
        password (``str``):
                    N/A
                
        turn (``bool``, *optional*):
                    N/A
                
        stun (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "ip", "ipv6", "port", "username", "password", "turn", "stun"]

    ID = 0x635fe375
    QUALNAME = "types.phoneConnectionWebrtc"

    def __init__(self, *, id: int, ip: str, ipv6: str, port: int, username: str, password: str, turn: Optional[bool] = None, stun: Optional[bool] = None) -> None:
        
                self.id = id  # long
        
                self.ip = ip  # string
        
                self.ipv6 = ipv6  # string
        
                self.port = port  # int
        
                self.username = username  # string
        
                self.password = password  # string
        
                self.turn = turn  # true
        
                self.stun = stun  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneConnectionWebrtc":
        
        flags = Int.read(b)
        
        turn = True if flags & (1 << 0) else False
        stun = True if flags & (1 << 1) else False
        id = Long.read(b)
        
        ip = String.read(b)
        
        ipv6 = String.read(b)
        
        port = Int.read(b)
        
        username = String.read(b)
        
        password = String.read(b)
        
        return PhoneConnectionWebrtc(id=id, ip=ip, ipv6=ipv6, port=port, username=username, password=password, turn=turn, stun=stun)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.ip))
        
        b.write(String(self.ipv6))
        
        b.write(Int(self.port))
        
        b.write(String(self.username))
        
        b.write(String(self.password))
        
        return b.getvalue()