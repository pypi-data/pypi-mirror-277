
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



class StickerSet(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.StickerSet`.

    Details:
        - Layer: ``181``
        - ID: ``6E153F16``

set (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
        packs (List of :obj:`StickerPack<typegram.api.ayiin.StickerPack>`):
                    N/A
                
        keywords (List of :obj:`StickerKeyword<typegram.api.ayiin.StickerKeyword>`):
                    N/A
                
        documents (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getStickerSet
            stickers.createStickerSet
            stickers.removeStickerFromSet
            stickers.changeStickerPosition
            stickers.addStickerToSet
            stickers.setStickerSetThumb
            stickers.changeSticker
            stickers.renameStickerSet
            stickers.replaceSticker
    """

    __slots__: List[str] = ["set", "packs", "keywords", "documents"]

    ID = 0x6e153f16
    QUALNAME = "types.messages.stickerSet"

    def __init__(self, *, set: "api.ayiin.StickerSet", packs: List["api.ayiin.StickerPack"], keywords: List["api.ayiin.StickerKeyword"], documents: List["api.ayiin.Document"]) -> None:
        
                self.set = set  # StickerSet
        
                self.packs = packs  # StickerPack
        
                self.keywords = keywords  # StickerKeyword
        
                self.documents = documents  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSet":
        # No flags
        
        set = Object.read(b)
        
        packs = Object.read(b)
        
        keywords = Object.read(b)
        
        documents = Object.read(b)
        
        return StickerSet(set=set, packs=packs, keywords=keywords, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.keywords))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()