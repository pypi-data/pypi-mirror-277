
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



class GroupCallParticipantVideo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.GroupCallParticipantVideo`.

    Details:
        - Layer: ``181``
        - ID: ``67753AC8``

endpoint (``str``):
                    N/A
                
        source_groups (List of :obj:`GroupCallParticipantVideoSourceGroup<typegram.api.ayiin.GroupCallParticipantVideoSourceGroup>`):
                    N/A
                
        paused (``bool``, *optional*):
                    N/A
                
        audio_source (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["endpoint", "source_groups", "paused", "audio_source"]

    ID = 0x67753ac8
    QUALNAME = "types.groupCallParticipantVideo"

    def __init__(self, *, endpoint: str, source_groups: List["api.ayiin.GroupCallParticipantVideoSourceGroup"], paused: Optional[bool] = None, audio_source: Optional[int] = None) -> None:
        
                self.endpoint = endpoint  # string
        
                self.source_groups = source_groups  # GroupCallParticipantVideoSourceGroup
        
                self.paused = paused  # true
        
                self.audio_source = audio_source  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipantVideo":
        
        flags = Int.read(b)
        
        paused = True if flags & (1 << 0) else False
        endpoint = String.read(b)
        
        source_groups = Object.read(b)
        
        audio_source = Int.read(b) if flags & (1 << 1) else None
        return GroupCallParticipantVideo(endpoint=endpoint, source_groups=source_groups, paused=paused, audio_source=audio_source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.endpoint))
        
        b.write(Vector(self.source_groups))
        
        if self.audio_source is not None:
            b.write(Int(self.audio_source))
        
        return b.getvalue()