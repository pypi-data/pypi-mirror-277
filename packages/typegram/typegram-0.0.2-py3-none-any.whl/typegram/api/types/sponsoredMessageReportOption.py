
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



class SponsoredMessageReportOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SponsoredMessageReportOption`.

    Details:
        - Layer: ``181``
        - ID: ``430D3150``

text (``str``):
                    N/A
                
        option (``bytes``):
                    N/A
                
    """

    __slots__: List[str] = ["text", "option"]

    ID = 0x430d3150
    QUALNAME = "types.sponsoredMessageReportOption"

    def __init__(self, *, text: str, option: bytes) -> None:
        
                self.text = text  # string
        
                self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportOption":
        # No flags
        
        text = String.read(b)
        
        option = Bytes.read(b)
        
        return SponsoredMessageReportOption(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()