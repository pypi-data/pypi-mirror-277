
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



class ReactionCustomEmoji(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Reaction`.

    Details:
        - Layer: ``181``
        - ID: ``8935FC73``

document_id (``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["document_id"]

    ID = 0x8935fc73
    QUALNAME = "types.reactionCustomEmoji"

    def __init__(self, *, document_id: int) -> None:
        
                self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionCustomEmoji":
        # No flags
        
        document_id = Long.read(b)
        
        return ReactionCustomEmoji(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        return b.getvalue()