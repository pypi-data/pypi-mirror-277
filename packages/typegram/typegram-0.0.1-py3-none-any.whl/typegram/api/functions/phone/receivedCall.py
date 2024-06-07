
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



class ReceivedCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``17D54F61``

peer (:obj:`InputPhoneCall<typegram.api.ayiin.InputPhoneCall>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer"]

    ID = 0x17d54f61
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPhoneCall") -> None:
        
                self.peer = peer  # InputPhoneCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedCall":
        # No flags
        
        peer = Object.read(b)
        
        return ReceivedCall(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()