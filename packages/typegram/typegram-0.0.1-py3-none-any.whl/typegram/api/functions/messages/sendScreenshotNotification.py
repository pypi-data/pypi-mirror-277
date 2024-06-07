
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



class SendScreenshotNotification(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A1405817``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "reply_to", "random_id"]

    ID = 0xa1405817
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", reply_to: "ayiin.InputReplyTo", random_id: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.random_id = random_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendScreenshotNotification":
        # No flags
        
        peer = Object.read(b)
        
        reply_to = Object.read(b)
        
        random_id = Long.read(b)
        
        return SendScreenshotNotification(peer=peer, reply_to=reply_to, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.reply_to.write())
        
        b.write(Long(self.random_id))
        
        return b.getvalue()