
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



class AutoSaveSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.AutoSaveSettings`.

    Details:
        - Layer: ``181``
        - ID: ``4C3E069D``

users_settings (:obj:`AutoSaveSettings<typegram.api.ayiin.AutoSaveSettings>`):
                    N/A
                
        chats_settings (:obj:`AutoSaveSettings<typegram.api.ayiin.AutoSaveSettings>`):
                    N/A
                
        broadcasts_settings (:obj:`AutoSaveSettings<typegram.api.ayiin.AutoSaveSettings>`):
                    N/A
                
        exceptions (List of :obj:`AutoSaveException<typegram.api.ayiin.AutoSaveException>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    """

    __slots__: List[str] = ["users_settings", "chats_settings", "broadcasts_settings", "exceptions", "chats", "users"]

    ID = 0x4c3e069d
    QUALNAME = "types.account.autoSaveSettings"

    def __init__(self, *, users_settings: "api.ayiin.AutoSaveSettings", chats_settings: "api.ayiin.AutoSaveSettings", broadcasts_settings: "api.ayiin.AutoSaveSettings", exceptions: List["api.ayiin.AutoSaveException"], chats: List["api.ayiin.Chat"], users: List["api.ayiin.User"]) -> None:
        
                self.users_settings = users_settings  # AutoSaveSettings
        
                self.chats_settings = chats_settings  # AutoSaveSettings
        
                self.broadcasts_settings = broadcasts_settings  # AutoSaveSettings
        
                self.exceptions = exceptions  # AutoSaveException
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveSettings":
        # No flags
        
        users_settings = Object.read(b)
        
        chats_settings = Object.read(b)
        
        broadcasts_settings = Object.read(b)
        
        exceptions = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return AutoSaveSettings(users_settings=users_settings, chats_settings=chats_settings, broadcasts_settings=broadcasts_settings, exceptions=exceptions, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.users_settings.write())
        
        b.write(self.chats_settings.write())
        
        b.write(self.broadcasts_settings.write())
        
        b.write(Vector(self.exceptions))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()