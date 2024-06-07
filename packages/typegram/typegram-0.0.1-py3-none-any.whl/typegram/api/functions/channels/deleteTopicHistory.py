
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



class DeleteTopicHistory(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``34435F2D``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        top_msg_id (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.AffectedHistory<typegram.api.ayiin.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["channel", "top_msg_id"]

    ID = 0x34435f2d
    QUALNAME = "functions.functionsmessages.AffectedHistory"

    def __init__(self, *, channel: "ayiin.InputChannel", top_msg_id: int) -> None:
        
                self.channel = channel  # InputChannel
        
                self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteTopicHistory":
        # No flags
        
        channel = Object.read(b)
        
        top_msg_id = Int.read(b)
        
        return DeleteTopicHistory(channel=channel, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.top_msg_id))
        
        return b.getvalue()