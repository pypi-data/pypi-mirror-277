
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



class MessageMediaStory(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``68CB6283``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        via_mention (``bool``, *optional*):
                    N/A
                
        story (:obj:`StoryItem<typegram.api.ayiin.StoryItem>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getWebPagePreview
            messages.uploadMedia
            messages.uploadImportedMedia
    """

    __slots__: List[str] = ["peer", "id", "via_mention", "story"]

    ID = 0x68cb6283
    QUALNAME = "types.messageMediaStory"

    def __init__(self, *, peer: "api.ayiin.Peer", id: int, via_mention: Optional[bool] = None, story: "api.ayiin.StoryItem" = None) -> None:
        
                self.peer = peer  # Peer
        
                self.id = id  # int
        
                self.via_mention = via_mention  # true
        
                self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaStory":
        
        flags = Int.read(b)
        
        via_mention = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        story = Object.read(b) if flags & (1 << 0) else None
        
        return MessageMediaStory(peer=peer, id=id, via_mention=via_mention, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.story is not None:
            b.write(self.story.write())
        
        return b.getvalue()