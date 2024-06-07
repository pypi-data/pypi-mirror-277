
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



class SetBotGroupDefaultAdminRights(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``925EC9EA``

admin_rights (:obj:`ChatAdminRights<typegram.api.ayiin.ChatAdminRights>`):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["admin_rights"]

    ID = 0x925ec9ea
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, admin_rights: "ayiin.ChatAdminRights") -> None:
        
                self.admin_rights = admin_rights  # ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotGroupDefaultAdminRights":
        # No flags
        
        admin_rights = Object.read(b)
        
        return SetBotGroupDefaultAdminRights(admin_rights=admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.admin_rights.write())
        
        return b.getvalue()