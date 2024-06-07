
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



class ToggleViewForumAsMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``9738BB15``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        enabled (``bool``):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x9738bb15
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", enabled: bool) -> None:
        
                self.channel = channel  # InputChannel
        
                self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleViewForumAsMessages":
        # No flags
        
        channel = Object.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleViewForumAsMessages(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()