
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



class RecentMeUrls(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.RecentMeUrls`.

    Details:
        - Layer: ``181``
        - ID: ``E0310D7``

urls (List of :obj:`RecentMeUrl<typegram.api.ayiin.RecentMeUrl>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["urls", "chats", "users"]

    ID = 0xe0310d7
    QUALNAME = "functions.typeshelp.RecentMeUrls"

    def __init__(self, *, urls: List["ayiin.RecentMeUrl"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.urls = urls  # RecentMeUrl
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrls":
        # No flags
        
        urls = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return RecentMeUrls(urls=urls, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.urls))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()