
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



class DeletePhoneCallHistory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F9CBE409``

revoke (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.AffectedFoundMessages<typegram.api.ayiin.messages.AffectedFoundMessages>`
    """

    __slots__: List[str] = ["revoke"]

    ID = 0xf9cbe409
    QUALNAME = "functions.functionsmessages.AffectedFoundMessages"

    def __init__(self, *, revoke: Optional[bool] = None) -> None:
        
                self.revoke = revoke  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhoneCallHistory":
        
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        return DeletePhoneCallHistory(revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()