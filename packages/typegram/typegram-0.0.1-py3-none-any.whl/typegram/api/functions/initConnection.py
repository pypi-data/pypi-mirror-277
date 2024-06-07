
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



class InitConnection(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``C1CD5EA9``

api_id (``int`` ``32-bit``):
                    N/A
                
        device_model (``str``):
                    N/A
                
        system_version (``str``):
                    N/A
                
        app_version (``str``):
                    N/A
                
        system_lang_code (``str``):
                    N/A
                
        lang_pack (``str``):
                    N/A
                
        lang_code (``str``):
                    N/A
                
        query (``!x``):
                    N/A
                
        proxy (:obj:`InputClientProxy<typegram.api.ayiin.InputClientProxy>`, *optional*):
                    N/A
                
        params (:obj:`JSONValue<typegram.api.ayiin.JSONValue>`, *optional*):
                    N/A
                
    Returns:
        Any object from :obj:`~typegram.api.types`
    """

    __slots__: List[str] = ["api_id", "device_model", "system_version", "app_version", "system_lang_code", "lang_pack", "lang_code", "query", "proxy", "params"]

    ID = 0xc1cd5ea9
    QUALNAME = "functions.functions.X"

    def __init__(self, *, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: bytes, proxy: "ayiin.InputClientProxy" = None, params: "ayiin.JSONValue" = None) -> None:
        
                self.api_id = api_id  # int
        
                self.device_model = device_model  # string
        
                self.system_version = system_version  # string
        
                self.app_version = app_version  # string
        
                self.system_lang_code = system_lang_code  # string
        
                self.lang_pack = lang_pack  # string
        
                self.lang_code = lang_code  # string
        
                self.query = query  # !X
        
                self.proxy = proxy  # InputClientProxy
        
                self.params = params  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitConnection":
        
        flags = Int.read(b)
        
        api_id = Int.read(b)
        
        device_model = String.read(b)
        
        system_version = String.read(b)
        
        app_version = String.read(b)
        
        system_lang_code = String.read(b)
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        proxy = Object.read(b) if flags & (1 << 0) else None
        
        params = Object.read(b) if flags & (1 << 1) else None
        
        query = !X.read(b)
        
        return InitConnection(api_id=api_id, device_model=device_model, system_version=system_version, app_version=app_version, system_lang_code=system_lang_code, lang_pack=lang_pack, lang_code=lang_code, query=query, proxy=proxy, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.device_model))
        
        b.write(String(self.system_version))
        
        b.write(String(self.app_version))
        
        b.write(String(self.system_lang_code))
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        if self.proxy is not None:
            b.write(self.proxy.write())
        
        if self.params is not None:
            b.write(self.params.write())
        
        b.write(!X(self.query))
        
        return b.getvalue()