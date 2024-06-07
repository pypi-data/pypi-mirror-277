
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



class EditBusinessChatLink(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8C3410AF``

slug (``str``):
                    N/A
                
        link (:obj:`InputBusinessChatLink<typegram.api.ayiin.InputBusinessChatLink>`):
                    N/A
                
    Returns:
        :obj:`BusinessChatLink<typegram.api.ayiin.BusinessChatLink>`
    """

    __slots__: List[str] = ["slug", "link"]

    ID = 0x8c3410af
    QUALNAME = "functions.functions.BusinessChatLink"

    def __init__(self, *, slug: str, link: "ayiin.InputBusinessChatLink") -> None:
        
                self.slug = slug  # string
        
                self.link = link  # InputBusinessChatLink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBusinessChatLink":
        # No flags
        
        slug = String.read(b)
        
        link = Object.read(b)
        
        return EditBusinessChatLink(slug=slug, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        b.write(self.link.write())
        
        return b.getvalue()