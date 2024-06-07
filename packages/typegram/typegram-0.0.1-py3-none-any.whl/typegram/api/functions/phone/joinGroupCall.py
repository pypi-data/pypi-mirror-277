
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



class JoinGroupCall(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B132FF7B``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        join_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        muted (``bool``, *optional*):
                    N/A
                
        video_stopped (``bool``, *optional*):
                    N/A
                
        invite_hash (``str``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["call", "join_as", "params", "muted", "video_stopped", "invite_hash"]

    ID = 0xb132ff7b
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, call: "ayiin.InputGroupCall", join_as: "ayiin.InputPeer", params: "ayiin.DataJSON", muted: Optional[bool] = None, video_stopped: Optional[bool] = None, invite_hash: Optional[str] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.join_as = join_as  # InputPeer
        
                self.params = params  # DataJSON
        
                self.muted = muted  # true
        
                self.video_stopped = video_stopped  # true
        
                self.invite_hash = invite_hash  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinGroupCall":
        
        flags = Int.read(b)
        
        muted = True if flags & (1 << 0) else False
        video_stopped = True if flags & (1 << 2) else False
        call = Object.read(b)
        
        join_as = Object.read(b)
        
        invite_hash = String.read(b) if flags & (1 << 1) else None
        params = Object.read(b)
        
        return JoinGroupCall(call=call, join_as=join_as, params=params, muted=muted, video_stopped=video_stopped, invite_hash=invite_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.join_as.write())
        
        if self.invite_hash is not None:
            b.write(String(self.invite_hash))
        
        b.write(self.params.write())
        
        return b.getvalue()