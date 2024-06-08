
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



class InputBusinessBotRecipients(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBusinessBotRecipients`.

    Details:
        - Layer: ``181``
        - ID: ``C4E5921E``

existing_chats (``bool``, *optional*):
                    N/A
                
        new_chats (``bool``, *optional*):
                    N/A
                
        contacts (``bool``, *optional*):
                    N/A
                
        non_contacts (``bool``, *optional*):
                    N/A
                
        exclude_selected (``bool``, *optional*):
                    N/A
                
        users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
        exclude_users (List of :obj:`InputUser<typegram.api.ayiin.InputUser>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["existing_chats", "new_chats", "contacts", "non_contacts", "exclude_selected", "users", "exclude_users"]

    ID = 0xc4e5921e
    QUALNAME = "types.inputBusinessBotRecipients"

    def __init__(self, *, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List["api.ayiin.InputUser"]] = None, exclude_users: Optional[List["api.ayiin.InputUser"]] = None) -> None:
        
                self.existing_chats = existing_chats  # true
        
                self.new_chats = new_chats  # true
        
                self.contacts = contacts  # true
        
                self.non_contacts = non_contacts  # true
        
                self.exclude_selected = exclude_selected  # true
        
                self.users = users  # InputUser
        
                self.exclude_users = exclude_users  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessBotRecipients":
        
        flags = Int.read(b)
        
        existing_chats = True if flags & (1 << 0) else False
        new_chats = True if flags & (1 << 1) else False
        contacts = True if flags & (1 << 2) else False
        non_contacts = True if flags & (1 << 3) else False
        exclude_selected = True if flags & (1 << 5) else False
        users = Object.read(b) if flags & (1 << 4) else []
        
        exclude_users = Object.read(b) if flags & (1 << 6) else []
        
        return InputBusinessBotRecipients(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users, exclude_users=exclude_users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.users is not None:
            b.write(Vector(self.users))
        
        if self.exclude_users is not None:
            b.write(Vector(self.exclude_users))
        
        return b.getvalue()