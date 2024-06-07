
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



class SendWebViewResultMessage(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``A4314F5``

bot_query_id (``str``):
                    N/A
                
        result (:obj:`InputBotInlineResult<typegram.api.ayiin.InputBotInlineResult>`):
                    N/A
                
    Returns:
        :obj:`WebViewMessageSent<typegram.api.ayiin.WebViewMessageSent>`
    """

    __slots__: List[str] = ["bot_query_id", "result"]

    ID = 0xa4314f5
    QUALNAME = "functions.functions.WebViewMessageSent"

    def __init__(self, *, bot_query_id: str, result: "ayiin.InputBotInlineResult") -> None:
        
                self.bot_query_id = bot_query_id  # string
        
                self.result = result  # InputBotInlineResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendWebViewResultMessage":
        # No flags
        
        bot_query_id = String.read(b)
        
        result = Object.read(b)
        
        return SendWebViewResultMessage(bot_query_id=bot_query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.bot_query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()