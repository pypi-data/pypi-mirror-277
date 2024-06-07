
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



class GetPrivacy(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``DADBC950``

key (:obj:`InputPrivacyKey<typegram.api.ayiin.InputPrivacyKey>`):
                    N/A
                
    Returns:
        :obj:`account.PrivacyRules<typegram.api.ayiin.account.PrivacyRules>`
    """

    __slots__: List[str] = ["key"]

    ID = 0xdadbc950
    QUALNAME = "functions.functionsaccount.PrivacyRules"

    def __init__(self, *, key: "ayiin.InputPrivacyKey") -> None:
        
                self.key = key  # InputPrivacyKey

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPrivacy":
        # No flags
        
        key = Object.read(b)
        
        return GetPrivacy(key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        return b.getvalue()