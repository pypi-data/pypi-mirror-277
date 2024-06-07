
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



class EditMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DFD14005``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        message (``str``, *optional*):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        schedule_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        quick_reply_shortcut_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities", "schedule_date", "quick_reply_shortcut_id"]

    ID = 0xdfd14005
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: "ayiin.InputMedia" = None, reply_markup: "ayiin.ReplyMarkup" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, schedule_date: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.no_webpage = no_webpage  # true
        
                self.invert_media = invert_media  # true
        
                self.message = message  # string
        
                self.media = media  # InputMedia
        
                self.reply_markup = reply_markup  # ReplyMarkup
        
                self.entities = entities  # MessageEntity
        
                self.schedule_date = schedule_date  # int
        
                self.quick_reply_shortcut_id = quick_reply_shortcut_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditMessage":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        media = Object.read(b) if flags & (1 << 14) else None
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        schedule_date = Int.read(b) if flags & (1 << 15) else None
        quick_reply_shortcut_id = Int.read(b) if flags & (1 << 17) else None
        return EditMessage(peer=peer, id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, quick_reply_shortcut_id=quick_reply_shortcut_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.quick_reply_shortcut_id is not None:
            b.write(Int(self.quick_reply_shortcut_id))
        
        return b.getvalue()