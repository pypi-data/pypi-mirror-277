
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



class BusinessRecipients(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessRecipients`.

    Details:
        - Layer: ``181``
        - ID: ``21108FF7``

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
                
        users (List of ``int`` ``64-bit``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["existing_chats", "new_chats", "contacts", "non_contacts", "exclude_selected", "users"]

    ID = 0x21108ff7
    QUALNAME = "types.businessRecipients"

    def __init__(self, *, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None) -> None:
        
                self.existing_chats = existing_chats  # true
        
                self.new_chats = new_chats  # true
        
                self.contacts = contacts  # true
        
                self.non_contacts = non_contacts  # true
        
                self.exclude_selected = exclude_selected  # true
        
                self.users = users  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessRecipients":
        
        flags = Int.read(b)
        
        existing_chats = True if flags & (1 << 0) else False
        new_chats = True if flags & (1 << 1) else False
        contacts = True if flags & (1 << 2) else False
        non_contacts = True if flags & (1 << 3) else False
        exclude_selected = True if flags & (1 << 5) else False
        users = Object.read(b, Long) if flags & (1 << 4) else []
        
        return BusinessRecipients(existing_chats=existing_chats, new_chats=new_chats, contacts=contacts, non_contacts=non_contacts, exclude_selected=exclude_selected, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.users is not None:
            b.write(Vector(self.users, Long))
        
        return b.getvalue()