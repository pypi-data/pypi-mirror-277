
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



class SetStickerSetThumb(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A76A5392``

stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
        thumb (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        thumb_document_id (``int`` ``64-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["stickerset", "thumb", "thumb_document_id"]

    ID = 0xa76a5392
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, stickerset: "ayiin.InputStickerSet", thumb: "ayiin.InputDocument" = None, thumb_document_id: Optional[int] = None) -> None:
        
                self.stickerset = stickerset  # InputStickerSet
        
                self.thumb = thumb  # InputDocument
        
                self.thumb_document_id = thumb_document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetStickerSetThumb":
        
        flags = Int.read(b)
        
        stickerset = Object.read(b)
        
        thumb = Object.read(b) if flags & (1 << 0) else None
        
        thumb_document_id = Long.read(b) if flags & (1 << 1) else None
        return SetStickerSetThumb(stickerset=stickerset, thumb=thumb, thumb_document_id=thumb_document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.stickerset.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.thumb_document_id is not None:
            b.write(Long(self.thumb_document_id))
        
        return b.getvalue()