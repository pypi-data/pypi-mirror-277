
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



class ExportedChatlistInvite(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.chatlists.ExportedChatlistInvite`.

    Details:
        - Layer: ``181``
        - ID: ``10E6E3A6``

filter (:obj:`DialogFilter<typegram.api.ayiin.DialogFilter>`):
                    N/A
                
        invite (:obj:`ExportedChatlistInvite<typegram.api.ayiin.ExportedChatlistInvite>`):
                    N/A
                
    Functions:
        This object can be returned by 32 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            chatlists.ExportedChatlistInvite
            chatlists.ExportedInvites
            chatlists.ChatlistInvite
            chatlists.ChatlistUpdates
    """

    __slots__: List[str] = ["filter", "invite"]

    ID = 0x10e6e3a6
    QUALNAME = "functions.typeschatlists.ExportedChatlistInvite"

    def __init__(self, *, filter: "ayiin.DialogFilter", invite: "ayiin.ExportedChatlistInvite") -> None:
        
                self.filter = filter  # DialogFilter
        
                self.invite = invite  # ExportedChatlistInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatlistInvite":
        # No flags
        
        filter = Object.read(b)
        
        invite = Object.read(b)
        
        return ExportedChatlistInvite(filter=filter, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.filter.write())
        
        b.write(self.invite.write())
        
        return b.getvalue()