
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



class BotInfo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.bots.BotInfo`.

    Details:
        - Layer: ``181``
        - ID: ``E8A775B0``

name (``str``):
                    N/A
                
        about (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
    Functions:
        This object can be returned by 12 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            bots.BotInfo
    """

    __slots__: List[str] = ["name", "about", "description"]

    ID = 0xe8a775b0
    QUALNAME = "functions.typesbots.BotInfo"

    def __init__(self, *, name: str, about: str, description: str) -> None:
        
                self.name = name  # string
        
                self.about = about  # string
        
                self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        # No flags
        
        name = String.read(b)
        
        about = String.read(b)
        
        description = String.read(b)
        
        return BotInfo(name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        b.write(String(self.about))
        
        b.write(String(self.description))
        
        return b.getvalue()