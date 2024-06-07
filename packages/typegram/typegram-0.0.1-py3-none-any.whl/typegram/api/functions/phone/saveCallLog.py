
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



class SaveCallLog(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``41248786``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
        file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "file"]

    ID = 0x41248786
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPhoneCall", file: "ayiin.InputFile") -> None:
        
                self.peer = peer  # InputPhoneCall
        
                self.file = file  # InputFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveCallLog":
        # No flags
        
        peer = Object.read(b)
        
        file = Object.read(b)
        
        return SaveCallLog(peer=peer, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.file.write())
        
        return b.getvalue()