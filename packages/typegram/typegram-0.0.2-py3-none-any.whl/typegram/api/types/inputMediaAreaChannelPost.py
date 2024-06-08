
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



class InputMediaAreaChannelPost(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``2271F2BF``

coordinates (:obj:`MediaAreaCoordinates<typegram.api.ayiin.MediaAreaCoordinates>`):
                    N/A
                
        channel (:obj:`InputChannel<typegram.api.ayiin.InputChannel>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
    """

    __slots__: List[str] = ["coordinates", "channel", "msg_id"]

    ID = 0x2271f2bf
    QUALNAME = "types.inputMediaAreaChannelPost"

    def __init__(self, *, coordinates: "api.ayiin.MediaAreaCoordinates", channel: "api.ayiin.InputChannel", msg_id: int) -> None:
        
                self.coordinates = coordinates  # MediaAreaCoordinates
        
                self.channel = channel  # InputChannel
        
                self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaChannelPost":
        # No flags
        
        coordinates = Object.read(b)
        
        channel = Object.read(b)
        
        msg_id = Int.read(b)
        
        return InputMediaAreaChannelPost(coordinates=coordinates, channel=channel, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()