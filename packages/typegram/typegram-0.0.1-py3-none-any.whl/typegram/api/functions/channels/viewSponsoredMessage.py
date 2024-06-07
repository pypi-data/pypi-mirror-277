
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



class ViewSponsoredMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BEAEDB94``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        random_id (``bytes``):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["channel", "random_id"]

    ID = 0xbeaedb94
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, channel: "ayiin.InputChannel", random_id: bytes) -> None:
        
                self.channel = channel  # InputChannel
        
                self.random_id = random_id  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ViewSponsoredMessage":
        # No flags
        
        channel = Object.read(b)
        
        random_id = Bytes.read(b)
        
        return ViewSponsoredMessage(channel=channel, random_id=random_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bytes(self.random_id))
        
        return b.getvalue()