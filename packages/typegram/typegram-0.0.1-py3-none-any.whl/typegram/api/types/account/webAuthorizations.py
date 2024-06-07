
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



class WebAuthorizations(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.WebAuthorizations`.

    Details:
        - Layer: ``181``
        - ID: ``ED56C9FC``

authorizations (List of :obj:`WebAuthorization<typegram.api.ayiin.WebAuthorization>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 25 functions.

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

    __slots__: List[str] = ["authorizations", "users"]

    ID = 0xed56c9fc
    QUALNAME = "functions.typesaccount.WebAuthorizations"

    def __init__(self, *, authorizations: List["ayiin.WebAuthorization"], users: List["ayiin.User"]) -> None:
        
                self.authorizations = authorizations  # WebAuthorization
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorizations":
        # No flags
        
        authorizations = Object.read(b)
        
        users = Object.read(b)
        
        return WebAuthorizations(authorizations=authorizations, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.authorizations))
        
        b.write(Vector(self.users))
        
        return b.getvalue()