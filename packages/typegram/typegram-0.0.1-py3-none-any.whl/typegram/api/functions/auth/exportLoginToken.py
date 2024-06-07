
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



class ExportLoginToken(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B7E085FE``

api_id (``int`` ``32-bit``):
                    N/A
                
        api_hash (``str``):
                    N/A
                
        except_ids (List of ``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`auth.LoginToken<typegram.api.ayiin.auth.LoginToken>`
    """

    __slots__: List[str] = ["api_id", "api_hash", "except_ids"]

    ID = 0xb7e085fe
    QUALNAME = "functions.functionsauth.LoginToken"

    def __init__(self, *, api_id: int, api_hash: str, except_ids: List[int]) -> None:
        
                self.api_id = api_id  # int
        
                self.api_hash = api_hash  # string
        
                self.except_ids = except_ids  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportLoginToken":
        # No flags
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        except_ids = Object.read(b, Long)
        
        return ExportLoginToken(api_id=api_id, api_hash=api_hash, except_ids=except_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        b.write(Vector(self.except_ids, Long))
        
        return b.getvalue()