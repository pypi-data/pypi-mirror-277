
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



class PeerNotifySettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PeerNotifySettings`.

    Details:
        - Layer: ``181``
        - ID: ``99622C0C``

show_previews (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        mute_until (``int`` ``32-bit``, *optional*):
                    N/A
                
        ios_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        android_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        other_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        stories_muted (``bool``, *optional*):
                    N/A
                
        stories_hide_sender (``bool``, *optional*):
                    N/A
                
        stories_ios_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        stories_android_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        stories_other_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.getNotifySettings
    """

    __slots__: List[str] = ["show_previews", "silent", "mute_until", "ios_sound", "android_sound", "other_sound", "stories_muted", "stories_hide_sender", "stories_ios_sound", "stories_android_sound", "stories_other_sound"]

    ID = 0x99622c0c
    QUALNAME = "types.peerNotifySettings"

    def __init__(self, *, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[int] = None, ios_sound: "api.ayiin.NotificationSound" = None, android_sound: "api.ayiin.NotificationSound" = None, other_sound: "api.ayiin.NotificationSound" = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_ios_sound: "api.ayiin.NotificationSound" = None, stories_android_sound: "api.ayiin.NotificationSound" = None, stories_other_sound: "api.ayiin.NotificationSound" = None) -> None:
        
                self.show_previews = show_previews  # Bool
        
                self.silent = silent  # Bool
        
                self.mute_until = mute_until  # int
        
                self.ios_sound = ios_sound  # NotificationSound
        
                self.android_sound = android_sound  # NotificationSound
        
                self.other_sound = other_sound  # NotificationSound
        
                self.stories_muted = stories_muted  # Bool
        
                self.stories_hide_sender = stories_hide_sender  # Bool
        
                self.stories_ios_sound = stories_ios_sound  # NotificationSound
        
                self.stories_android_sound = stories_android_sound  # NotificationSound
        
                self.stories_other_sound = stories_other_sound  # NotificationSound

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerNotifySettings":
        
        flags = Int.read(b)
        
        show_previews = Bool.read(b) if flags & (1 << 0) else None
        silent = Bool.read(b) if flags & (1 << 1) else None
        mute_until = Int.read(b) if flags & (1 << 2) else None
        ios_sound = Object.read(b) if flags & (1 << 3) else None
        
        android_sound = Object.read(b) if flags & (1 << 4) else None
        
        other_sound = Object.read(b) if flags & (1 << 5) else None
        
        stories_muted = Bool.read(b) if flags & (1 << 6) else None
        stories_hide_sender = Bool.read(b) if flags & (1 << 7) else None
        stories_ios_sound = Object.read(b) if flags & (1 << 8) else None
        
        stories_android_sound = Object.read(b) if flags & (1 << 9) else None
        
        stories_other_sound = Object.read(b) if flags & (1 << 10) else None
        
        return PeerNotifySettings(show_previews=show_previews, silent=silent, mute_until=mute_until, ios_sound=ios_sound, android_sound=android_sound, other_sound=other_sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_ios_sound=stories_ios_sound, stories_android_sound=stories_android_sound, stories_other_sound=stories_other_sound)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.show_previews is not None:
            b.write(Bool(self.show_previews))
        
        if self.silent is not None:
            b.write(Bool(self.silent))
        
        if self.mute_until is not None:
            b.write(Int(self.mute_until))
        
        if self.ios_sound is not None:
            b.write(self.ios_sound.write())
        
        if self.android_sound is not None:
            b.write(self.android_sound.write())
        
        if self.other_sound is not None:
            b.write(self.other_sound.write())
        
        if self.stories_muted is not None:
            b.write(Bool(self.stories_muted))
        
        if self.stories_hide_sender is not None:
            b.write(Bool(self.stories_hide_sender))
        
        if self.stories_ios_sound is not None:
            b.write(self.stories_ios_sound.write())
        
        if self.stories_android_sound is not None:
            b.write(self.stories_android_sound.write())
        
        if self.stories_other_sound is not None:
            b.write(self.stories_other_sound.write())
        
        return b.getvalue()