
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



class UrlAuthResultRequest(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.UrlAuthResult`.

    Details:
        - Layer: ``181``
        - ID: ``92D33A0E``

bot (:obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        domain (``str``):
                    N/A
                
        request_write_access (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            messages.requestUrlAuth
            messages.acceptUrlAuth
    """

    __slots__: List[str] = ["bot", "domain", "request_write_access"]

    ID = 0x92d33a0e
    QUALNAME = "types.urlAuthResultRequest"

    def __init__(self, *, bot: "api.ayiin.User", domain: str, request_write_access: Optional[bool] = None) -> None:
        
                self.bot = bot  # User
        
                self.domain = domain  # string
        
                self.request_write_access = request_write_access  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UrlAuthResultRequest":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        bot = Object.read(b)
        
        domain = String.read(b)
        
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.domain))
        
        return b.getvalue()