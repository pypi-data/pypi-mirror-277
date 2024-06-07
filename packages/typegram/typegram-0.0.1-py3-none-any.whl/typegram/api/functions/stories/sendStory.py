
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



class SendStory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E4E6694B``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`):
                    N/A
                
        privacy_rules (List of :obj:`InputPrivacyRule<typegram.api.ayiin.InputPrivacyRule>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        fwd_modified (``bool``, *optional*):
                    N/A
                
        media_areas (List of :obj:`MediaArea<typegram.api.ayiin.MediaArea>`, *optional*):
                    N/A
                
        caption (``str``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        period (``int`` ``32-bit``, *optional*):
                    N/A
                
        fwd_from_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        fwd_from_story (``int`` ``32-bit``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "media", "privacy_rules", "random_id", "pinned", "noforwards", "fwd_modified", "media_areas", "caption", "entities", "period", "fwd_from_id", "fwd_from_story"]

    ID = 0xe4e6694b
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", media: "ayiin.InputMedia", privacy_rules: List["ayiin.InputPrivacyRule"], random_id: int, pinned: Optional[bool] = None, noforwards: Optional[bool] = None, fwd_modified: Optional[bool] = None, media_areas: Optional[List["ayiin.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["ayiin.MessageEntity"]] = None, period: Optional[int] = None, fwd_from_id: "ayiin.InputPeer" = None, fwd_from_story: Optional[int] = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.media = media  # InputMedia
        
                self.privacy_rules = privacy_rules  # InputPrivacyRule
        
                self.random_id = random_id  # long
        
                self.pinned = pinned  # true
        
                self.noforwards = noforwards  # true
        
                self.fwd_modified = fwd_modified  # true
        
                self.media_areas = media_areas  # MediaArea
        
                self.caption = caption  # string
        
                self.entities = entities  # MessageEntity
        
                self.period = period  # int
        
                self.fwd_from_id = fwd_from_id  # InputPeer
        
                self.fwd_from_story = fwd_from_story  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStory":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        noforwards = True if flags & (1 << 4) else False
        fwd_modified = True if flags & (1 << 7) else False
        peer = Object.read(b)
        
        media = Object.read(b)
        
        media_areas = Object.read(b) if flags & (1 << 5) else []
        
        caption = String.read(b) if flags & (1 << 0) else None
        entities = Object.read(b) if flags & (1 << 1) else []
        
        privacy_rules = Object.read(b)
        
        random_id = Long.read(b)
        
        period = Int.read(b) if flags & (1 << 3) else None
        fwd_from_id = Object.read(b) if flags & (1 << 6) else None
        
        fwd_from_story = Int.read(b) if flags & (1 << 6) else None
        return SendStory(peer=peer, media=media, privacy_rules=privacy_rules, random_id=random_id, pinned=pinned, noforwards=noforwards, fwd_modified=fwd_modified, media_areas=media_areas, caption=caption, entities=entities, period=period, fwd_from_id=fwd_from_id, fwd_from_story=fwd_from_story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(Vector(self.privacy_rules))
        
        b.write(Long(self.random_id))
        
        if self.period is not None:
            b.write(Int(self.period))
        
        if self.fwd_from_id is not None:
            b.write(self.fwd_from_id.write())
        
        if self.fwd_from_story is not None:
            b.write(Int(self.fwd_from_story))
        
        return b.getvalue()