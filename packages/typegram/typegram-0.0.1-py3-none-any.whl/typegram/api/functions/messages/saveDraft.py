
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



class SaveDraft(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``7FF3B806``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        message (``str``):
                    N/A
                
        no_webpage (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "message", "no_webpage", "invert_media", "reply_to", "entities", "media"]

    ID = 0x7ff3b806
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: "ayiin.InputReplyTo" = None, entities: Optional[List["ayiin.MessageEntity"]] = None, media: "ayiin.InputMedia" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.message = message  # string
        
                self.no_webpage = no_webpage  # true
        
                self.invert_media = invert_media  # true
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.entities = entities  # MessageEntity
        
                self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDraft":
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 6) else False
        reply_to = Object.read(b) if flags & (1 << 4) else None
        
        peer = Object.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        media = Object.read(b) if flags & (1 << 5) else None
        
        return SaveDraft(peer=peer, message=message, no_webpage=no_webpage, invert_media=invert_media, reply_to=reply_to, entities=entities, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(self.peer.write())
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.media is not None:
            b.write(self.media.write())
        
        return b.getvalue()