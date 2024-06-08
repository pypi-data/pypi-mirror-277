
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



class EmojiList(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.EmojiList`.

    Details:
        - Layer: ``181``
        - ID: ``7A1E11D1``

hash (``int`` ``64-bit``):
                    N/A
                
        document_id (List of ``int`` ``64-bit``):
                    N/A
                
    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getDefaultProfilePhotoEmojis
            account.getDefaultGroupPhotoEmojis
            account.getDefaultBackgroundEmojis
            account.getChannelRestrictedStatusEmojis
            messages.searchCustomEmoji
    """

    __slots__: List[str] = ["hash", "document_id"]

    ID = 0x7a1e11d1
    QUALNAME = "types.emojiList"

    def __init__(self, *, hash: int, document_id: List[int]) -> None:
        
                self.hash = hash  # long
        
                self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiList":
        # No flags
        
        hash = Long.read(b)
        
        document_id = Object.read(b, Long)
        
        return EmojiList(hash=hash, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.document_id, Long))
        
        return b.getvalue()