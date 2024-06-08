
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



class RequestPeerTypeUser(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RequestPeerType`.

    Details:
        - Layer: ``181``
        - ID: ``5F3B8A00``

bot (``bool``, *optional*):
                    N/A
                
        premium (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["bot", "premium"]

    ID = 0x5f3b8a00
    QUALNAME = "types.requestPeerTypeUser"

    def __init__(self, *, bot: Optional[bool] = None, premium: Optional[bool] = None) -> None:
        
                self.bot = bot  # Bool
        
                self.premium = premium  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeUser":
        
        flags = Int.read(b)
        
        bot = Bool.read(b) if flags & (1 << 0) else None
        premium = Bool.read(b) if flags & (1 << 1) else None
        return RequestPeerTypeUser(bot=bot, premium=premium)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(Bool(self.bot))
        
        if self.premium is not None:
            b.write(Bool(self.premium))
        
        return b.getvalue()