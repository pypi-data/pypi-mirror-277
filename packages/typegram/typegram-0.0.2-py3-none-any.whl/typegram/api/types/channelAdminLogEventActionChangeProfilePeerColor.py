
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



class ChannelAdminLogEventActionChangeProfilePeerColor(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``5E477B25``

prev_value (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`):
                    N/A
                
        new_value (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`):
                    N/A
                
    """

    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x5e477b25
    QUALNAME = "types.channelAdminLogEventActionChangeProfilePeerColor"

    def __init__(self, *, prev_value: "api.ayiin.PeerColor", new_value: "api.ayiin.PeerColor") -> None:
        
                self.prev_value = prev_value  # PeerColor
        
                self.new_value = new_value  # PeerColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeProfilePeerColor":
        # No flags
        
        prev_value = Object.read(b)
        
        new_value = Object.read(b)
        
        return ChannelAdminLogEventActionChangeProfilePeerColor(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()