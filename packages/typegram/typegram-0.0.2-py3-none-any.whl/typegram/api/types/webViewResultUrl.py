
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



class WebViewResultUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebViewResult`.

    Details:
        - Layer: ``181``
        - ID: ``C14557C``

query_id (``int`` ``64-bit``):
                    N/A
                
        url (``str``):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.requestWebView
    """

    __slots__: List[str] = ["query_id", "url"]

    ID = 0xc14557c
    QUALNAME = "types.webViewResultUrl"

    def __init__(self, *, query_id: int, url: str) -> None:
        
                self.query_id = query_id  # long
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewResultUrl":
        # No flags
        
        query_id = Long.read(b)
        
        url = String.read(b)
        
        return WebViewResultUrl(query_id=query_id, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(String(self.url))
        
        return b.getvalue()