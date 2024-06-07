
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



class UploadMedia(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``14967978``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`):
                    N/A
                
        business_connection_id (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "media", "business_connection_id"]

    ID = 0x14967978
    QUALNAME = "functions.functions.MessageMedia"

    def __init__(self, *, peer: "ayiin.InputPeer", media: "ayiin.InputMedia", business_connection_id: Optional[str] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.media = media  # InputMedia
        
                self.business_connection_id = business_connection_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadMedia":
        
        flags = Int.read(b)
        
        business_connection_id = String.read(b) if flags & (1 << 0) else None
        peer = Object.read(b)
        
        media = Object.read(b)
        
        return UploadMedia(peer=peer, media=media, business_connection_id=business_connection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.business_connection_id is not None:
            b.write(String(self.business_connection_id))
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        return b.getvalue()