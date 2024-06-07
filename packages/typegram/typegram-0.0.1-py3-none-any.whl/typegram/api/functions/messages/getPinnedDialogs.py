
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



class GetPinnedDialogs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D6B94DF2``

folder_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.PeerDialogs<typegram.api.ayiin.messages.PeerDialogs>`
    """

    __slots__: List[str] = ["folder_id"]

    ID = 0xd6b94df2
    QUALNAME = "functions.functionsmessages.PeerDialogs"

    def __init__(self, *, folder_id: int) -> None:
        
                self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPinnedDialogs":
        # No flags
        
        folder_id = Int.read(b)
        
        return GetPinnedDialogs(folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()