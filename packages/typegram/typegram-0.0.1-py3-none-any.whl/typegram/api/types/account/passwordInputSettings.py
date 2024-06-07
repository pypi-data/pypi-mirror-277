
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



class PasswordInputSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.PasswordInputSettings`.

    Details:
        - Layer: ``181``
        - ID: ``C23727C9``

new_algo (:obj:`PasswordKdfAlgo<typegram.api.ayiin.PasswordKdfAlgo>`, *optional*):
                    N/A
                
        new_password_hash (``bytes``, *optional*):
                    N/A
                
        hint (``str``, *optional*):
                    N/A
                
        email (``str``, *optional*):
                    N/A
                
        new_secure_settings (:obj:`SecureSecretSettings<typegram.api.ayiin.SecureSecretSettings>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 29 functions.

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

    __slots__: List[str] = ["new_algo", "new_password_hash", "hint", "email", "new_secure_settings"]

    ID = 0xc23727c9
    QUALNAME = "functions.typesaccount.PasswordInputSettings"

    def __init__(self, *, new_algo: "ayiin.PasswordKdfAlgo" = None, new_password_hash: Optional[bytes] = None, hint: Optional[str] = None, email: Optional[str] = None, new_secure_settings: "ayiin.SecureSecretSettings" = None) -> None:
        
                self.new_algo = new_algo  # PasswordKdfAlgo
        
                self.new_password_hash = new_password_hash  # bytes
        
                self.hint = hint  # string
        
                self.email = email  # string
        
                self.new_secure_settings = new_secure_settings  # SecureSecretSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PasswordInputSettings":
        
        flags = Int.read(b)
        
        new_algo = Object.read(b) if flags & (1 << 0) else None
        
        new_password_hash = Bytes.read(b) if flags & (1 << 0) else None
        hint = String.read(b) if flags & (1 << 0) else None
        email = String.read(b) if flags & (1 << 1) else None
        new_secure_settings = Object.read(b) if flags & (1 << 2) else None
        
        return PasswordInputSettings(new_algo=new_algo, new_password_hash=new_password_hash, hint=hint, email=email, new_secure_settings=new_secure_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.new_algo is not None:
            b.write(self.new_algo.write())
        
        if self.new_password_hash is not None:
            b.write(Bytes(self.new_password_hash))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.new_secure_settings is not None:
            b.write(self.new_secure_settings.write())
        
        return b.getvalue()