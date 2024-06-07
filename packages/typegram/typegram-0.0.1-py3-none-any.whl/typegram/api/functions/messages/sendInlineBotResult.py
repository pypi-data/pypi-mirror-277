
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



class SendInlineBotResult(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``3EBEE86A``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        random_id (``int`` ``64-bit``):
                    N/A
                
        query_id (``int`` ``64-bit``):
                    N/A
                
        id (``str``):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        background (``bool``, *optional*):
                    N/A
                
        clear_draft (``bool``, *optional*):
                    N/A
                
        hide_via (``bool``, *optional*):
                    N/A
                
        reply_to (:obj:`InputReplyTo<typegram.api.ayiin.InputReplyTo>`, *optional*):
                    N/A
                
        schedule_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        send_as (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        quick_reply_shortcut (:obj:`InputQuickReplyShortcut<typegram.api.ayiin.InputQuickReplyShortcut>`, *optional*):
                    N/A
                
    Returns:
        :obj:`Updates<typegram.api.ayiin.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "query_id", "id", "silent", "background", "clear_draft", "hide_via", "reply_to", "schedule_date", "send_as", "quick_reply_shortcut"]

    ID = 0x3ebee86a
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, peer: "ayiin.InputPeer", random_id: int, query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: "ayiin.InputReplyTo" = None, schedule_date: Optional[int] = None, send_as: "ayiin.InputPeer" = None, quick_reply_shortcut: "ayiin.InputQuickReplyShortcut" = None) -> None:
        
                self.peer = peer  # InputPeer
        
                self.random_id = random_id  # long
        
                self.query_id = query_id  # long
        
                self.id = id  # string
        
                self.silent = silent  # true
        
                self.background = background  # true
        
                self.clear_draft = clear_draft  # true
        
                self.hide_via = hide_via  # true
        
                self.reply_to = reply_to  # InputReplyTo
        
                self.schedule_date = schedule_date  # int
        
                self.send_as = send_as  # InputPeer
        
                self.quick_reply_shortcut = quick_reply_shortcut  # InputQuickReplyShortcut

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendInlineBotResult":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        hide_via = True if flags & (1 << 11) else False
        peer = Object.read(b)
        
        reply_to = Object.read(b) if flags & (1 << 0) else None
        
        random_id = Long.read(b)
        
        query_id = Long.read(b)
        
        id = String.read(b)
        
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = Object.read(b) if flags & (1 << 13) else None
        
        quick_reply_shortcut = Object.read(b) if flags & (1 << 17) else None
        
        return SendInlineBotResult(peer=peer, random_id=random_id, query_id=query_id, id=id, silent=silent, background=background, clear_draft=clear_draft, hide_via=hide_via, reply_to=reply_to, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Long(self.random_id))
        
        b.write(Long(self.query_id))
        
        b.write(String(self.id))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())
        
        return b.getvalue()