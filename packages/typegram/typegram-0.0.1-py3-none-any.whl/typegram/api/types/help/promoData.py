
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



class PromoData(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PromoData`.

    Details:
        - Layer: ``181``
        - ID: ``8C39793F``

expires (``int`` ``32-bit``):
                    N/A
                
        peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        chats (List of :obj:`Chat<typegram.api.ayiin.Chat>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        proxy (``bool``, *optional*):
                    N/A
                
        psa_type (``str``, *optional*):
                    N/A
                
        psa_message (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["expires", "peer", "chats", "users", "proxy", "psa_type", "psa_message"]

    ID = 0x8c39793f
    QUALNAME = "functions.typeshelp.PromoData"

    def __init__(self, *, expires: int, peer: "ayiin.Peer", chats: List["ayiin.Chat"], users: List["ayiin.User"], proxy: Optional[bool] = None, psa_type: Optional[str] = None, psa_message: Optional[str] = None) -> None:
        
                self.expires = expires  # int
        
                self.peer = peer  # Peer
        
                self.chats = chats  # Chat
        
                self.users = users  # User
        
                self.proxy = proxy  # true
        
                self.psa_type = psa_type  # string
        
                self.psa_message = psa_message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PromoData":
        
        flags = Int.read(b)
        
        proxy = True if flags & (1 << 0) else False
        expires = Int.read(b)
        
        peer = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        psa_type = String.read(b) if flags & (1 << 1) else None
        psa_message = String.read(b) if flags & (1 << 2) else None
        return PromoData(expires=expires, peer=peer, chats=chats, users=users, proxy=proxy, psa_type=psa_type, psa_message=psa_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.expires))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.psa_type is not None:
            b.write(String(self.psa_type))
        
        if self.psa_message is not None:
            b.write(String(self.psa_message))
        
        return b.getvalue()