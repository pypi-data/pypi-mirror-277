
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



class SmsJob(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SmsJob`.

    Details:
        - Layer: ``181``
        - ID: ``E6A1EEB8``

job_id (``str``):
                    N/A
                
        phone_number (``str``):
                    N/A
                
        text (``str``):
                    N/A
                
    Functions:
        This object can be returned by 6 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            smsjobs.getSmsJob
    """

    __slots__: List[str] = ["job_id", "phone_number", "text"]

    ID = 0xe6a1eeb8
    QUALNAME = "types.smsJob"

    def __init__(self, *, job_id: str, phone_number: str, text: str) -> None:
        
                self.job_id = job_id  # string
        
                self.phone_number = phone_number  # string
        
                self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SmsJob":
        # No flags
        
        job_id = String.read(b)
        
        phone_number = String.read(b)
        
        text = String.read(b)
        
        return SmsJob(job_id=job_id, phone_number=phone_number, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.job_id))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.text))
        
        return b.getvalue()