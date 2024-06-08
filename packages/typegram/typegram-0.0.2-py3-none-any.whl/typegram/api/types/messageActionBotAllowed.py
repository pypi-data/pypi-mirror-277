
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



class MessageActionBotAllowed(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C516D679``

attach_menu (``bool``, *optional*):
                    N/A
                
        from_request (``bool``, *optional*):
                    N/A
                
        domain (``str``, *optional*):
                    N/A
                
        app (:obj:`BotApp<typegram.api.ayiin.BotApp>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["attach_menu", "from_request", "domain", "app"]

    ID = 0xc516d679
    QUALNAME = "types.messageActionBotAllowed"

    def __init__(self, *, attach_menu: Optional[bool] = None, from_request: Optional[bool] = None, domain: Optional[str] = None, app: "api.ayiin.BotApp" = None) -> None:
        
                self.attach_menu = attach_menu  # true
        
                self.from_request = from_request  # true
        
                self.domain = domain  # string
        
                self.app = app  # BotApp

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionBotAllowed":
        
        flags = Int.read(b)
        
        attach_menu = True if flags & (1 << 1) else False
        from_request = True if flags & (1 << 3) else False
        domain = String.read(b) if flags & (1 << 0) else None
        app = Object.read(b) if flags & (1 << 2) else None
        
        return MessageActionBotAllowed(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.domain is not None:
            b.write(String(self.domain))
        
        if self.app is not None:
            b.write(self.app.write())
        
        return b.getvalue()