
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



class AutoDownloadSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.AutoDownloadSettings`.

    Details:
        - Layer: ``181``
        - ID: ``63CACF26``

low (:obj:`AutoDownloadSettings<typegram.api.ayiin.AutoDownloadSettings>`):
                    N/A
                
        medium (:obj:`AutoDownloadSettings<typegram.api.ayiin.AutoDownloadSettings>`):
                    N/A
                
        high (:obj:`AutoDownloadSettings<typegram.api.ayiin.AutoDownloadSettings>`):
                    N/A
                
    """

    __slots__: List[str] = ["low", "medium", "high"]

    ID = 0x63cacf26
    QUALNAME = "types.account.autoDownloadSettings"

    def __init__(self, *, low: "api.ayiin.AutoDownloadSettings", medium: "api.ayiin.AutoDownloadSettings", high: "api.ayiin.AutoDownloadSettings") -> None:
        
                self.low = low  # AutoDownloadSettings
        
                self.medium = medium  # AutoDownloadSettings
        
                self.high = high  # AutoDownloadSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoDownloadSettings":
        # No flags
        
        low = Object.read(b)
        
        medium = Object.read(b)
        
        high = Object.read(b)
        
        return AutoDownloadSettings(low=low, medium=medium, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.low.write())
        
        b.write(self.medium.write())
        
        b.write(self.high.write())
        
        return b.getvalue()