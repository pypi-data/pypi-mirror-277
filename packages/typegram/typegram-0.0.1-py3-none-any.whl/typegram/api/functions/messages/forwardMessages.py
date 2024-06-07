
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



class ForwardMessages(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``D5039208``

from_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        id (List of ``int`` ``32-bit``):
                    N/A
                
        random_id (List of ``int`` ``64-bit``):
                    N/A
                
        to_peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        background (``bool``, *optional*):
                    N/A
                
        with_my_score (``bool``, *optional*):
                    N/A
                
        drop_author (``bool``, *optional*):
                    N/A
                
        drop_media_captions (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["from_peer", "id", "random_id", "to_peer", "silent", "background", "with_my_score", "drop_author", "drop_media_captions", "noforwards", "top_msg_id", "schedule_date", "send_as", "quick_reply_shortcut"]

    ID = 0xd5039208
    QUALNAME = "functions.functions.Updates"

    def __init__(self, *, from_peer: "ayiin.InputPeer", id: List[int], random_id: List[int], to_peer: "ayiin.InputPeer", silent: Optional[bool] = None, background: Optional[bool] = None, with_my_score: Optional[bool] = None, drop_author: Optional[bool] = None, drop_media_captions: Optional[bool] = None, noforwards: Optional[bool] = None, top_msg_id: Optional[int] = None, schedule_date: Optional[int] = None, send_as: "ayiin.InputPeer" = None, quick_reply_shortcut: "ayiin.InputQuickReplyShortcut" = None) -> None:
        
                self.from_peer = from_peer  # InputPeer
        
                self.id = id  # int
        
                self.random_id = random_id  # long
        
                self.to_peer = to_peer  # InputPeer
        
                self.silent = silent  # true
        
                self.background = background  # true
        
                self.with_my_score = with_my_score  # true
        
                self.drop_author = drop_author  # true
        
                self.drop_media_captions = drop_media_captions  # true
        
                self.noforwards = noforwards  # true
        
                self.top_msg_id = top_msg_id  # int
        
                self.schedule_date = schedule_date  # int
        
                self.send_as = send_as  # InputPeer
        
                self.quick_reply_shortcut = quick_reply_shortcut  # InputQuickReplyShortcut

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForwardMessages":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        with_my_score = True if flags & (1 << 8) else False
        drop_author = True if flags & (1 << 11) else False
        drop_media_captions = True if flags & (1 << 12) else False
        noforwards = True if flags & (1 << 14) else False
        from_peer = Object.read(b)
        
        id = Object.read(b, Int)
        
        random_id = Object.read(b, Long)
        
        to_peer = Object.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 9) else None
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = Object.read(b) if flags & (1 << 13) else None
        
        quick_reply_shortcut = Object.read(b) if flags & (1 << 17) else None
        
        return ForwardMessages(from_peer=from_peer, id=id, random_id=random_id, to_peer=to_peer, silent=silent, background=background, with_my_score=with_my_score, drop_author=drop_author, drop_media_captions=drop_media_captions, noforwards=noforwards, top_msg_id=top_msg_id, schedule_date=schedule_date, send_as=send_as, quick_reply_shortcut=quick_reply_shortcut)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.from_peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(Vector(self.random_id, Long))
        
        b.write(self.to_peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        if self.quick_reply_shortcut is not None:
            b.write(self.quick_reply_shortcut.write())
        
        return b.getvalue()