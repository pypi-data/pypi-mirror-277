
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



class EditGroupCallParticipant(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A5273ABF``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        participant (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        muted (``bool``, *optional*):
                    N/A
                
        volume (``int`` ``32-bit``, *optional*):
                    N/A
                
        raise_hand (``bool``, *optional*):
                    N/A
                
        video_stopped (``bool``, *optional*):
                    N/A
                
        video_paused (``bool``, *optional*):
                    N/A
                
        presentation_paused (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "muted", "volume", "raise_hand", "video_stopped", "video_paused", "presentation_paused"]

    ID = 0xa5273abf
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, call: "ayiin.InputGroupCall", participant: "ayiin.InputPeer", muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.participant = participant  # InputPeer
        
                self.muted = muted  # Bool
        
                self.volume = volume  # int
        
                self.raise_hand = raise_hand  # Bool
        
                self.video_stopped = video_stopped  # Bool
        
                self.video_paused = video_paused  # Bool
        
                self.presentation_paused = presentation_paused  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditGroupCallParticipant":
        
        flags = Int.read(b)
        
        call = Object.read(b)
        
        participant = Object.read(b)
        
        muted = Bool.read(b) if flags & (1 << 0) else None
        volume = Int.read(b) if flags & (1 << 1) else None
        raise_hand = Bool.read(b) if flags & (1 << 2) else None
        video_stopped = Bool.read(b) if flags & (1 << 3) else None
        video_paused = Bool.read(b) if flags & (1 << 4) else None
        presentation_paused = Bool.read(b) if flags & (1 << 5) else None
        return EditGroupCallParticipant(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand, video_stopped=video_stopped, video_paused=video_paused, presentation_paused=presentation_paused)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.participant.write())
        
        if self.muted is not None:
            b.write(Bool(self.muted))
        
        if self.volume is not None:
            b.write(Int(self.volume))
        
        if self.raise_hand is not None:
            b.write(Bool(self.raise_hand))
        
        if self.video_stopped is not None:
            b.write(Bool(self.video_stopped))
        
        if self.video_paused is not None:
            b.write(Bool(self.video_paused))
        
        if self.presentation_paused is not None:
            b.write(Bool(self.presentation_paused))
        
        return b.getvalue()