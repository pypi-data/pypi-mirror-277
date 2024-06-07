
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



class GetParticipants(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``77CED9D0``

channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        filter (:obj:`ChannelParticipantsFilter<typegram.api.ayiin.ChannelParticipantsFilter>`):
                    N/A
                
        offset (``int`` ``32-bit``):
                    N/A
                
        limit (``int`` ``32-bit``):
                    N/A
                
        hash (``int`` ``64-bit``):
                    N/A
                
    Returns:
        :obj:`channels.ChannelParticipants<typegram.api.ayiin.channels.ChannelParticipants>`
    """

    __slots__: List[str] = ["channel", "filter", "offset", "limit", "hash"]

    ID = 0x77ced9d0
    QUALNAME = "functions.functionschannels.ChannelParticipants"

    def __init__(self, *, channel: "ayiin.InputChannel", filter: "ayiin.ChannelParticipantsFilter", offset: int, limit: int, hash: int) -> None:
        
                self.channel = channel  # InputChannel
        
                self.filter = filter  # ChannelParticipantsFilter
        
                self.offset = offset  # int
        
                self.limit = limit  # int
        
                self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetParticipants":
        # No flags
        
        channel = Object.read(b)
        
        filter = Object.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetParticipants(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()