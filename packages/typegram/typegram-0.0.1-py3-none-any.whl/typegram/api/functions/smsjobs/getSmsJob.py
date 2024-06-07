
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



class GetSmsJob(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``778D902F``

job_id (``str``):
                    N/A
                
    Returns:
        :obj:`SmsJob<typegram.api.ayiin.SmsJob>`
    """

    __slots__: List[str] = ["job_id"]

    ID = 0x778d902f
    QUALNAME = "functions.functions.SmsJob"

    def __init__(self, *, job_id: str) -> None:
        
                self.job_id = job_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSmsJob":
        # No flags
        
        job_id = String.read(b)
        
        return GetSmsJob(job_id=job_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.job_id))
        
        return b.getvalue()