
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



class InputBusinessAwayMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputBusinessAwayMessage`.

    Details:
        - Layer: ``181``
        - ID: ``832175E0``

shortcut_id (``int`` ``32-bit``):
                    N/A
                
        schedule (:obj:`BusinessAwayMessageSchedule<typegram.api.ayiin.BusinessAwayMessageSchedule>`):
                    N/A
                
        recipients (:obj:`InputBusinessRecipients<typegram.api.ayiin.InputBusinessRecipients>`):
                    N/A
                
        offline_only (``bool``, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["shortcut_id", "schedule", "recipients", "offline_only"]

    ID = 0x832175e0
    QUALNAME = "types.inputBusinessAwayMessage"

    def __init__(self, *, shortcut_id: int, schedule: "api.ayiin.BusinessAwayMessageSchedule", recipients: "api.ayiin.InputBusinessRecipients", offline_only: Optional[bool] = None) -> None:
        
                self.shortcut_id = shortcut_id  # int
        
                self.schedule = schedule  # BusinessAwayMessageSchedule
        
                self.recipients = recipients  # InputBusinessRecipients
        
                self.offline_only = offline_only  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBusinessAwayMessage":
        
        flags = Int.read(b)
        
        offline_only = True if flags & (1 << 0) else False
        shortcut_id = Int.read(b)
        
        schedule = Object.read(b)
        
        recipients = Object.read(b)
        
        return InputBusinessAwayMessage(shortcut_id=shortcut_id, schedule=schedule, recipients=recipients, offline_only=offline_only)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.shortcut_id))
        
        b.write(self.schedule.write())
        
        b.write(self.recipients.write())
        
        return b.getvalue()