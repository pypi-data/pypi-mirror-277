
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



class ReplyKeyboardForceReply(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``86B40B08``

single_use (``bool``, *optional*):
                    N/A
                
        selective (``bool``, *optional*):
                    N/A
                
        placeholder (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["single_use", "selective", "placeholder"]

    ID = 0x86b40b08
    QUALNAME = "types.replyKeyboardForceReply"

    def __init__(self, *, single_use: Optional[bool] = None, selective: Optional[bool] = None, placeholder: Optional[str] = None) -> None:
        
                self.single_use = single_use  # true
        
                self.selective = selective  # true
        
                self.placeholder = placeholder  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardForceReply":
        
        flags = Int.read(b)
        
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardForceReply(single_use=single_use, selective=selective, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()