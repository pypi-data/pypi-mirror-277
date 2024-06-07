
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



class ExportMessageLink(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``E63FADEB``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        id (``int`` ``32-bit``):
                    N/A
                
        grouped (``bool``, *optional*):
                    N/A
                
        thread (``bool``, *optional*):
                    N/A
                
    Returns:
        :obj:`ExportedMessageLink<typegram.api.ayiin.ExportedMessageLink>`
    """

    __slots__: List[str] = ["channel", "id", "grouped", "thread"]

    ID = 0xe63fadeb
    QUALNAME = "functions.functions.ExportedMessageLink"

    def __init__(self, *, channel: "ayiin.InputChannel", id: int, grouped: Optional[bool] = None, thread: Optional[bool] = None) -> None:
        
                self.channel = channel  # InputChannel
        
                self.id = id  # int
        
                self.grouped = grouped  # true
        
                self.thread = thread  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportMessageLink":
        
        flags = Int.read(b)
        
        grouped = True if flags & (1 << 0) else False
        thread = True if flags & (1 << 1) else False
        channel = Object.read(b)
        
        id = Int.read(b)
        
        return ExportMessageLink(channel=channel, id=id, grouped=grouped, thread=thread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()