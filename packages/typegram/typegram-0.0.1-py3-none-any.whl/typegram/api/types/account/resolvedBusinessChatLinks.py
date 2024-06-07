
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



class ResolvedBusinessChatLinks(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.account.ResolvedBusinessChatLinks`.

    Details:
        - Layer: ``181``
        - ID: ``9A23AF21``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        message (``str``):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 33 functions.

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

    __slots__: List[str] = ["peer", "message", "chats", "users", "entities"]

    ID = 0x9a23af21
    QUALNAME = "functions.typesaccount.ResolvedBusinessChatLinks"

    def __init__(self, *, peer: "ayiin.Peer", message: str, chats: List["ayiin.Chat"], users: List["ayiin.User"], entities: Optional[List["ayiin.MessageEntity"]] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.message = message  # string
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.entities = entities  # MessageEntity

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResolvedBusinessChatLinks":
        
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 0) else []
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ResolvedBusinessChatLinks(peer=peer, message=message, chats=chats, users=users, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()