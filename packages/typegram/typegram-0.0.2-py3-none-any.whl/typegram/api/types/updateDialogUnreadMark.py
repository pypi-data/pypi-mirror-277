
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



class UpdateDialogUnreadMark(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``E16459C3``

peer (:obj:`DialogPeer<typegram.api.ayiin.DialogPeer>`):
                    N/A
                
        unread (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "unread"]

    ID = 0xe16459c3
    QUALNAME = "types.updateDialogUnreadMark"

    def __init__(self, *, peer: "api.ayiin.DialogPeer", unread: Optional[bool] = None) -> None:
        
                self.peer = peer  # DialogPeer
        
                self.unread = unread  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogUnreadMark":
        
        flags = Int.read(b)
        
        unread = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        return UpdateDialogUnreadMark(peer=peer, unread=unread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()