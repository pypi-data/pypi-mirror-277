
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



class GetChatlistUpdates(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``89419521``

chatlist (:obj:`InputChatlist<typegram.api.ayiin.InputChatlist>`):
                    N/A
                
    Returns:
        :obj:`chatlists.ChatlistUpdates<typegram.api.ayiin.chatlists.ChatlistUpdates>`
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0x89419521
    QUALNAME = "functions.chatlists.getChatlistUpdates"

    def __init__(self, *, chatlist: "api.ayiin.InputChatlist") -> None:
        
                self.chatlist = chatlist  # InputChatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatlistUpdates":
        # No flags
        
        chatlist = Object.read(b)
        
        return GetChatlistUpdates(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        return b.getvalue()