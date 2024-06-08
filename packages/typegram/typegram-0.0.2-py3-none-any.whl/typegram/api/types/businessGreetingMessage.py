
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



class BusinessGreetingMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BusinessGreetingMessage`.

    Details:
        - Layer: ``181``
        - ID: ``E519ABAB``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        recipients (:obj:`BusinessRecipients<typegram.api.ayiin.BusinessRecipients>`):
                    N/A
                
        no_activity_days (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["shortcut_id", "recipients", "no_activity_days"]

    ID = 0xe519abab
    QUALNAME = "types.businessGreetingMessage"

    def __init__(self, *, shortcut_id: int, recipients: "api.ayiin.BusinessRecipients", no_activity_days: int) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.recipients = recipients  # BusinessRecipients
        
                self.no_activity_days = no_activity_days  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessGreetingMessage":
        # No flags
        
        shortcut_id = Int.read(b)
        
        recipients = Object.read(b)
        
        no_activity_days = Int.read(b)
        
        return BusinessGreetingMessage(shortcut_id=shortcut_id, recipients=recipients, no_activity_days=no_activity_days)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(self.recipients.write())
        
        b.write(Int(self.no_activity_days))
        
        return b.getvalue()