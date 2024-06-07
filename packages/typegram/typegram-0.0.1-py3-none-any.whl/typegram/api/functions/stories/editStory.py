
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



class EditStory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B583BA46``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`, *optional*):
                    N/A
                
        media_areas (List of :obj:`MediaArea<typegram.api.ayiin.MediaArea>`, *optional*):
                    N/A
                
        caption (``str``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        privacy_rules (List of :obj:`InputPrivacyRule<typegram.api.ayiin.InputPrivacyRule>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "media", "media_areas", "caption", "entities", "privacy_rules"]

    ID = 0xb583ba46
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", id: int, media: "ayiin.InputMedia" = None, media_areas: Optional[List["ayiin.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["ayiin.MessageEntity"]] = None, privacy_rules: Optional[List["ayiin.InputPrivacyRule"]] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.media = media  # InputMedia
        
                self.media_areas = media_areas  # MediaArea
        
                self.caption = caption  # string
        
                self.entities = entities  # MessageEntity
        
                self.privacy_rules = privacy_rules  # InputPrivacyRule

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditStory":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        id = Int.read(b)
        
        media = Object.read(b) if flags & (1 << 0) else None
        
        media_areas = Object.read(b) if flags & (1 << 3) else []
        
        caption = String.read(b) if flags & (1 << 1) else None
        entities = Object.read(b) if flags & (1 << 1) else []
        
        privacy_rules = Object.read(b) if flags & (1 << 2) else []
        
        return EditStory(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.privacy_rules is not None:
            b.write(Vector(self.privacy_rules))
        
        return b.getvalue()