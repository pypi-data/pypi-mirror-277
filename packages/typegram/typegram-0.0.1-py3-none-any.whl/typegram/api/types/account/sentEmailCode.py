
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



class SentEmailCode(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.SentEmailCode`.

    Details:
        - Layer: ``181``
        - ID: ``811F854F``

email_pattern (``str``):
                    N/A
                
        length (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 21 functions.

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

    __slots__: List[str] = ["email_pattern", "length"]

    ID = 0x811f854f
    QUALNAME = "functions.typesaccount.SentEmailCode"

    def __init__(self, *, email_pattern: str, length: int) -> None:
        
                self.email_pattern = email_pattern  # string
        
                self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentEmailCode":
        # No flags
        
        email_pattern = String.read(b)
        
        length = Int.read(b)
        
        return SentEmailCode(email_pattern=email_pattern, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email_pattern))
        
        b.write(Int(self.length))
        
        return b.getvalue()