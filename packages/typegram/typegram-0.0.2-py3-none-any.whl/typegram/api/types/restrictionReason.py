
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



class RestrictionReason(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RestrictionReason`.

    Details:
        - Layer: ``181``
        - ID: ``D072ACB4``

platform (``str``):
                    N/A
                
        reason (``str``):
                    N/A
                
        text (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["platform", "reason", "text"]

    ID = 0xd072acb4
    QUALNAME = "types.restrictionReason"

    def __init__(self, *, platform: str, reason: str, text: str) -> None:
        
                self.platform = platform  # string
        
                self.reason = reason  # string
        
                self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RestrictionReason":
        # No flags
        
        platform = String.read(b)
        
        reason = String.read(b)
        
        text = String.read(b)
        
        return RestrictionReason(platform=platform, reason=reason, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.platform))
        
        b.write(String(self.reason))
        
        b.write(String(self.text))
        
        return b.getvalue()