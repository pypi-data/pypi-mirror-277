
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



class SponsoredMessageReportResultChooseOption(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.channels.SponsoredMessageReportResult`.

    Details:
        - Layer: ``181``
        - ID: ``846F9E42``

title (``str``):
                    N/A
                
        options (List of :obj:`SponsoredMessageReportOption<typegram.api.ayiin.SponsoredMessageReportOption>`):
                    N/A
                
    Functions:
        This object can be returned by 37 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            channels.ChannelParticipants
            channels.ChannelParticipant
            channels.AdminLogResults
            channels.SendAsPeers
            channels.SponsoredMessageReportResult
    """

    __slots__: List[str] = ["title", "options"]

    ID = 0x846f9e42
    QUALNAME = "functions.typeschannels.SponsoredMessageReportResult"

    def __init__(self, *, title: str, options: List["ayiin.SponsoredMessageReportOption"]) -> None:
        
                self.title = title  # string
        
                self.options = options  # SponsoredMessageReportOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportResultChooseOption":
        # No flags
        
        title = String.read(b)
        
        options = Object.read(b)
        
        return SponsoredMessageReportResultChooseOption(title=title, options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.options))
        
        return b.getvalue()