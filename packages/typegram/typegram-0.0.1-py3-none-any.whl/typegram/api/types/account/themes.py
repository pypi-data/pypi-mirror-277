
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



class Themes(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.Themes`.

    Details:
        - Layer: ``181``
        - ID: ``9A3D8C6D``

hash (``int`` ``64-bit``):
                    N/A
                
        themes (List of :obj:`Theme<typegram.api.ayiin.Theme>`):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["hash", "themes"]

    ID = 0x9a3d8c6d
    QUALNAME = "functions.typesaccount.Themes"

    def __init__(self, *, hash: int, themes: List["ayiin.Theme"]) -> None:
        
                self.hash = hash  # long
        
                self.themes = themes  # Theme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Themes":
        # No flags
        
        hash = Long.read(b)
        
        themes = Object.read(b)
        
        return Themes(hash=hash, themes=themes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.themes))
        
        return b.getvalue()