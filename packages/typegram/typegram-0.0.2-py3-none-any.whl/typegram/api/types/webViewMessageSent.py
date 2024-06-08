
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



class WebViewMessageSent(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WebViewMessageSent`.

    Details:
        - Layer: ``181``
        - ID: ``C94511C``

msg_id (:obj:`InputBotInlineMessageID<typegram.api.ayiin.InputBotInlineMessageID>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.sendWebViewResultMessage
    """

    __slots__: List[str] = ["msg_id"]

    ID = 0xc94511c
    QUALNAME = "types.webViewMessageSent"

    def __init__(self, *, msg_id: "api.ayiin.InputBotInlineMessageID" = None) -> None:
        
                self.msg_id = msg_id  # InputBotInlineMessageID

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebViewMessageSent":
        
        flags = Int.read(b)
        
        msg_id = Object.read(b) if flags & (1 << 0) else None
        
        return WebViewMessageSent(msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()