
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



class CreateStickerSet(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9021AB67``

user_id (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        title (``str``):
                    N/A
                
        short_name (``str``):
                    N/A
                
        stickers (List of :obj:`InputStickerSetItem<typegram.api.ayiin.InputStickerSetItem>`):
                    N/A
                
        masks (``bool``, *optional*):
                    N/A
                
        emojis (``bool``, *optional*):
                    N/A
                
        text_color (``bool``, *optional*):
                    N/A
                
        thumb (:obj:`InputDocument<typegram.api.ayiin.InputDocument>`, *optional*):
                    N/A
                
        software (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.StickerSet<typegram.api.ayiin.messages.StickerSet>`
    """

    __slots__: List[str] = ["user_id", "title", "short_name", "stickers", "masks", "emojis", "text_color", "thumb", "software"]

    ID = 0x9021ab67
    QUALNAME = "functions.functionsmessages.StickerSet"

    def __init__(self, *, user_id: "ayiin.InputUser", title: str, short_name: str, stickers: List["ayiin.InputStickerSetItem"], masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: "ayiin.InputDocument" = None, software: Optional[str] = None) -> None:
        
                self.user_id = user_id  # InputUser
        
                self.title = title  # string
        
                self.short_name = short_name  # string
        
                self.stickers = stickers  # InputStickerSetItem
        
                self.masks = masks  # true
        
                self.emojis = emojis  # true
        
                self.text_color = text_color  # true
        
                self.thumb = thumb  # InputDocument
        
                self.software = software  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateStickerSet":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 5) else False
        text_color = True if flags & (1 << 6) else False
        user_id = Object.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        thumb = Object.read(b) if flags & (1 << 2) else None
        
        stickers = Object.read(b)
        
        software = String.read(b) if flags & (1 << 3) else None
        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks, emojis=emojis, text_color=text_color, thumb=thumb, software=software)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(Vector(self.stickers))
        
        if self.software is not None:
            b.write(String(self.software))
        
        return b.getvalue()