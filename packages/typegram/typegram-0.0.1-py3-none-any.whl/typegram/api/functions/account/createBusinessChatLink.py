
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



class CreateBusinessChatLink(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8851E68E``

link (:obj:`InputBusinessChatLink<typegram.api.ayiin.InputBusinessChatLink>`):
                    N/A
                
    Returns:
        :obj:`BusinessChatLink<typegram.api.ayiin.BusinessChatLink>`
    """

    __slots__: List[str] = ["link"]

    ID = 0x8851e68e
    QUALNAME = "functions.functions.BusinessChatLink"

    def __init__(self, *, link: "ayiin.InputBusinessChatLink") -> None:
        
                self.link = link  # InputBusinessChatLink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateBusinessChatLink":
        # No flags
        
        link = Object.read(b)
        
        return CreateBusinessChatLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.link.write())
        
        return b.getvalue()