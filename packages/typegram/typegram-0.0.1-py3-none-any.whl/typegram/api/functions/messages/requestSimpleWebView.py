
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



class RequestSimpleWebView(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``1A46500A``

bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        platform (``str``):
                    N/A
                
        from_switch_webview (``bool``, *optional*):
                    N/A
                
        from_side_menu (``bool``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        start_param (``str``, *optional*):
                    N/A
                
        theme_params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
    Returns:
        :obj:`SimpleWebViewResult<typegram.api.ayiin.SimpleWebViewResult>`
    """

    __slots__: List[str] = ["bot", "platform", "from_switch_webview", "from_side_menu", "url", "start_param", "theme_params"]

    ID = 0x1a46500a
    QUALNAME = "functions.functions.SimpleWebViewResult"

    def __init__(self, *, bot: "ayiin.InputUser", platform: str, from_switch_webview: Optional[bool] = None, from_side_menu: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: "ayiin.DataJSON" = None) -> None:
        
                self.bot = bot  # InputUser
        
                self.platform = platform  # string
        
                self.from_switch_webview = from_switch_webview  # true
        
                self.from_side_menu = from_side_menu  # true
        
                self.url = url  # string
        
                self.start_param = start_param  # string
        
                self.theme_params = theme_params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestSimpleWebView":
        
        flags = Int.read(b)
        
        from_switch_webview = True if flags & (1 << 1) else False
        from_side_menu = True if flags & (1 << 2) else False
        bot = Object.read(b)
        
        url = String.read(b) if flags & (1 << 3) else None
        start_param = String.read(b) if flags & (1 << 4) else None
        theme_params = Object.read(b) if flags & (1 << 0) else None
        
        platform = String.read(b)
        
        return RequestSimpleWebView(bot=bot, platform=platform, from_switch_webview=from_switch_webview, from_side_menu=from_side_menu, url=url, start_param=start_param, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        return b.getvalue()