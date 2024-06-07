
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



class Status(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.smsjobs.Status`.

    Details:
        - Layer: ``181``
        - ID: ``2AEE9191``

recent_sent (``int`` ``32-bit``):
                    N/A
                
        recent_since (``int`` ``32-bit``):
                    N/A
                
        recent_remains (``int`` ``32-bit``):
                    N/A
                
        total_sent (``int`` ``32-bit``):
                    N/A
                
        total_since (``int`` ``32-bit``):
                    N/A
                
        terms_url (``str``):
                    N/A
                
        allow_international (``bool``, *optional*):
                    N/A
                
        last_gift_slug (``str``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["recent_sent", "recent_since", "recent_remains", "total_sent", "total_since", "terms_url", "allow_international", "last_gift_slug"]

    ID = 0x2aee9191
    QUALNAME = "functions.typessmsjobs.Status"

    def __init__(self, *, recent_sent: int, recent_since: int, recent_remains: int, total_sent: int, total_since: int, terms_url: str, allow_international: Optional[bool] = None, last_gift_slug: Optional[str] = None) -> None:
        
                self.recent_sent = recent_sent  # int
        
                self.recent_since = recent_since  # int
        
                self.recent_remains = recent_remains  # int
        
                self.total_sent = total_sent  # int
        
                self.total_since = total_since  # int
        
                self.terms_url = terms_url  # string
        
                self.allow_international = allow_international  # true
        
                self.last_gift_slug = last_gift_slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Status":
        
        flags = Int.read(b)
        
        allow_international = True if flags & (1 << 0) else False
        recent_sent = Int.read(b)
        
        recent_since = Int.read(b)
        
        recent_remains = Int.read(b)
        
        total_sent = Int.read(b)
        
        total_since = Int.read(b)
        
        last_gift_slug = String.read(b) if flags & (1 << 1) else None
        terms_url = String.read(b)
        
        return Status(recent_sent=recent_sent, recent_since=recent_since, recent_remains=recent_remains, total_sent=total_sent, total_since=total_since, terms_url=terms_url, allow_international=allow_international, last_gift_slug=last_gift_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.recent_sent))
        
        b.write(Int(self.recent_since))
        
        b.write(Int(self.recent_remains))
        
        b.write(Int(self.total_sent))
        
        b.write(Int(self.total_since))
        
        if self.last_gift_slug is not None:
            b.write(String(self.last_gift_slug))
        
        b.write(String(self.terms_url))
        
        return b.getvalue()