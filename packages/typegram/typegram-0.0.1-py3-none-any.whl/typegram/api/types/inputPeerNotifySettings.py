
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



class InputPeerNotifySettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputPeerNotifySettings`.

    Details:
        - Layer: ``181``
        - ID: ``CACB6AE2``

show_previews (``bool``, *optional*):
                    N/A
                
        silent (``bool``, *optional*):
                    N/A
                
        mute_until (``int`` ``32-bit``, *optional*):
                    N/A
                
        sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
        stories_muted (``bool``, *optional*):
                    N/A
                
        stories_hide_sender (``bool``, *optional*):
                    N/A
                
        stories_sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 24 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            .X
            .RpcDropAnswer
            .Bool
            .Authorization
            .PeerNotifySettings
            .User
            .Vector<SecureValue>
            .SecureValue
            .Updates
            .WallPaper
            .Document
            .Theme
            .Vector<WallPaper>
            .GlobalPrivacySettings
            .EmojiList
            .BusinessChatLink
            .ReactionsNotifySettings
            .Vector<User>
            .Vector<Bool>
            .Vector<int>
            .Vector<ReceivedNotifyMessage>
            .EncryptedChat
            .Vector<long>
            .MessageMedia
            .ExportedChatInvite
            .ChatInvite
            .Vector<StickerSetCovered>
            .EncryptedFile
            .ChatOnlines
            .EmojiKeywordsDifference
            .Vector<EmojiLanguage>
            .EmojiURL
            .UrlAuthResult
            .Vector<ReadParticipantDate>
            .AttachMenuBots
            .AttachMenuBotsBot
            .WebViewResult
            .SimpleWebViewResult
            .WebViewMessageSent
            .Vector<Document>
            .AppWebViewResult
            .OutboxReadDate
            .Vector<FactCheck>
            .Vector<FileHash>
            .ExportedMessageLink
            .DataJSON
            .Vector<BotCommand>
            .BotMenuButton
            .Vector<PremiumGiftCodeOption>
            .LangPackDifference
            .Vector<LangPackString>
            .Vector<LangPackLanguage>
            .LangPackLanguage
            .StatsGraph
            .ExportedChatlistInvite
            .Vector<Peer>
            .ExportedStoryLink
            .SmsJob
            .ResPQ
            .P_Q_inner_data
            .BindAuthKeyInner
            .Server_DH_Params
            .Server_DH_inner_data
            .Client_DH_Inner_Data
            .Set_client_DH_params_answer
    """

    __slots__: List[str] = ["show_previews", "silent", "mute_until", "sound", "stories_muted", "stories_hide_sender", "stories_sound"]

    ID = 0xcacb6ae2
    QUALNAME = "functions.types.InputPeerNotifySettings"

    def __init__(self, *, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[int] = None, sound: "ayiin.NotificationSound" = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_sound: "ayiin.NotificationSound" = None) -> None:
        
                self.show_previews = show_previews  # Bool
        
                self.silent = silent  # Bool
        
                self.mute_until = mute_until  # int
        
                self.sound = sound  # NotificationSound
        
                self.stories_muted = stories_muted  # Bool
        
                self.stories_hide_sender = stories_hide_sender  # Bool
        
                self.stories_sound = stories_sound  # NotificationSound

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerNotifySettings":
        
        flags = Int.read(b)
        
        show_previews = Bool.read(b) if flags & (1 << 0) else None
        silent = Bool.read(b) if flags & (1 << 1) else None
        mute_until = Int.read(b) if flags & (1 << 2) else None
        sound = Object.read(b) if flags & (1 << 3) else None
        
        stories_muted = Bool.read(b) if flags & (1 << 6) else None
        stories_hide_sender = Bool.read(b) if flags & (1 << 7) else None
        stories_sound = Object.read(b) if flags & (1 << 8) else None
        
        return InputPeerNotifySettings(show_previews=show_previews, silent=silent, mute_until=mute_until, sound=sound, stories_muted=stories_muted, stories_hide_sender=stories_hide_sender, stories_sound=stories_sound)

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
        
        if self.sound is not None:
            b.write(self.sound.write())
        
        if self.stories_muted is not None:
            b.write(Bool(self.stories_muted))
        
        if self.stories_hide_sender is not None:
            b.write(Bool(self.stories_hide_sender))
        
        if self.stories_sound is not None:
            b.write(self.stories_sound.write())
        
        return b.getvalue()