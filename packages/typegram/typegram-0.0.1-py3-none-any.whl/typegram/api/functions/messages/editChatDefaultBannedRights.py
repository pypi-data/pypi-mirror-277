
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



class EditChatDefaultBannedRights(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A5866B41``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "banned_rights"]

    ID = 0xa5866b41
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", banned_rights: "ayiin.ChatBannedRights") -> None:
        
                self.peer = peer  # InputPeer
        
                self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatDefaultBannedRights":
        # No flags
        
        peer = Object.read(b)
        
        banned_rights = Object.read(b)
        
        return EditChatDefaultBannedRights(peer=peer, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()