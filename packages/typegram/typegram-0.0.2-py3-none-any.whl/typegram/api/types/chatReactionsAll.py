
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



class ChatReactionsAll(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatReactions`.

    Details:
        - Layer: ``181``
        - ID: ``52928BCA``

allow_custom (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["allow_custom"]

    ID = 0x52928bca
    QUALNAME = "types.chatReactionsAll"

    def __init__(self, *, allow_custom: Optional[bool] = None) -> None:
        
                self.allow_custom = allow_custom  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsAll":
        
        flags = Int.read(b)
        
        allow_custom = True if flags & (1 << 0) else False
        return ChatReactionsAll(allow_custom=allow_custom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()