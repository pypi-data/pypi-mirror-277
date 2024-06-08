
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



class UpdateGroupCallConnection(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B783982``

params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        presentation (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["params", "presentation"]

    ID = 0xb783982
    QUALNAME = "types.updateGroupCallConnection"

    def __init__(self, *, params: "api.ayiin.DataJSON", presentation: Optional[bool] = None) -> None:
        
                self.params = params  # DataJSON
        
                self.presentation = presentation  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallConnection":
        
        flags = Int.read(b)
        
        presentation = True if flags & (1 << 0) else False
        params = Object.read(b)
        
        return UpdateGroupCallConnection(params=params, presentation=presentation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.params.write())
        
        return b.getvalue()