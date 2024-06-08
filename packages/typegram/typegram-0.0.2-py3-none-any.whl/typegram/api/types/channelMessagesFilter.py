
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



class ChannelMessagesFilter(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelMessagesFilter`.

    Details:
        - Layer: ``181``
        - ID: ``CD77D957``

ranges (List of :obj:`MessageRange<typegram.api.ayiin.MessageRange>`):
                    N/A
                
        exclude_new_messages (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["ranges", "exclude_new_messages"]

    ID = 0xcd77d957
    QUALNAME = "types.channelMessagesFilter"

    def __init__(self, *, ranges: List["api.ayiin.MessageRange"], exclude_new_messages: Optional[bool] = None) -> None:
        
                self.ranges = ranges  # MessageRange
        
                self.exclude_new_messages = exclude_new_messages  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessagesFilter":
        
        flags = Int.read(b)
        
        exclude_new_messages = True if flags & (1 << 1) else False
        ranges = Object.read(b)
        
        return ChannelMessagesFilter(ranges=ranges, exclude_new_messages=exclude_new_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.ranges))
        
        return b.getvalue()