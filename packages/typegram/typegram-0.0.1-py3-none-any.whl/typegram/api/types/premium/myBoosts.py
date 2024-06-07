
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



class MyBoosts(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.premium.MyBoosts`.

    Details:
        - Layer: ``181``
        - ID: ``9AE228E2``

my_boosts (List of :obj:`MyBoost<typegram.api.ayiin.MyBoost>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            premium.BoostsList
            premium.MyBoosts
            premium.BoostsStatus
    """

    __slots__: List[str] = ["my_boosts", "chats", "users"]

    ID = 0x9ae228e2
    QUALNAME = "functions.typespremium.MyBoosts"

    def __init__(self, *, my_boosts: List["ayiin.MyBoost"], chats: List["ayiin.Chat"], users: List["ayiin.User"]) -> None:
        
                self.my_boosts = my_boosts  # MyBoost
        
                self.chats = chats  # Chat
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyBoosts":
        # No flags
        
        my_boosts = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return MyBoosts(my_boosts=my_boosts, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.my_boosts))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()