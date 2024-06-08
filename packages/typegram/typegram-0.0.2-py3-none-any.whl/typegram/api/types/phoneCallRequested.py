
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



class PhoneCallRequested(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``14B0ED0C``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        admin_id (``int`` ``64-bit``):
                    N/A
                
        participant_id (``int`` ``64-bit``):
                    N/A
                
        g_a_hash (``bytes``):
                    N/A
                
        protocol (:obj:`PhoneCallProtocol<typegram.api.ayiin.PhoneCallProtocol>`):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_hash", "protocol", "video"]

    ID = 0x14b0ed0c
    QUALNAME = "types.phoneCallRequested"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_hash: bytes, protocol: "api.ayiin.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.date = date  # int
        
                self.admin_id = admin_id  # long
        
                self.participant_id = participant_id  # long
        
                self.g_a_hash = g_a_hash  # bytes
        
                self.protocol = protocol  # PhoneCallProtocol
        
                self.video = video  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallRequested":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = Object.read(b)
        
        return PhoneCallRequested(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()