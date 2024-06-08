
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



class UpdateQuickReplies(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F9470AB2``

quick_replies (List of :obj:`QuickReply<typegram.api.ayiin.QuickReply>`):
                    N/A
                
    """

    __slots__: List[str] = ["quick_replies"]

    ID = 0xf9470ab2
    QUALNAME = "types.updateQuickReplies"

    def __init__(self, *, quick_replies: List["api.ayiin.QuickReply"]) -> None:
        
                self.quick_replies = quick_replies  # QuickReply

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateQuickReplies":
        # No flags
        
        quick_replies = Object.read(b)
        
        return UpdateQuickReplies(quick_replies=quick_replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.quick_replies))
        
        return b.getvalue()