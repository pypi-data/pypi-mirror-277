
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



class GroupCallStreamChannels(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.GroupCallStreamChannels`.

    Details:
        - Layer: ``181``
        - ID: ``D0E482B2``

channels (List of :obj:`GroupCallStreamChannel<typegram.api.ayiin.GroupCallStreamChannel>`):
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

    __slots__: List[str] = ["channels"]

    ID = 0xd0e482b2
    QUALNAME = "functions.typesphone.GroupCallStreamChannels"

    def __init__(self, *, channels: List["ayiin.GroupCallStreamChannel"]) -> None:
        
                self.channels = channels  # GroupCallStreamChannel

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannels":
        # No flags
        
        channels = Object.read(b)
        
        return GroupCallStreamChannels(channels=channels)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.channels))
        
        return b.getvalue()