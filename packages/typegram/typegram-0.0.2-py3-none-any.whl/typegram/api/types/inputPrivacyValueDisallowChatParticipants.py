
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



class InputPrivacyValueDisallowChatParticipants(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPrivacyRule`.

    Details:
        - Layer: ``181``
        - ID: ``E94F0F86``

chats (List of ``int`` ``64-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["chats"]

    ID = 0xe94f0f86
    QUALNAME = "types.inputPrivacyValueDisallowChatParticipants"

    def __init__(self, *, chats: List[int]) -> None:
        
                self.chats = chats  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPrivacyValueDisallowChatParticipants":
        # No flags
        
        chats = Object.read(b, Long)
        
        return InputPrivacyValueDisallowChatParticipants(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.chats, Long))
        
        return b.getvalue()