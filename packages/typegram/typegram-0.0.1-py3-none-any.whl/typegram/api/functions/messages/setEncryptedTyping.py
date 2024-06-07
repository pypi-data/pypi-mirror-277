
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



class SetEncryptedTyping(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``791451ED``

peer (:obj:`InputEncryptedChat<typegram.api.ayiin.InputEncryptedChat>`):
                    N/A
                
        typing (``bool``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "typing"]

    ID = 0x791451ed
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputEncryptedChat", typing: bool) -> None:
        
                self.peer = peer  # InputEncryptedChat
        
                self.typing = typing  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetEncryptedTyping":
        # No flags
        
        peer = Object.read(b)
        
        typing = Bool.read(b)
        
        return SetEncryptedTyping(peer=peer, typing=typing)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.typing))
        
        return b.getvalue()