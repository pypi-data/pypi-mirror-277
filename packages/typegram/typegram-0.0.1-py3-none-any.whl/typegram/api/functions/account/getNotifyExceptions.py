
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



class GetNotifyExceptions(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``53577479``

compare_sound (``bool``, *optional*):
                    N/A
                
        compare_stories (``bool``, *optional*):
                    N/A
                
        peer (:obj:`InputNotifyPeer<typegram.api.ayiin.InputNotifyPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["compare_sound", "compare_stories", "peer"]

    ID = 0x53577479
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: "ayiin.InputNotifyPeer" = None) -> None:
        
                self.compare_sound = compare_sound  # true
        
                self.compare_stories = compare_stories  # true
        
                self.peer = peer  # InputNotifyPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetNotifyExceptions":
        
        flags = Int.read(b)
        
        compare_sound = True if flags & (1 << 1) else False
        compare_stories = True if flags & (1 << 2) else False
        peer = Object.read(b) if flags & (1 << 0) else None
        
        return GetNotifyExceptions(compare_sound=compare_sound, compare_stories=compare_stories, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        return b.getvalue()