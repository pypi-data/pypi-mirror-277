
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



class SaveAutoSaveSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D69B8361``

settings (:obj:`AutoSaveSettings<typegram.api.ayiin.AutoSaveSettings>`):
                    N/A
                
        users (``bool``, *optional*):
                    N/A
                
        chats (``bool``, *optional*):
                    N/A
                
        broadcasts (``bool``, *optional*):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["settings", "users", "chats", "broadcasts", "peer"]

    ID = 0xd69b8361
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, settings: "ayiin.AutoSaveSettings", users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: "ayiin.InputPeer" = None) -> None:
        
                self.settings = settings  # AutoSaveSettings
        
                self.users = users  # true
        
                self.chats = chats  # true
        
                self.broadcasts = broadcasts  # true
        
                self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAutoSaveSettings":
        
        flags = Int.read(b)
        
        users = True if flags & (1 << 0) else False
        chats = True if flags & (1 << 1) else False
        broadcasts = True if flags & (1 << 2) else False
        peer = Object.read(b) if flags & (1 << 3) else None
        
        settings = Object.read(b)
        
        return SaveAutoSaveSettings(settings=settings, users=users, chats=chats, broadcasts=broadcasts, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()