
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



class InitHistoryImport(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``34090C3B``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        file (:obj:`InputFile<typegram.api.ayiin.InputFile>`):
                    N/A
                
        media_count (``int`` ``32-bit``):
                    N/A
                
    Returns:
        :obj:`messages.HistoryImport<typegram.api.ayiin.messages.HistoryImport>`
    """

    __slots__: List[str] = ["peer", "file", "media_count"]

    ID = 0x34090c3b
    QUALNAME = "functions.functionsmessages.HistoryImport"

    def __init__(self, *, peer: "ayiin.InputPeer", file: "ayiin.InputFile", media_count: int) -> None:
        
                self.peer = peer  # InputPeer
        
                self.file = file  # InputFile
        
                self.media_count = media_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitHistoryImport":
        # No flags
        
        peer = Object.read(b)
        
        file = Object.read(b)
        
        media_count = Int.read(b)
        
        return InitHistoryImport(peer=peer, file=file, media_count=media_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.file.write())
        
        b.write(Int(self.media_count))
        
        return b.getvalue()