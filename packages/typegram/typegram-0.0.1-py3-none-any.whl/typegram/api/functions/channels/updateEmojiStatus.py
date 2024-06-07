
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



class UpdateEmojiStatus(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F0D3E6A8``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        emoji_status (:obj:`EmojiStatus<typegram.api.ayiin.EmojiStatus>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "emoji_status"]

    ID = 0xf0d3e6a8
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", emoji_status: "ayiin.EmojiStatus") -> None:
        
                self.channel = channel  # InputChannel
        
                self.emoji_status = emoji_status  # EmojiStatus

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEmojiStatus":
        # No flags
        
        channel = Object.read(b)
        
        emoji_status = Object.read(b)
        
        return UpdateEmojiStatus(channel=channel, emoji_status=emoji_status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.emoji_status.write())
        
        return b.getvalue()