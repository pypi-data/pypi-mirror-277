
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



class SentEncryptedMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SentEncryptedMessage`.

    Details:
        - Layer: ``181``
        - ID: ``560F8935``

date (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 29 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.sendEncrypted
            messages.sendEncryptedFile
            messages.sendEncryptedService
    """

    __slots__: List[str] = ["date"]

    ID = 0x560f8935
    QUALNAME = "types.messages.sentEncryptedMessage"

    def __init__(self, *, date: int) -> None:
        
                self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEncryptedMessage":
        # No flags
        
        date = Int.read(b)
        
        return SentEncryptedMessage(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        return b.getvalue()