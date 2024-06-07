
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



class GetTopPeers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``973478B6``

offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
        correspondents (``bool``, *optional*):
                    N/A
                
        bots_pm (``bool``, *optional*):
                    N/A
                
        bots_inline (``bool``, *optional*):
                    N/A
                
        phone_calls (``bool``, *optional*):
                    N/A
                
        forward_users (``bool``, *optional*):
                    N/A
                
        forward_chats (``bool``, *optional*):
                    N/A
                
        groups (``bool``, *optional*):
                    N/A
                
        channels (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`contacts.TopPeers<typegram.api.ayiin.contacts.TopPeers>`
    """

    __slots__: List[str] = ["offset", "limit", "hash", "correspondents", "bots_pm", "bots_inline", "phone_calls", "forward_users", "forward_chats", "groups", "channels"]

    ID = 0x973478b6
    QUALNAME = "functions.functionscontacts.TopPeers"

    def __init__(self, *, offset: int, limit: int, hash: int, correspondents: Optional[bool] = None, bots_pm: Optional[bool] = None, bots_inline: Optional[bool] = None, phone_calls: Optional[bool] = None, forward_users: Optional[bool] = None, forward_chats: Optional[bool] = None, groups: Optional[bool] = None, channels: Optional[bool] = None) -> None:
        
                self.offset = offset  # int
        
                self.limit = limit  # int
        
                self.hash = hash  # long
        
                self.correspondents = correspondents  # true
        
                self.bots_pm = bots_pm  # true
        
                self.bots_inline = bots_inline  # true
        
                self.phone_calls = phone_calls  # true
        
                self.forward_users = forward_users  # true
        
                self.forward_chats = forward_chats  # true
        
                self.groups = groups  # true
        
                self.channels = channels  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTopPeers":
        
        flags = Int.read(b)
        
        correspondents = True if flags & (1 << 0) else False
        bots_pm = True if flags & (1 << 1) else False
        bots_inline = True if flags & (1 << 2) else False
        phone_calls = True if flags & (1 << 3) else False
        forward_users = True if flags & (1 << 4) else False
        forward_chats = True if flags & (1 << 5) else False
        groups = True if flags & (1 << 10) else False
        channels = True if flags & (1 << 15) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetTopPeers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()