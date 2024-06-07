
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



class Password(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.Password`.

    Details:
        - Layer: ``181``
        - ID: ``957B50FB``

new_algo (:obj:`PasswordKdfAlgo<typegram.api.ayiin.PasswordKdfAlgo>`):
                    N/A
                
        new_secure_algo (:obj:`SecurePasswordKdfAlgo<typegram.api.ayiin.SecurePasswordKdfAlgo>`):
                    N/A
                
        secure_random (``bytes``):
                    N/A
                
        has_recovery (``bool``, *optional*):
                    N/A
                
        has_secure_values (``bool``, *optional*):
                    N/A
                
        has_password (``bool``, *optional*):
                    N/A
                
        current_algo (:obj:`PasswordKdfAlgo<typegram.api.ayiin.PasswordKdfAlgo>`, *optional*):
                    N/A
                
        srp_B (``bytes``, *optional*):
                    N/A
                
        srp_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        hint (``str``, *optional*):
                    N/A
                
        email_unconfirmed_pattern (``str``, *optional*):
                    N/A
                
        pending_reset_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        login_email_pattern (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["new_algo", "new_secure_algo", "secure_random", "has_recovery", "has_secure_values", "has_password", "current_algo", "srp_B", "srp_id", "hint", "email_unconfirmed_pattern", "pending_reset_date", "login_email_pattern"]

    ID = 0x957b50fb
    QUALNAME = "functions.typesaccount.Password"

    def __init__(self, *, new_algo: "ayiin.PasswordKdfAlgo", new_secure_algo: "ayiin.SecurePasswordKdfAlgo", secure_random: bytes, has_recovery: Optional[bool] = None, has_secure_values: Optional[bool] = None, has_password: Optional[bool] = None, current_algo: "ayiin.PasswordKdfAlgo" = None, srp_B: Optional[bytes] = None, srp_id: Optional[int] = None, hint: Optional[str] = None, email_unconfirmed_pattern: Optional[str] = None, pending_reset_date: Optional[int] = None, login_email_pattern: Optional[str] = None) -> None:
        
                self.new_algo = new_algo  # PasswordKdfAlgo
        
                self.new_secure_algo = new_secure_algo  # SecurePasswordKdfAlgo
        
                self.secure_random = secure_random  # bytes
        
                self.has_recovery = has_recovery  # true
        
                self.has_secure_values = has_secure_values  # true
        
                self.has_password = has_password  # true
        
                self.current_algo = current_algo  # PasswordKdfAlgo
        
                self.srp_B = srp_B  # bytes
        
                self.srp_id = srp_id  # long
        
                self.hint = hint  # string
        
                self.email_unconfirmed_pattern = email_unconfirmed_pattern  # string
        
                self.pending_reset_date = pending_reset_date  # int
        
                self.login_email_pattern = login_email_pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Password":
        
        flags = Int.read(b)
        
        has_recovery = True if flags & (1 << 0) else False
        has_secure_values = True if flags & (1 << 1) else False
        has_password = True if flags & (1 << 2) else False
        current_algo = Object.read(b) if flags & (1 << 2) else None
        
        srp_B = Bytes.read(b) if flags & (1 << 2) else None
        srp_id = Long.read(b) if flags & (1 << 2) else None
        hint = String.read(b) if flags & (1 << 3) else None
        email_unconfirmed_pattern = String.read(b) if flags & (1 << 4) else None
        new_algo = Object.read(b)
        
        new_secure_algo = Object.read(b)
        
        secure_random = Bytes.read(b)
        
        pending_reset_date = Int.read(b) if flags & (1 << 5) else None
        login_email_pattern = String.read(b) if flags & (1 << 6) else None
        return Password(new_algo=new_algo, new_secure_algo=new_secure_algo, secure_random=secure_random, has_recovery=has_recovery, has_secure_values=has_secure_values, has_password=has_password, current_algo=current_algo, srp_B=srp_B, srp_id=srp_id, hint=hint, email_unconfirmed_pattern=email_unconfirmed_pattern, pending_reset_date=pending_reset_date, login_email_pattern=login_email_pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.current_algo is not None:
            b.write(self.current_algo.write())
        
        if self.srp_B is not None:
            b.write(Bytes(self.srp_B))
        
        if self.srp_id is not None:
            b.write(Long(self.srp_id))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email_unconfirmed_pattern is not None:
            b.write(String(self.email_unconfirmed_pattern))
        
        b.write(self.new_algo.write())
        
        b.write(self.new_secure_algo.write())
        
        b.write(Bytes(self.secure_random))
        
        if self.pending_reset_date is not None:
            b.write(Int(self.pending_reset_date))
        
        if self.login_email_pattern is not None:
            b.write(String(self.login_email_pattern))
        
        return b.getvalue()