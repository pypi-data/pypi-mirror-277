
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



class GetForumTopicsByID(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B0831EB9``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        topics (List of ``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.ForumTopics<typegram.api.ayiin.messages.ForumTopics>`
    """

    __slots__: List[str] = ["channel", "topics"]

    ID = 0xb0831eb9
    QUALNAME = "functions.functionsmessages.ForumTopics"

    def __init__(self, *, channel: "ayiin.InputChannel", topics: List[int]) -> None:
        
                self.channel = channel  # InputChannel
        
                self.topics = topics  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetForumTopicsByID":
        # No flags
        
        channel = Object.read(b)
        
        topics = Object.read(b, Int)
        
        return GetForumTopicsByID(channel=channel, topics=topics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Vector(self.topics, Int))
        
        return b.getvalue()