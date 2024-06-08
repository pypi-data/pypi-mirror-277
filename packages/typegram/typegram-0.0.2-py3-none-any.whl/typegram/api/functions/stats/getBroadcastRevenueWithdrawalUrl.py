
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



class GetBroadcastRevenueWithdrawalUrl(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2A65EF73``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        password (:obj:`InputCheckPasswordSRP<typegram.api.ayiin.InputCheckPasswordSRP>`):
                    N/A
                
    Returns:
        :obj:`stats.BroadcastRevenueWithdrawalUrl<typegram.api.ayiin.stats.BroadcastRevenueWithdrawalUrl>`
    """

    __slots__: List[str] = ["channel", "password"]

    ID = 0x2a65ef73
    QUALNAME = "functions.stats.getBroadcastRevenueWithdrawalUrl"

    def __init__(self, *, channel: "api.ayiin.InputChannel", password: "api.ayiin.InputCheckPasswordSRP") -> None:
        
                self.channel = channel  # InputChannel
        
                self.password = password  # InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBroadcastRevenueWithdrawalUrl":
        # No flags
        
        channel = Object.read(b)
        
        password = Object.read(b)
        
        return GetBroadcastRevenueWithdrawalUrl(channel=channel, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.password.write())
        
        return b.getvalue()