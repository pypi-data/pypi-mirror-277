
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



class ResetPasswordFailedWait(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.ResetPasswordResult`.

    Details:
        - Layer: ``181``
        - ID: ``E3779861``

retry_date (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 27 functions.

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

    __slots__: List[str] = ["retry_date"]

    ID = 0xe3779861
    QUALNAME = "functions.typesaccount.ResetPasswordResult"

    def __init__(self, *, retry_date: int) -> None:
        
                self.retry_date = retry_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordFailedWait":
        # No flags
        
        retry_date = Int.read(b)
        
        return ResetPasswordFailedWait(retry_date=retry_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.retry_date))
        
        return b.getvalue()