
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



class DeleteExportedChatInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D464A42B``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        link (``str``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "link"]

    ID = 0xd464a42b
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", link: str) -> None:
        
                self.peer = peer  # InputPeer
        
                self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteExportedChatInvite":
        # No flags
        
        peer = Object.read(b)
        
        link = String.read(b)
        
        return DeleteExportedChatInvite(peer=peer, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        return b.getvalue()