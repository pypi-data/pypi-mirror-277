
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



class BotMenuButton(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotMenuButton`.

    Details:
        - Layer: ``181``
        - ID: ``C7B57CE6``

text (``str``):
                    N/A
                
        url (``str``):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            bots.getBotMenuButton
    """

    __slots__: List[str] = ["text", "url"]

    ID = 0xc7b57ce6
    QUALNAME = "types.botMenuButton"

    def __init__(self, *, text: str, url: str) -> None:
        
                self.text = text  # string
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotMenuButton":
        # No flags
        
        text = String.read(b)
        
        url = String.read(b)
        
        return BotMenuButton(text=text, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.url))
        
        return b.getvalue()