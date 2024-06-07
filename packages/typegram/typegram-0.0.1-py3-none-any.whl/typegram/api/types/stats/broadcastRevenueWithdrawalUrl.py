
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



class BroadcastRevenueWithdrawalUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.stats.BroadcastRevenueWithdrawalUrl`.

    Details:
        - Layer: ``181``
        - ID: ``EC659737``

url (``str``):
                    N/A
                
    Functions:
        This object can be returned by 35 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            stats.BroadcastStats
            stats.MegagroupStats
            stats.PublicForwards
            stats.MessageStats
            stats.StoryStats
            stats.BroadcastRevenueStats
            stats.BroadcastRevenueWithdrawalUrl
            stats.BroadcastRevenueTransactions
    """

    __slots__: List[str] = ["url"]

    ID = 0xec659737
    QUALNAME = "functions.typesstats.BroadcastRevenueWithdrawalUrl"

    def __init__(self, *, url: str) -> None:
        
                self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueWithdrawalUrl":
        # No flags
        
        url = String.read(b)
        
        return BroadcastRevenueWithdrawalUrl(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()