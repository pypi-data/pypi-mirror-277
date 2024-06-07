
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



class AuthorizationForm(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.AuthorizationForm`.

    Details:
        - Layer: ``181``
        - ID: ``AD2E1CD8``

required_types (List of :obj:`SecureRequiredType<typegram.api.ayiin.SecureRequiredType>`):
                    N/A
                
        values (List of :obj:`SecureValue<typegram.api.ayiin.SecureValue>`):
                    N/A
                
        errors (List of :obj:`SecureValueError<typegram.api.ayiin.SecureValueError>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        privacy_policy_url (``str``, *optional*):
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

    __slots__: List[str] = ["required_types", "values", "errors", "users", "privacy_policy_url"]

    ID = 0xad2e1cd8
    QUALNAME = "functions.typesaccount.AuthorizationForm"

    def __init__(self, *, required_types: List["ayiin.SecureRequiredType"], values: List["ayiin.SecureValue"], errors: List["ayiin.SecureValueError"], users: List["ayiin.User"], privacy_policy_url: Optional[str] = None) -> None:
        
                self.required_types = required_types  # SecureRequiredType
        
                self.values = values  # SecureValue
        
                self.errors = errors  # SecureValueError
        
                self.users = users  # User
        
                self.privacy_policy_url = privacy_policy_url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuthorizationForm":
        
        flags = Int.read(b)
        
        required_types = Object.read(b)
        
        values = Object.read(b)
        
        errors = Object.read(b)
        
        users = Object.read(b)
        
        privacy_policy_url = String.read(b) if flags & (1 << 0) else None
        return AuthorizationForm(required_types=required_types, values=values, errors=errors, users=users, privacy_policy_url=privacy_policy_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.required_types))
        
        b.write(Vector(self.values))
        
        b.write(Vector(self.errors))
        
        b.write(Vector(self.users))
        
        if self.privacy_policy_url is not None:
            b.write(String(self.privacy_policy_url))
        
        return b.getvalue()