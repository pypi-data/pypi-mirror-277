
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class MediaAreaChannelPost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``770416AF``

coordinates (:obj:`MediaAreaCoordinates<typegram.api.ayiin.MediaAreaCoordinates>`):
                    N/A
                
        channel_id (``int`` ``64-bit``):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["coordinates", "channel_id", "msg_id"]

    ID = 0x770416af
    QUALNAME = "types.mediaAreaChannelPost"

    def __init__(self, *, coordinates: "api.ayiin.MediaAreaCoordinates", channel_id: int, msg_id: int) -> None:
        
                self.coordinates = coordinates  # MediaAreaCoordinates
        
                self.channel_id = channel_id  # long
        
                self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaChannelPost":
        # No flags
        
        coordinates = Object.read(b)
        
        channel_id = Long.read(b)
        
        msg_id = Int.read(b)
        
        return MediaAreaChannelPost(coordinates=coordinates, channel_id=channel_id, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()