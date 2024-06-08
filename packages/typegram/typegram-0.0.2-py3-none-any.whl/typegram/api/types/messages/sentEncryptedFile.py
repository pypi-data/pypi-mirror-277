
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



class SentEncryptedFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.SentEncryptedMessage`.

    Details:
        - Layer: ``181``
        - ID: ``9493FF32``

date (``int`` ``32-bit``):
                    N/A
                
        file (:obj:`EncryptedFile<typegram.api.ayiin.EncryptedFile>`):
                    N/A
                
    Functions:
        This object can be returned by 26 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.sendEncrypted
            messages.sendEncryptedFile
            messages.sendEncryptedService
    """

    __slots__: List[str] = ["date", "file"]

    ID = 0x9493ff32
    QUALNAME = "types.messages.sentEncryptedFile"

    def __init__(self, *, date: int, file: "api.ayiin.EncryptedFile") -> None:
        
                self.date = date  # int
        
                self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEncryptedFile":
        # No flags
        
        date = Int.read(b)
        
        file = Object.read(b)
        
        return SentEncryptedFile(date=date, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(self.file.write())
        
        return b.getvalue()