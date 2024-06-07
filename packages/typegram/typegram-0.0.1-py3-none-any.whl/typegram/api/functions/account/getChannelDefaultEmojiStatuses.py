
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



class GetChannelDefaultEmojiStatuses(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7727A7D5``

hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`account.EmojiStatuses<typegram.api.ayiin.account.EmojiStatuses>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x7727a7d5
    QUALNAME = "functions.functionsaccount.EmojiStatuses"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelDefaultEmojiStatuses":
        # No flags
        
        hash = Long.read(b)
        
        return GetChannelDefaultEmojiStatuses(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        return b.getvalue()