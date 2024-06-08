
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



class BusinessWorkHours(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessWorkHours`.

    Details:
        - Layer: ``181``
        - ID: ``8C92B098``

timezone_id (``str``):
                    N/A
                
        weekly_open (List of :obj:`BusinessWeeklyOpen<typegram.api.ayiin.BusinessWeeklyOpen>`):
                    N/A
                
        open_now (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["timezone_id", "weekly_open", "open_now"]

    ID = 0x8c92b098
    QUALNAME = "types.businessWorkHours"

    def __init__(self, *, timezone_id: str, weekly_open: List["api.ayiin.BusinessWeeklyOpen"], open_now: Optional[bool] = None) -> None:
        
                self.timezone_id = timezone_id  # string
        
                self.weekly_open = weekly_open  # BusinessWeeklyOpen
        
                self.open_now = open_now  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessWorkHours":
        
        flags = Int.read(b)
        
        open_now = True if flags & (1 << 0) else False
        timezone_id = String.read(b)
        
        weekly_open = Object.read(b)
        
        return BusinessWorkHours(timezone_id=timezone_id, weekly_open=weekly_open, open_now=open_now)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.timezone_id))
        
        b.write(Vector(self.weekly_open))
        
        return b.getvalue()