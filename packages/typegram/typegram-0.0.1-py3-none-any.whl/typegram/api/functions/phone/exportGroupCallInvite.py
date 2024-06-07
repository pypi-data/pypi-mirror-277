
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



class ExportGroupCallInvite(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E6AA647F``

call (:obj:`InputGroupCall<typegram.api.ayiin.InputGroupCall>`):
                    N/A
                
        can_is_self_unmute (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`phone.ExportedGroupCallInvite<typegram.api.ayiin.phone.ExportedGroupCallInvite>`
    """

    __slots__: List[str] = ["call", "can_is_self_unmute"]

    ID = 0xe6aa647f
    QUALNAME = "functions.functionsphone.ExportedGroupCallInvite"

    def __init__(self, *, call: "ayiin.InputGroupCall", can_is_self_unmute: Optional[bool] = None) -> None:
        
                self.call = call  # InputGroupCall
        
                self.can_is_self_unmute = can_is_self_unmute  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportGroupCallInvite":
        
        flags = Int.read(b)
        
        can_is_self_unmute = True if flags & (1 << 0) else False
        call = Object.read(b)
        
        return ExportGroupCallInvite(call=call, can_is_self_unmute=can_is_self_unmute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        return b.getvalue()