
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



class TogglePeerTranslations(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E47CB579``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        disabled (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "disabled"]

    ID = 0xe47cb579
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", disabled: Optional[bool] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.disabled = disabled  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TogglePeerTranslations":
        
        flags = Int.read(b)
        
        disabled = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        return TogglePeerTranslations(peer=peer, disabled=disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()