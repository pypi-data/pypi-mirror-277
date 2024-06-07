
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



class Difference(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.Difference`.

    Details:
        - Layer: ``181``
        - ID: ``F49CA0``

new_messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        new_encrypted_messages (List of :obj:`EncryptedMessage<typegram.api.ayiin.EncryptedMessage>`):
                    N/A
                
        other_updates (List of :obj:`Update<typegram.api.ayiin.Update>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        state (:obj:`updates.State<typegram.api.ayiin.updates.State>`):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["new_messages", "new_encrypted_messages", "other_updates", "chats", "users", "state"]

    ID = 0xf49ca0
    QUALNAME = "functions.typesupdates.Difference"

    def __init__(self, *, new_messages: List["ayiin.Message"], new_encrypted_messages: List["ayiin.EncryptedMessage"], other_updates: List["ayiin.Update"], chats: List["ayiin.Chat"], users: List["ayiin.User"], state: "ayiinupdates.State") -> None:
        
                self.new_messages = new_messages  # Message
        
                self.new_encrypted_messages = new_encrypted_messages  # EncryptedMessage
        
                self.other_updates = other_updates  # Update
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.state = state  # updates.State

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Difference":
        # No flags
        
        new_messages = Object.read(b)
        
        new_encrypted_messages = Object.read(b)
        
        other_updates = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        state = Object.read(b)
        
        return Difference(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages, other_updates=other_updates, chats=chats, users=users, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.new_messages))
        
        b.write(Vector(self.new_encrypted_messages))
        
        b.write(Vector(self.other_updates))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(self.state.write())
        
        return b.getvalue()