
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



class ProlongWebView(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``B0D81A83``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        query_id (``int`` ``64-bit``):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        send_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "bot", "query_id", "silent", "reply_to", "send_as"]

    ID = 0xb0d81a83
    QUALNAME = "functions.functions.Bool"

    def __init__(self, *, peer: "ayiin.InputPeer", bot: "ayiin.InputUser", query_id: int, silent: Optional[bool] = None, reply_to: "ayiin.InputReplyTo" = None, send_as: "ayiin.InputPeer" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.bot = bot  # InputUser
        
                self.query_id = query_id  # long
        
                self.silent = silent  # true
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProlongWebView":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        peer = Object.read(b)
        
        bot = Object.read(b)
        
        query_id = Long.read(b)
        
        reply_to = Object.read(b) if flags & (1 << 0) else None
        
        send_as = Object.read(b) if flags & (1 << 13) else None
        
        return ProlongWebView(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to=reply_to, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        b.write(Long(self.query_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()