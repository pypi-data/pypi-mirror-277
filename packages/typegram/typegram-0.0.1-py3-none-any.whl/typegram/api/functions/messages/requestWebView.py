
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



class RequestWebView(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``269DC2C1``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        platform (``str``):
                    N/A
                
        from_bot_menu (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        url (``str``, *optional*):
                    N/A
                
        start_param (``str``, *optional*):
                    N/A
                
        theme_params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        send_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        :obj:`WebViewResult<typegram.api.ayiin.WebViewResult>`
    """

    __slots__: List[str] = ["peer", "bot", "platform", "from_bot_menu", "silent", "url", "start_param", "theme_params", "reply_to", "send_as"]

    ID = 0x269dc2c1
    QUALNAME = "functions.functions.WebViewResult"

    def __init__(self, *, peer: "ayiin.InputPeer", bot: "ayiin.InputUser", platform: str, from_bot_menu: Optional[bool] = None, silent: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: "ayiin.DataJSON" = None, reply_to: "ayiin.InputReplyTo" = None, send_as: "ayiin.InputPeer" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.bot = bot  # InputUser
        
                self.platform = platform  # string
        
                self.from_bot_menu = from_bot_menu  # true
        
                self.silent = silent  # true
        
                self.url = url  # string
        
                self.start_param = start_param  # string
        
                self.theme_params = theme_params  # DataJSON
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestWebView":
        
        flags = Int.read(b)
        
        from_bot_menu = True if flags & (1 << 4) else False
        silent = True if flags & (1 << 5) else False
        peer = Object.read(b)
        
        bot = Object.read(b)
        
        url = String.read(b) if flags & (1 << 1) else None
        start_param = String.read(b) if flags & (1 << 3) else None
        theme_params = Object.read(b) if flags & (1 << 2) else None
        
        platform = String.read(b)
        
        reply_to = Object.read(b) if flags & (1 << 0) else None
        
        send_as = Object.read(b) if flags & (1 << 13) else None
        
        return RequestWebView(peer=peer, bot=bot, platform=platform, from_bot_menu=from_bot_menu, silent=silent, url=url, start_param=start_param, theme_params=theme_params, reply_to=reply_to, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()