
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



class Authorizations(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.Authorizations`.

    Details:
        - Layer: ``181``
        - ID: ``4BFF8EA0``

authorization_ttl_days (``int`` ``32-bit``):
                    N/A
                
        authorizations (List of :obj:`Authorization<typegram.api.ayiin.Authorization>`):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.WallPapers
            account.PrivacyRules
            account.PasswordSettings
            account.TmpPassword
            account.AuthorizationForm
            account.SentEmailCode
            account.EmailVerified
            account.Takeout
            account.Themes
            account.SavedRingtones
            account.SavedRingtone
            account.EmojiStatuses
            account.ResolvedBusinessChatLinks
    """

    __slots__: List[str] = ["authorization_ttl_days", "authorizations"]

    ID = 0x4bff8ea0
    QUALNAME = "functions.typesaccount.Authorizations"

    def __init__(self, *, authorization_ttl_days: int, authorizations: List["ayiin.Authorization"]) -> None:
        
                self.authorization_ttl_days = authorization_ttl_days  # int
        
                self.authorizations = authorizations  # Authorization

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorizations":
        # No flags
        
        authorization_ttl_days = Int.read(b)
        
        authorizations = Object.read(b)
        
        return Authorizations(authorization_ttl_days=authorization_ttl_days, authorizations=authorizations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.authorization_ttl_days))
        
        b.write(Vector(self.authorizations))
        
        return b.getvalue()