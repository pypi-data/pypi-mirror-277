
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



class ExportStoryLink(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7B8DEF20``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`ExportedStoryLink<typegram.api.ayiin.ExportedStoryLink>`
    """

    __slots__: List[str] = ["peer", "id"]

    ID = 0x7b8def20
    QUALNAME = "functions.stories.exportStoryLink"

    def __init__(self, *, peer: "api.ayiin.InputPeer", id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportStoryLink":
        # No flags
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        return ExportStoryLink(peer=peer, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()