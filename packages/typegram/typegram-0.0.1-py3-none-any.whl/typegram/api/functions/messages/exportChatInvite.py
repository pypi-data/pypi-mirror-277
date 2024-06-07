
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



class ExportChatInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A02CE5D5``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        legacy_revoke_permanent (``bool``, *optional*):
                    N/A
                
        request_needed (``bool``, *optional*):
                    N/A
                
        expire_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        usage_limit (``int`` ``32-bit``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "legacy_revoke_permanent", "request_needed", "expire_date", "usage_limit", "title"]

    ID = 0xa02ce5d5
    QUALNAME = "functions.functions.ExportedChatInvite"

    def __init__(self, *, peer: "ayiin.InputPeer", legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, title: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.legacy_revoke_permanent = legacy_revoke_permanent  # true
        
                self.request_needed = request_needed  # true
        
                self.expire_date = expire_date  # int
        
                self.usage_limit = usage_limit  # int
        
                self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportChatInvite":
        
        flags = Int.read(b)
        
        legacy_revoke_permanent = True if flags & (1 << 2) else False
        request_needed = True if flags & (1 << 3) else False
        peer = Object.read(b)
        
        expire_date = Int.read(b) if flags & (1 << 0) else None
        usage_limit = Int.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 4) else None
        return ExportChatInvite(peer=peer, legacy_revoke_permanent=legacy_revoke_permanent, request_needed=request_needed, expire_date=expire_date, usage_limit=usage_limit, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()