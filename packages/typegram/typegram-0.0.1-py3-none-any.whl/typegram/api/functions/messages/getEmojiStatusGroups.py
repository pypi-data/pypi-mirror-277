
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



class GetEmojiStatusGroups(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2ECD56CD``

hash (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.EmojiGroups<typegram.api.ayiin.messages.EmojiGroups>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0x2ecd56cd
    QUALNAME = "functions.functionsmessages.EmojiGroups"

    def __init__(self, *, hash: int) -> None:
        
                self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiStatusGroups":
        # No flags
        
        hash = Int.read(b)
        
        return GetEmojiStatusGroups(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()