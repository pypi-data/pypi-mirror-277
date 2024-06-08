
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



class KeyboardButtonRequestPeer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``53D7BFD8``

text (``str``):
                    N/A
                
        button_id (``int`` ``32-bit``):
                    N/A
                
        peer_type (:obj:`RequestPeerType<typegram.api.ayiin.RequestPeerType>`):
                    N/A
                
        max_quantity (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "button_id", "peer_type", "max_quantity"]

    ID = 0x53d7bfd8
    QUALNAME = "types.keyboardButtonRequestPeer"

    def __init__(self, *, text: str, button_id: int, peer_type: "api.ayiin.RequestPeerType", max_quantity: int) -> None:
        
                self.text = text  # string
        
                self.button_id = button_id  # int
        
                self.peer_type = peer_type  # RequestPeerType
        
                self.max_quantity = max_quantity  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPeer":
        # No flags
        
        text = String.read(b)
        
        button_id = Int.read(b)
        
        peer_type = Object.read(b)
        
        max_quantity = Int.read(b)
        
        return KeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()