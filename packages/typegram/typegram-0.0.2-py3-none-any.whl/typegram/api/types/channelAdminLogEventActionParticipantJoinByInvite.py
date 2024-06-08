
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



class ChannelAdminLogEventActionParticipantJoinByInvite(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``FE9FC158``

invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`):
                    N/A
                
        via_chatlist (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["invite", "via_chatlist"]

    ID = 0xfe9fc158
    QUALNAME = "types.channelAdminLogEventActionParticipantJoinByInvite"

    def __init__(self, *, invite: "api.ayiin.ExportedChatInvite", via_chatlist: Optional[bool] = None) -> None:
        
                self.invite = invite  # ExportedChatInvite
        
                self.via_chatlist = via_chatlist  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionParticipantJoinByInvite":
        
        flags = Int.read(b)
        
        via_chatlist = True if flags & (1 << 0) else False
        invite = Object.read(b)
        
        return ChannelAdminLogEventActionParticipantJoinByInvite(invite=invite, via_chatlist=via_chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.invite.write())
        
        return b.getvalue()