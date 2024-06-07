
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



class ChannelDifferenceTooLong(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.updates.ChannelDifference`.

    Details:
        - Layer: ``181``
        - ID: ``A4BCC6FE``

dialog (:obj:`Dialog<typegram.api.ayiin.Dialog>`):
                    N/A
                
        messages (List of :obj:`Message<typegram.api.ayiin.Message>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        final (``bool``, *optional*):
                    N/A
                
        timeout (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            updates.Difference
            updates.ChannelDifference
    """

    __slots__: List[str] = ["dialog", "messages", "chats", "users", "final", "timeout"]

    ID = 0xa4bcc6fe
    QUALNAME = "functions.typesupdates.ChannelDifference"

    def __init__(self, *, dialog: "ayiin.Dialog", messages: List["ayiin.Message"], chats: List["ayiin.Chat"], users: List["ayiin.User"], final: Optional[bool] = None, timeout: Optional[int] = None) -> None:
        
                self.dialog = dialog  # Dialog
        
                self.messages = messages  # Message
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.final = final  # true
        
                self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelDifferenceTooLong":
        
        flags = Int.read(b)
        
        final = True if flags & (1 << 0) else False
        timeout = Int.read(b) if flags & (1 << 1) else None
        dialog = Object.read(b)
        
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChannelDifferenceTooLong(dialog=dialog, messages=messages, chats=chats, users=users, final=final, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        b.write(self.dialog.write())
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()