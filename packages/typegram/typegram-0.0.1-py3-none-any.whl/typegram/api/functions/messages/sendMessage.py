
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



class SendMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``983F9745``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        message (``str``):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        background (``bool``, *optional*):
                    N/A
                
        clear_draft (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        update_stickersets_order (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        schedule_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        send_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        quick_reply_shortcut (:obj:`InputQuickReplyShortcut<typegram.api.ayiin.InputQuickReplyShortcut>`, *optional*):
                    N/A
                
        effect (``int`` ``64-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "message", "random_id", "no_webpage", "silent", "background", "clear_draft", "noforwards", "update_stickersets_order", "invert_media", "reply_to", "reply_markup", "entities", "schedule_date", "send_as", "quick_reply_shortcut", "effect"]

    ID = 0x983f9745
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", message: str, random_id: int, no_webpage: Optional[bool] = None, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: "ayiin.InputReplyTo" = None, reply_markup: "ayiin.ReplyMarkup" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, schedule_date: Optional[int] = None, send_as: "ayiin.InputPeer" = None, quick_reply_shortcut: "ayiin.InputQuickReplyShortcut" = None, effect: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.message = message  # string
        
                self.random_id = random_id  # long
        
                self.no_webpage = no_webpage  # true
        
                self.silent = silent  # true
        
                self.background = background  # true
        
                self.clear_draft = clear_draft  # true
        
                self.noforwards = noforwards  # true
        
                self.update_stickersets_order = update_stickersets_order  # true
        
                self.invert_media = invert_media  # true
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.reply_markup = reply_markup  # ReplyMarkup
        
                self.entities = entities  # MessageEntity
        
                self.schedule_date = schedule_date  # int
        
                self.send_as = send_as  # InputPeer
        
                self.quick_reply_shortcut = quick_reply_shortcut  # InputQuickReplyShortcut
        
                self.effect = effect  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessage":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        noforwards = True if flags & (1 << 14) else False
        update_stickersets_order = True if flags & (1 << 15) else False
        invert_media = True if flags & (1 << 16) else False
        peer = Object.read(b)
        
        reply_to = Object.read(b) if flags & (1 << 0) else None
        
        message = String.read(b)
        
        random_id = Long.read(b)
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = Object.read(b) if flags & (1 << 13) else None
        
        quick_reply_shortcut = Object.read(b) if flags & (1 << 17) else None
        
        effect = Long.read(b) if flags & (1 << 18) else None
        return SendMessage(peer=peer, message=message, random_id=random_id, no_webpage=no_webpage, silent=silent, background=background, clear_draft=clear_draft, noforwards=noforwards, update_stickersets_order=update_stickersets_order, invert_media=invert_media, reply_to=reply_to, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut, effect=effect)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(String(self.message))
        
        b.write(Long(self.random_id))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())
        
        if self.effect is not None:
            b.write(Long(self.effect))
        
        return b.getvalue()