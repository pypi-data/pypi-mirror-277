
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



class SetPrivacy(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``C9F81CE8``

key (:obj:`InputPrivacyKey<typegram.api.ayiin.InputPrivacyKey>`):
                    N/A
                
        rules (List of :obj:`InputPrivacyRule<typegram.api.ayiin.InputPrivacyRule>`):
                    N/A
                
    Returns:
        :obj:`account.PrivacyRules<typegram.api.ayiin.account.PrivacyRules>`
    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xc9f81ce8
    QUALNAME = "functions.functionsaccount.PrivacyRules"

    def __init__(self, *, key: "ayiin.InputPrivacyKey", rules: List["ayiin.InputPrivacyRule"]) -> None:
        
                self.key = key  # InputPrivacyKey
        
                self.rules = rules  # InputPrivacyRule

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetPrivacy":
        # No flags
        
        key = Object.read(b)
        
        rules = Object.read(b)
        
        return SetPrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()