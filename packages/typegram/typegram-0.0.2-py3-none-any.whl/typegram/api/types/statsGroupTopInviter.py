
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



class StatsGroupTopInviter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StatsGroupTopInviter`.

    Details:
        - Layer: ``181``
        - ID: ``535F779D``

user_id (``int`` ``64-bit``):
                    N/A
                
        invitations (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["user_id", "invitations"]

    ID = 0x535f779d
    QUALNAME = "types.statsGroupTopInviter"

    def __init__(self, *, user_id: int, invitations: int) -> None:
        
                self.user_id = user_id  # long
        
                self.invitations = invitations  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGroupTopInviter":
        # No flags
        
        user_id = Long.read(b)
        
        invitations = Int.read(b)
        
        return StatsGroupTopInviter(user_id=user_id, invitations=invitations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.invitations))
        
        return b.getvalue()