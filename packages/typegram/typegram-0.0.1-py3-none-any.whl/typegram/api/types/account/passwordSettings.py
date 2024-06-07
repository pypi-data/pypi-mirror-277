
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



class PasswordSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.PasswordSettings`.

    Details:
        - Layer: ``181``
        - ID: ``9A5C33E5``

email (``str``, *optional*):
                    N/A
                
        secure_settings (:obj:`SecureSecretSettings<typegram.api.ayiin.SecureSecretSettings>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

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

    __slots__: List[str] = ["email", "secure_settings"]

    ID = 0x9a5c33e5
    QUALNAME = "functions.typesaccount.PasswordSettings"

    def __init__(self, *, email: Optional[str] = None, secure_settings: "ayiin.SecureSecretSettings" = None) -> None:
        
                self.email = email  # string
        
                self.secure_settings = secure_settings  # SecureSecretSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordSettings":
        
        flags = Int.read(b)
        
        email = String.read(b) if flags & (1 << 0) else None
        secure_settings = Object.read(b) if flags & (1 << 1) else None
        
        return PasswordSettings(email=email, secure_settings=secure_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.secure_settings is not None:
            b.write(self.secure_settings.write())
        
        return b.getvalue()