
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



class SetInlineBotResults(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``BB12A419``

query_id (``int`` ``64-bit``):
                    N/A
                
        results (List of :obj:`InputBotInlineResult<typegram.api.ayiin.InputBotInlineResult>`):
                    N/A
                
        cache_time (``int`` ``32-bit``):
                    N/A
                
        gallery (``bool``, *optional*):
                    N/A
                
        private (``bool``, *optional*):
                    N/A
                
        next_offset (``str``, *optional*):
                    N/A
                
        switch_pm (:obj:`InlineBotSwitchPM<typegram.api.ayiin.InlineBotSwitchPM>`, *optional*):
                    N/A
                
        switch_webview (:obj:`InlineBotWebView<typegram.api.ayiin.InlineBotWebView>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["query_id", "results", "cache_time", "gallery", "private", "next_offset", "switch_pm", "switch_webview"]

    ID = 0xbb12a419
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, query_id: int, results: List["ayiin.InputBotInlineResult"], cache_time: int, gallery: Optional[bool] = None, private: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: "ayiin.InlineBotSwitchPM" = None, switch_webview: "ayiin.InlineBotWebView" = None) -> None:
        
                self.query_id = query_id  # long
        
                self.results = results  # InputBotInlineResult
        
                self.cache_time = cache_time  # int
        
                self.gallery = gallery  # true
        
                self.private = private  # true
        
                self.next_offset = next_offset  # string
        
                self.switch_pm = switch_pm  # InlineBotSwitchPM
        
                self.switch_webview = switch_webview  # InlineBotWebView

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetInlineBotResults":
        
        flags = Int.read(b)
        
        gallery = True if flags & (1 << 0) else False
        private = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        results = Object.read(b)
        
        cache_time = Int.read(b)
        
        next_offset = String.read(b) if flags & (1 << 2) else None
        switch_pm = Object.read(b) if flags & (1 << 3) else None
        
        switch_webview = Object.read(b) if flags & (1 << 4) else None
        
        return SetInlineBotResults(query_id=query_id, results=results, cache_time=cache_time, gallery=gallery, private=private, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Vector(self.results))
        
        b.write(Int(self.cache_time))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        if self.switch_pm is not None:
            b.write(self.switch_pm.write())
        
        if self.switch_webview is not None:
            b.write(self.switch_webview.write())
        
        return b.getvalue()