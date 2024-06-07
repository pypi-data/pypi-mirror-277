
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



class GroupCallStreamRtmpUrl(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.phone.GroupCallStreamRtmpUrl`.

    Details:
        - Layer: ``181``
        - ID: ``2DBF3432``

url (``str``):
                    N/A
                
        key (``str``):
                    N/A
                
    Functions:
        This object can be returned by 28 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            phone.PhoneCall
            phone.GroupCall
            phone.GroupParticipants
            phone.JoinAsPeers
            phone.ExportedGroupCallInvite
            phone.GroupCallStreamChannels
            phone.GroupCallStreamRtmpUrl
    """

    __slots__: List[str] = ["url", "key"]

    ID = 0x2dbf3432
    QUALNAME = "functions.typesphone.GroupCallStreamRtmpUrl"

    def __init__(self, *, url: str, key: str) -> None:
        
                self.url = url  # string
        
                self.key = key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamRtmpUrl":
        # No flags
        
        url = String.read(b)
        
        key = String.read(b)
        
        return GroupCallStreamRtmpUrl(url=url, key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(String(self.key))
        
        return b.getvalue()