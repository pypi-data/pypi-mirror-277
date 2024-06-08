
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



class ChannelParticipantsMentions(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelParticipantsFilter`.

    Details:
        - Layer: ``181``
        - ID: ``E04B5CEB``

q (``str``, *optional*):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["q", "top_msg_id"]

    ID = 0xe04b5ceb
    QUALNAME = "types.channelParticipantsMentions"

    def __init__(self, *, q: Optional[str] = None, top_msg_id: Optional[int] = None) -> None:
        
                self.q = q  # string
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantsMentions":
        
        flags = Int.read(b)
        
        q = String.read(b) if flags & (1 << 0) else None
        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        return ChannelParticipantsMentions(q=q, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.q is not None:
            b.write(String(self.q))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        return b.getvalue()