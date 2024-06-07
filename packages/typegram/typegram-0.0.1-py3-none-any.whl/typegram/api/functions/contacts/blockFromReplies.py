
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



class BlockFromReplies(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``29A8962C``

msg_id (``int`` ``32-bit``):
                    N/A
                
        delete_message (``bool``, *optional*):
                    N/A
                
        delete_history (``bool``, *optional*):
                    N/A
                
        report_spam (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["msg_id", "delete_message", "delete_history", "report_spam"]

    ID = 0x29a8962c
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, msg_id: int, delete_message: Optional[bool] = None, delete_history: Optional[bool] = None, report_spam: Optional[bool] = None) -> None:
        
                self.msg_id = msg_id  # int
        
                self.delete_message = delete_message  # true
        
                self.delete_history = delete_history  # true
        
                self.report_spam = report_spam  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BlockFromReplies":
        
        flags = Int.read(b)
        
        delete_message = True if flags & (1 << 0) else False
        delete_history = True if flags & (1 << 1) else False
        report_spam = True if flags & (1 << 2) else False
        msg_id = Int.read(b)
        
        return BlockFromReplies(msg_id=msg_id, delete_message=delete_message, delete_history=delete_history, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()