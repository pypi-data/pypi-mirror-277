
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



class AppWebViewResultUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AppWebViewResult`.

    Details:
        - Layer: ``181``
        - ID: ``3C1B4F0D``

url (``str``):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.requestAppWebView
    """

    __slots__: List[str] = ["url"]

    ID = 0x3c1b4f0d
    QUALNAME = "types.appWebViewResultUrl"

    def __init__(self, *, url: str) -> None:
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppWebViewResultUrl":
        # No flags
        
        url = String.read(b)
        
        return AppWebViewResultUrl(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()