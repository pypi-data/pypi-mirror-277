
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



class ExportedGroupCallInvite(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.ExportedGroupCallInvite`.

    Details:
        - Layer: ``181``
        - ID: ``204BD158``

link (``str``):
                    N/A
                
    Functions:
        This object can be returned by 29 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            phone.PhoneCall
            phone.GroupCall
            phone.GroupParticipants
            phone.JoinAsPeers
            phone.ExportedGroupCallInvite
            phone.GroupCallStreamChannels
            phone.GroupCallStreamRtmpUrl
    """

    __slots__: List[str] = ["link"]

    ID = 0x204bd158
    QUALNAME = "functions.typesphone.ExportedGroupCallInvite"

    def __init__(self, *, link: str) -> None:
        
                self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedGroupCallInvite":
        # No flags
        
        link = String.read(b)
        
        return ExportedGroupCallInvite(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.link))
        
        return b.getvalue()