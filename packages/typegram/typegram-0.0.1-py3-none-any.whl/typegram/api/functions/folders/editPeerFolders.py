
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



class EditPeerFolders(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``6847D0AB``

folder_peers (List of :obj:`InputFolderPeer<typegram.api.ayiin.InputFolderPeer>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["folder_peers"]

    ID = 0x6847d0ab
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, folder_peers: List["ayiin.InputFolderPeer"]) -> None:
        
                self.folder_peers = folder_peers  # InputFolderPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditPeerFolders":
        # No flags
        
        folder_peers = Object.read(b)
        
        return EditPeerFolders(folder_peers=folder_peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.folder_peers))
        
        return b.getvalue()