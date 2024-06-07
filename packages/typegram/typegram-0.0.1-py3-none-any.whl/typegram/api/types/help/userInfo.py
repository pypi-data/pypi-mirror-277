
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



class UserInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.UserInfo`.

    Details:
        - Layer: ``181``
        - ID: ``1EB3758``

message (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
        author (``str``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

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

    __slots__: List[str] = ["message", "entities", "author", "date"]

    ID = 0x1eb3758
    QUALNAME = "functions.typeshelp.UserInfo"

    def __init__(self, *, message: str, entities: List["ayiin.MessageEntity"], author: str, date: int) -> None:
        
                self.message = message  # string
        
                self.entities = entities  # MessageEntity
        
                self.author = author  # string
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserInfo":
        # No flags
        
        message = String.read(b)
        
        entities = Object.read(b)
        
        author = String.read(b)
        
        date = Int.read(b)
        
        return UserInfo(message=message, entities=entities, author=author, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.message))
        
        b.write(Vector(self.entities))
        
        b.write(String(self.author))
        
        b.write(Int(self.date))
        
        return b.getvalue()