
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



class GetChannelRecommendations(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``25A71742``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Chats<typegram.api.ayiin.messages.Chats>`
    """

    __slots__: List[str] = ["channel"]

    ID = 0x25a71742
    QUALNAME = "functions.functionsmessages.Chats"

    def __init__(self, *, channel: "ayiin.InputChannel" = None) -> None:
        
                self.channel = channel  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelRecommendations":
        
        flags = Int.read(b)
        
        channel = Object.read(b) if flags & (1 << 0) else None
        
        return GetChannelRecommendations(channel=channel)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.channel is not None:
            b.write(self.channel.write())
        
        return b.getvalue()