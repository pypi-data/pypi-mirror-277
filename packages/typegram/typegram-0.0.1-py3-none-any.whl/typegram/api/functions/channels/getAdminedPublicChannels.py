
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



class GetAdminedPublicChannels(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``F8B036AF``

by_location (``bool``, *optional*):
                    N/A
                
        check_limit (``bool``, *optional*):
                    N/A
                
        for_personal (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.Chats<typegram.api.ayiin.messages.Chats>`
    """

    __slots__: List[str] = ["by_location", "check_limit", "for_personal"]

    ID = 0xf8b036af
    QUALNAME = "functions.functionsmessages.Chats"

    def __init__(self, *, by_location: Optional[bool] = None, check_limit: Optional[bool] = None, for_personal: Optional[bool] = None) -> None:
        
                self.by_location = by_location  # true
        
                self.check_limit = check_limit  # true
        
                self.for_personal = for_personal  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAdminedPublicChannels":
        
        flags = Int.read(b)
        
        by_location = True if flags & (1 << 0) else False
        check_limit = True if flags & (1 << 1) else False
        for_personal = True if flags & (1 << 2) else False
        return GetAdminedPublicChannels(by_location=by_location, check_limit=check_limit, for_personal=for_personal)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()