
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



class MessageEntityBlockquote(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageEntity`.

    Details:
        - Layer: ``181``
        - ID: ``F1CCAAAC``

offset (``int`` ``32-bit``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
        collapsed (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["offset", "length", "collapsed"]

    ID = 0xf1ccaaac
    QUALNAME = "types.messageEntityBlockquote"

    def __init__(self, *, offset: int, length: int, collapsed: Optional[bool] = None) -> None:
        
                self.offset = offset  # int
        
                self.length = length  # int
        
                self.collapsed = collapsed  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityBlockquote":
        
        flags = Int.read(b)
        
        collapsed = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityBlockquote(offset=offset, length=length, collapsed=collapsed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()