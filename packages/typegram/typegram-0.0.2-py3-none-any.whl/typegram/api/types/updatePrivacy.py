
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



class UpdatePrivacy(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``EE3B272A``

key (:obj:`PrivacyKey<typegram.api.ayiin.PrivacyKey>`):
                    N/A
                
        rules (List of :obj:`PrivacyRule<typegram.api.ayiin.PrivacyRule>`):
                    N/A
                
    """

    __slots__: List[str] = ["key", "rules"]

    ID = 0xee3b272a
    QUALNAME = "types.updatePrivacy"

    def __init__(self, *, key: "api.ayiin.PrivacyKey", rules: List["api.ayiin.PrivacyRule"]) -> None:
        
                self.key = key  # PrivacyKey
        
                self.rules = rules  # PrivacyRule

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePrivacy":
        # No flags
        
        key = Object.read(b)
        
        rules = Object.read(b)
        
        return UpdatePrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()