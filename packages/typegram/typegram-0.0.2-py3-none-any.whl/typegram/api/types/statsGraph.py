
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



class StatsGraph(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StatsGraph`.

    Details:
        - Layer: ``181``
        - ID: ``8EA464B6``

json (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        zoom_token (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stats.loadAsyncGraph
    """

    __slots__: List[str] = ["json", "zoom_token"]

    ID = 0x8ea464b6
    QUALNAME = "types.statsGraph"

    def __init__(self, *, json: "api.ayiin.DataJSON", zoom_token: Optional[str] = None) -> None:
        
                self.json = json  # DataJSON
        
                self.zoom_token = zoom_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraph":
        
        flags = Int.read(b)
        
        json = Object.read(b)
        
        zoom_token = String.read(b) if flags & (1 << 0) else None
        return StatsGraph(json=json, zoom_token=zoom_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.json.write())
        
        if self.zoom_token is not None:
            b.write(String(self.zoom_token))
        
        return b.getvalue()