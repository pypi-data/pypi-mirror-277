
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



class SaveAutoDownloadSettings(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``76F36233``

settings (:obj:`AutoDownloadSettings<typegram.api.ayiin.AutoDownloadSettings>`):
                    N/A
                
        low (``bool``, *optional*):
                    N/A
                
        high (``bool``, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["settings", "low", "high"]

    ID = 0x76f36233
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, settings: "ayiin.AutoDownloadSettings", low: Optional[bool] = None, high: Optional[bool] = None) -> None:
        
                self.settings = settings  # AutoDownloadSettings
        
                self.low = low  # true
        
                self.high = high  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAutoDownloadSettings":
        
        flags = Int.read(b)
        
        low = True if flags & (1 << 0) else False
        high = True if flags & (1 << 1) else False
        settings = Object.read(b)
        
        return SaveAutoDownloadSettings(settings=settings, low=low, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.settings.write())
        
        return b.getvalue()