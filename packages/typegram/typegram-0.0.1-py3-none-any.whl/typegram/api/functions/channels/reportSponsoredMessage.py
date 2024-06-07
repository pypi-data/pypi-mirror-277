
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



class ReportSponsoredMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``AF8FF6B9``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        random_id (``bytes``):
                    N/A
                
        option (``bytes``):
                    N/A
                
    Returns:
        :obj:`channels.SponsoredMessageReportResult<typegram.api.ayiin.channels.SponsoredMessageReportResult>`
    """

    __slots__: List[str] = ["channel", "random_id", "option"]

    ID = 0xaf8ff6b9
    QUALNAME = "functions.functionschannels.SponsoredMessageReportResult"

    def __init__(self, *, channel: "ayiin.InputChannel", random_id: bytes, option: bytes) -> None:
        
                self.channel = channel  # InputChannel
        
                self.random_id = random_id  # bytes
        
                self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportSponsoredMessage":
        # No flags
        
        channel = Object.read(b)
        
        random_id = Bytes.read(b)
        
        option = Bytes.read(b)
        
        return ReportSponsoredMessage(channel=channel, random_id=random_id, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bytes(self.random_id))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()