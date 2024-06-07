
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



class ConnectedBots(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.ConnectedBots`.

    Details:
        - Layer: ``181``
        - ID: ``17D7F87B``

connected_bots (List of :obj:`ConnectedBot<typegram.api.ayiin.ConnectedBot>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
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

    __slots__: List[str] = ["connected_bots", "users"]

    ID = 0x17d7f87b
    QUALNAME = "functions.typesaccount.ConnectedBots"

    def __init__(self, *, connected_bots: List["ayiin.ConnectedBot"], users: List["ayiin.User"]) -> None:
        
                self.connected_bots = connected_bots  # ConnectedBot
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConnectedBots":
        # No flags
        
        connected_bots = Object.read(b)
        
        users = Object.read(b)
        
        return ConnectedBots(connected_bots=connected_bots, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.connected_bots))
        
        b.write(Vector(self.users))
        
        return b.getvalue()