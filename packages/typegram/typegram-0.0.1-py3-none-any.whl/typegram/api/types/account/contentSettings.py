
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



class ContentSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.ContentSettings`.

    Details:
        - Layer: ``181``
        - ID: ``57E28221``

sensitive_enabled (``bool``, *optional*):
                    N/A
                
        sensitive_can_change (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 23 functions.

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

    __slots__: List[str] = ["sensitive_enabled", "sensitive_can_change"]

    ID = 0x57e28221
    QUALNAME = "functions.typesaccount.ContentSettings"

    def __init__(self, *, sensitive_enabled: Optional[bool] = None, sensitive_can_change: Optional[bool] = None) -> None:
        
                self.sensitive_enabled = sensitive_enabled  # true
        
                self.sensitive_can_change = sensitive_can_change  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContentSettings":
        
        flags = Int.read(b)
        
        sensitive_enabled = True if flags & (1 << 0) else False
        sensitive_can_change = True if flags & (1 << 1) else False
        return ContentSettings(sensitive_enabled=sensitive_enabled, sensitive_can_change=sensitive_can_change)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        return b.getvalue()