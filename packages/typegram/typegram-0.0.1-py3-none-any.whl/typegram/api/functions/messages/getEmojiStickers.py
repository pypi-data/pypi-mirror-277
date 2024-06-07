
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



class GetEmojiStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``FBFCA18F``

hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`messages.AllStickers<typegram.api.ayiin.messages.AllStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xfbfca18f
    QUALNAME = "functions.functionsmessages.AllStickers"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiStickers":
        # No flags
        
        hash = Long.read(b)
        
        return GetEmojiStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        return b.getvalue()