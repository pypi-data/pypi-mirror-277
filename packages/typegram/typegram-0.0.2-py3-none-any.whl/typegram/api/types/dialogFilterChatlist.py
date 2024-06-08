
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



class DialogFilterChatlist(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DialogFilter`.

    Details:
        - Layer: ``181``
        - ID: ``9FE28EA4``

id (``int`` ``32-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        pinned_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        include_peers (List of :obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        has_my_invites (``bool``, *optional*):
                    N/A
                
        emoticon (``str``, *optional*):
                    N/A
                
        color (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "has_my_invites", "emoticon", "color"]

    ID = 0x9fe28ea4
    QUALNAME = "types.dialogFilterChatlist"

    def __init__(self, *, id: int, title: str, pinned_peers: List["api.ayiin.InputPeer"], include_peers: List["api.ayiin.InputPeer"], has_my_invites: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None) -> None:
        
                self.id = id  # int
        
                self.title = title  # string
        
                self.pinned_peers = pinned_peers  # InputPeer
        
                self.include_peers = include_peers  # InputPeer
        
                self.has_my_invites = has_my_invites  # true
        
                self.emoticon = emoticon  # string
        
                self.color = color  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilterChatlist":
        
        flags = Int.read(b)
        
        has_my_invites = True if flags & (1 << 26) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        emoticon = String.read(b) if flags & (1 << 25) else None
        color = Int.read(b) if flags & (1 << 27) else None
        pinned_peers = Object.read(b)
        
        include_peers = Object.read(b)
        
        return DialogFilterChatlist(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, has_my_invites=has_my_invites, emoticon=emoticon, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        if self.color is not None:
            b.write(Int(self.color))
        
        b.write(Vector(self.pinned_peers))
        
        b.write(Vector(self.include_peers))
        
        return b.getvalue()