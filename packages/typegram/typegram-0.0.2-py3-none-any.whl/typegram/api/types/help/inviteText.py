
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



class InviteText(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.InviteText`.

    Details:
        - Layer: ``181``
        - ID: ``18CB9F78``

message (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["message"]

    ID = 0x18cb9f78
    QUALNAME = "types.help.inviteText"

    def __init__(self, *, message: str) -> None:
        
                self.message = message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteText":
        # No flags
        
        message = String.read(b)
        
        return InviteText(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.message))
        
        return b.getvalue()