
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



class EditBanned(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``96E6CD81``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        participant (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["channel", "participant", "banned_rights"]

    ID = 0x96e6cd81
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, channel: "ayiin.InputChannel", participant: "ayiin.InputPeer", banned_rights: "ayiin.ChatBannedRights") -> None:
        
                self.channel = channel  # InputChannel
        
                self.participant = participant  # InputPeer
        
                self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBanned":
        # No flags
        
        channel = Object.read(b)
        
        participant = Object.read(b)
        
        banned_rights = Object.read(b)
        
        return EditBanned(channel=channel, participant=participant, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()