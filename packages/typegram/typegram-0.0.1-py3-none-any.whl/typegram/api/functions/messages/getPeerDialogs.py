
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



class GetPeerDialogs(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E470BCFD``

peers (List of :obj:`InputDialogPeer<typegram.api.ayiin.InputDialogPeer>`):
                    N/A
                
    Returns:
        :obj:`messages.PeerDialogs<typegram.api.ayiin.messages.PeerDialogs>`
    """

    __slots__: List[str] = ["peers"]

    ID = 0xe470bcfd
    QUALNAME = "functions.functionsmessages.PeerDialogs"

    def __init__(self, *, peers: List["ayiin.InputDialogPeer"]) -> None:
        
                self.peers = peers  # InputDialogPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPeerDialogs":
        # No flags
        
        peers = Object.read(b)
        
        return GetPeerDialogs(peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.peers))
        
        return b.getvalue()