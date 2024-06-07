
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



class RequestAppWebView(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``8C5A3B3C``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        app (:obj:`InputBotApp<typegram.api.ayiin.InputBotApp>`):
                    N/A
                
        platform (``str``):
                    N/A
                
        write_allowed (``bool``, *optional*):
                    N/A
                
        start_param (``str``, *optional*):
                    N/A
                
        theme_params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
    Returns:
        :obj:`AppWebViewResult<typegram.api.ayiin.AppWebViewResult>`
    """

    __slots__: List[str] = ["peer", "app", "platform", "write_allowed", "start_param", "theme_params"]

    ID = 0x8c5a3b3c
    QUALNAME = "functions.functions.AppWebViewResult"

    def __init__(self, *, peer: "ayiin.InputPeer", app: "ayiin.InputBotApp", platform: str, write_allowed: Optional[bool] = None, start_param: Optional[str] = None, theme_params: "ayiin.DataJSON" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.app = app  # InputBotApp
        
                self.platform = platform  # string
        
                self.write_allowed = write_allowed  # true
        
                self.start_param = start_param  # string
        
                self.theme_params = theme_params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestAppWebView":
        
        flags = Int.read(b)
        
        write_allowed = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        app = Object.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        theme_params = Object.read(b) if flags & (1 << 2) else None
        
        platform = String.read(b)
        
        return RequestAppWebView(peer=peer, app=app, platform=platform, write_allowed=write_allowed, start_param=start_param, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.app.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        return b.getvalue()