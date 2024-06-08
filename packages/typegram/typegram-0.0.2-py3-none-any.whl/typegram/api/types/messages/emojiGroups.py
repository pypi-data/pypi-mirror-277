
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



class EmojiGroups(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.messages.EmojiGroups`.

    Details:
        - Layer: ``181``
        - ID: ``881FB94B``

hash (``int`` ``32-bit``):
                    N/A
                
        groups (List of :obj:`EmojiGroup<typegram.api.ayiin.EmojiGroup>`):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.getEmojiGroups
            messages.getEmojiStatusGroups
            messages.getEmojiProfilePhotoGroups
            messages.getEmojiStickerGroups
    """

    __slots__: List[str] = ["hash", "groups"]

    ID = 0x881fb94b
    QUALNAME = "types.messages.emojiGroups"

    def __init__(self, *, hash: int, groups: List["api.ayiin.EmojiGroup"]) -> None:
        
                self.hash = hash  # int
        
                self.groups = groups  # EmojiGroup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiGroups":
        # No flags
        
        hash = Int.read(b)
        
        groups = Object.read(b)
        
        return EmojiGroups(hash=hash, groups=groups)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.groups))
        
        return b.getvalue()