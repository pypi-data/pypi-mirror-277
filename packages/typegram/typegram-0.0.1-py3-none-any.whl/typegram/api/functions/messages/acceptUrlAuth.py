
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



class AcceptUrlAuth(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B12C7125``

write_allowed (``bool``, *optional*):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        button_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`UrlAuthResult<typegram.api.ayiin.UrlAuthResult>`
    """

    __slots__: List[str] = ["write_allowed", "peer", "msg_id", "button_id", "url"]

    ID = 0xb12c7125
    QUALNAME = "functions.functions.UrlAuthResult"

    def __init__(self, *, write_allowed: Optional[bool] = None, peer: "ayiin.InputPeer" = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None) -> None:
        
                self.write_allowed = write_allowed  # true
        
                self.peer = peer  # InputPeer
        
                self.msg_id = msg_id  # int
        
                self.button_id = button_id  # int
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptUrlAuth":
        
        flags = Int.read(b)
        
        write_allowed = True if flags & (1 << 0) else False
        peer = Object.read(b) if flags & (1 << 1) else None
        
        msg_id = Int.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b) if flags & (1 << 1) else None
        url = String.read(b) if flags & (1 << 2) else None
        return AcceptUrlAuth(write_allowed=write_allowed, peer=peer, msg_id=msg_id, button_id=button_id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.button_id is not None:
            b.write(Int(self.button_id))
        
        if self.url is not None:
            b.write(String(self.url))
        
        return b.getvalue()