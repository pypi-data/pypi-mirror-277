
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



class BankCardOpenUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BankCardOpenUrl`.

    Details:
        - Layer: ``181``
        - ID: ``F568028A``

url (``str``):
                    N/A
                
        name (``str``):
                    N/A
                
    """

    __slots__: List[str] = ["url", "name"]

    ID = 0xf568028a
    QUALNAME = "types.bankCardOpenUrl"

    def __init__(self, *, url: str, name: str) -> None:
        
                self.url = url  # string
        
                self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BankCardOpenUrl":
        # No flags
        
        url = String.read(b)
        
        name = String.read(b)
        
        return BankCardOpenUrl(url=url, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(String(self.name))
        
        return b.getvalue()