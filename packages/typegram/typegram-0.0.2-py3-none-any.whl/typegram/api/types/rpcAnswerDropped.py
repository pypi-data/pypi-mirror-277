
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



class RpcAnswerDropped(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.RpcDropAnswer`.

    Details:
        - Layer: ``181``
        - ID: ``A43AD8B7``

msg_id (``int`` ``64-bit``):
                    N/A
                
        seq_no (``int`` ``32-bit``):
                    N/A
                
        bytes (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            rpcDropAnswer
    """

    __slots__: List[str] = ["msg_id", "seq_no", "bytes"]

    ID = 0xa43ad8b7
    QUALNAME = "types.rpcAnswerDropped"

    def __init__(self, *, msg_id: int, seq_no: int, bytes: int) -> None:
        
                self.msg_id = msg_id  # long
        
                self.seq_no = seq_no  # int
        
                self.bytes = bytes  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcAnswerDropped":
        # No flags
        
        msg_id = Long.read(b)
        
        seq_no = Int.read(b)
        
        bytes = Int.read(b)
        
        return RpcAnswerDropped(msg_id=msg_id, seq_no=seq_no, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(Int(self.seq_no))
        
        b.write(Int(self.bytes))
        
        return b.getvalue()