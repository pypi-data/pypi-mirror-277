
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



class UpdateNotifySettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``84BE5B93``

peer (:obj:`InputNotifyPeer<typegram.api.ayiin.InputNotifyPeer>`):
                    N/A
                
        settings (:obj:`InputPeerNotifySettings<typegram.api.ayiin.InputPeerNotifySettings>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "settings"]

    ID = 0x84be5b93
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputNotifyPeer", settings: "ayiin.InputPeerNotifySettings") -> None:
        
                self.peer = peer  # InputNotifyPeer
        
                self.settings = settings  # InputPeerNotifySettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNotifySettings":
        # No flags
        
        peer = Object.read(b)
        
        settings = Object.read(b)
        
        return UpdateNotifySettings(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()