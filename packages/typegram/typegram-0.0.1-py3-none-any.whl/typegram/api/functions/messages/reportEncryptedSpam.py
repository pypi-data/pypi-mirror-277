
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



class ReportEncryptedSpam(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``4B0C8C0F``

peer (:obj:`InputEncryptedChat<typegram.api.ayiin.InputEncryptedChat>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x4b0c8c0f
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputEncryptedChat") -> None:
        
                self.peer = peer  # InputEncryptedChat

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportEncryptedSpam":
        # No flags
        
        peer = Object.read(b)
        
        return ReportEncryptedSpam(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()