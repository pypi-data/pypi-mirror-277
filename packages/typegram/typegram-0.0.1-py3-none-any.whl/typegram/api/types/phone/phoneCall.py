
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



class PhoneCall(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``EC82E140``

phone_call (:obj:`PhoneCall<typegram.api.ayiin.PhoneCall>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["phone_call", "users"]

    ID = 0xec82e140
    QUALNAME = "functions.typesphone.PhoneCall"

    def __init__(self, *, phone_call: "ayiin.PhoneCall", users: List["ayiin.User"]) -> None:
        
                self.phone_call = phone_call  # PhoneCall
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCall":
        # No flags
        
        phone_call = Object.read(b)
        
        users = Object.read(b)
        
        return PhoneCall(phone_call=phone_call, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.phone_call.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()