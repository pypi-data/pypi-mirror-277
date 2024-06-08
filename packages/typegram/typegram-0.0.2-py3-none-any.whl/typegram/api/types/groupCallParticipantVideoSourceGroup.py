
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



class GroupCallParticipantVideoSourceGroup(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GroupCallParticipantVideoSourceGroup`.

    Details:
        - Layer: ``181``
        - ID: ``DCB118B7``

semantics (``str``):
                    N/A
                
        sources (List of ``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["semantics", "sources"]

    ID = 0xdcb118b7
    QUALNAME = "types.groupCallParticipantVideoSourceGroup"

    def __init__(self, *, semantics: str, sources: List[int]) -> None:
        
                self.semantics = semantics  # string
        
                self.sources = sources  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipantVideoSourceGroup":
        # No flags
        
        semantics = String.read(b)
        
        sources = Object.read(b, Int)
        
        return GroupCallParticipantVideoSourceGroup(semantics=semantics, sources=sources)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.semantics))
        
        b.write(Vector(self.sources, Int))
        
        return b.getvalue()