
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



class AttachMenuBots(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AttachMenuBots`.

    Details:
        - Layer: ``181``
        - ID: ``3C4301C0``

hash (``int`` ``64-bit``):
                    N/A
                
        bots (List of :obj:`AttachMenuBot<typegram.api.ayiin.AttachMenuBot>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getAttachMenuBots
    """

    __slots__: List[str] = ["hash", "bots", "users"]

    ID = 0x3c4301c0
    QUALNAME = "types.attachMenuBots"

    def __init__(self, *, hash: int, bots: List["api.ayiin.AttachMenuBot"], users: List["api.ayiin.User"]) -> None:
        
                self.hash = hash  # long
        
                self.bots = bots  # AttachMenuBot
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBots":
        # No flags
        
        hash = Long.read(b)
        
        bots = Object.read(b)
        
        users = Object.read(b)
        
        return AttachMenuBots(hash=hash, bots=bots, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.bots))
        
        b.write(Vector(self.users))
        
        return b.getvalue()