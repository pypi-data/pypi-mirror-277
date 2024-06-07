
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



class GetAttachedStickers(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``CC5B67CC``

media (:obj:`InputStickeredMedia<typegram.api.ayiin.InputStickeredMedia>`):
                    N/A
                
    Returns:
        List of :obj:`StickerSetCovered<typegram.api.ayiin.StickerSetCovered>`
    """

    __slots__: List[str] = ["media"]

    ID = 0xcc5b67cc
    QUALNAME = "functions.functions.Vector<StickerSetCovered>"

    def __init__(self, *, media: "ayiin.InputStickeredMedia") -> None:
        
                self.media = media  # InputStickeredMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAttachedStickers":
        # No flags
        
        media = Object.read(b)
        
        return GetAttachedStickers(media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.media.write())
        
        return b.getvalue()