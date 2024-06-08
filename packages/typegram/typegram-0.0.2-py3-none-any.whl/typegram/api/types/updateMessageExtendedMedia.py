
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



class UpdateMessageExtendedMedia(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``5A73A98C``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        extended_media (:obj:`MessageExtendedMedia<typegram.api.ayiin.MessageExtendedMedia>`):
                    N/A
                
    """

    __slots__: List[str] = ["peer", "msg_id", "extended_media"]

    ID = 0x5a73a98c
    QUALNAME = "types.updateMessageExtendedMedia"

    def __init__(self, *, peer: "api.ayiin.Peer", msg_id: int, extended_media: "api.ayiin.MessageExtendedMedia") -> None:
        
                self.peer = peer  # Peer
        
                self.msg_id = msg_id  # int
        
                self.extended_media = extended_media  # MessageExtendedMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageExtendedMedia":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        extended_media = Object.read(b)
        
        return UpdateMessageExtendedMedia(peer=peer, msg_id=msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(self.extended_media.write())
        
        return b.getvalue()