
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



class PeerChat(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Peer`.

    Details:
        - Layer: ``181``
        - ID: ``36C6019A``

chat_id (``int`` ``64-bit``):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            chatlists.getLeaveChatlistSuggestions
    """

    __slots__: List[str] = ["chat_id"]

    ID = 0x36c6019a
    QUALNAME = "types.peerChat"

    def __init__(self, *, chat_id: int) -> None:
        
                self.chat_id = chat_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerChat":
        # No flags
        
        chat_id = Long.read(b)
        
        return PeerChat(chat_id=chat_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        return b.getvalue()