
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



class InviteToChannel(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``C9E33D54``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
    Returns:
        :obj:`messages.InvitedUsers<typegram.api.ayiin.messages.InvitedUsers>`
    """

    __slots__: List[str] = ["channel", "users"]

    ID = 0xc9e33d54
    QUALNAME = "functions.functionsmessages.InvitedUsers"

    def __init__(self, *, channel: "ayiin.InputChannel", users: List["ayiin.InputUser"]) -> None:
        
                self.channel = channel  # InputChannel
        
                self.users = users  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InviteToChannel":
        # No flags
        
        channel = Object.read(b)
        
        users = Object.read(b)
        
        return InviteToChannel(channel=channel, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()