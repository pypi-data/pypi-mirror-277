
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



class RequestPeerTypeChat(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestPeerType`.

    Details:
        - Layer: ``181``
        - ID: ``C9F06E1B``

creator (``bool``, *optional*):
                    N/A
                
        bot_participant (``bool``, *optional*):
                    N/A
                
        has_username (``bool``, *optional*):
                    N/A
                
        forum (``bool``, *optional*):
                    N/A
                
        user_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
        bot_admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["creator", "bot_participant", "has_username", "forum", "user_admin_rights", "bot_admin_rights"]

    ID = 0xc9f06e1b
    QUALNAME = "types.requestPeerTypeChat"

    def __init__(self, *, creator: Optional[bool] = None, bot_participant: Optional[bool] = None, has_username: Optional[bool] = None, forum: Optional[bool] = None, user_admin_rights: "api.ayiin.ChatAdminRights" = None, bot_admin_rights: "api.ayiin.ChatAdminRights" = None) -> None:
        
                self.creator = creator  # true
        
                self.bot_participant = bot_participant  # true
        
                self.has_username = has_username  # Bool
        
                self.forum = forum  # Bool
        
                self.user_admin_rights = user_admin_rights  # ChatAdminRights
        
                self.bot_admin_rights = bot_admin_rights  # ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeChat":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        bot_participant = True if flags & (1 << 5) else False
        has_username = Bool.read(b) if flags & (1 << 3) else None
        forum = Bool.read(b) if flags & (1 << 4) else None
        user_admin_rights = Object.read(b) if flags & (1 << 1) else None
        
        bot_admin_rights = Object.read(b) if flags & (1 << 2) else None
        
        return RequestPeerTypeChat(creator=creator, bot_participant=bot_participant, has_username=has_username, forum=forum, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.has_username is not None:
            b.write(Bool(self.has_username))
        
        if self.forum is not None:
            b.write(Bool(self.forum))
        
        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())
        
        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())
        
        return b.getvalue()