
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



class GetExportedChatInvites(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A2B5A3F6``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        admin_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        revoked (``bool``, *optional*):
                    N/A
                
        offset_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        offset_link (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.ExportedChatInvites<typegram.api.ayiin.messages.ExportedChatInvites>`
    """

    __slots__: List[str] = ["peer", "admin_id", "limit", "revoked", "offset_date", "offset_link"]

    ID = 0xa2b5a3f6
    QUALNAME = "functions.functionsmessages.ExportedChatInvites"

    def __init__(self, *, peer: "ayiin.InputPeer", admin_id: "ayiin.InputUser", limit: int, revoked: Optional[bool] = None, offset_date: Optional[int] = None, offset_link: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.admin_id = admin_id  # InputUser
        
                self.limit = limit  # int
        
                self.revoked = revoked  # true
        
                self.offset_date = offset_date  # int
        
                self.offset_link = offset_link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetExportedChatInvites":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 3) else False
        peer = Object.read(b)
        
        admin_id = Object.read(b)
        
        offset_date = Int.read(b) if flags & (1 << 2) else None
        offset_link = String.read(b) if flags & (1 << 2) else None
        limit = Int.read(b)
        
        return GetExportedChatInvites(peer=peer, admin_id=admin_id, limit=limit, revoked=revoked, offset_date=offset_date, offset_link=offset_link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.admin_id.write())
        
        if self.offset_date is not None:
            b.write(Int(self.offset_date))
        
        if self.offset_link is not None:
            b.write(String(self.offset_link))
        
        b.write(Int(self.limit))
        
        return b.getvalue()