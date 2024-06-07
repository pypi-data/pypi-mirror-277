
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



class ReactionsNotifySettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ReactionsNotifySettings`.

    Details:
        - Layer: ``181``
        - ID: ``56E34970``

sound (:obj:`NotificationSound<typegram.api.ayiin.NotificationSound>`):
                    N/A
                
        show_previews (``bool``):
                    N/A
                
        messages_notify_from (:obj:`ReactionNotificationsFrom<typegram.api.ayiin.ReactionNotificationsFrom>`, *optional*):
                    N/A
                
        stories_notify_from (:obj:`ReactionNotificationsFrom<typegram.api.ayiin.ReactionNotificationsFrom>`, *optional*):
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

    __slots__: List[str] = ["sound", "show_previews", "messages_notify_from", "stories_notify_from"]

    ID = 0x56e34970
    QUALNAME = "functions.types.ReactionsNotifySettings"

    def __init__(self, *, sound: "ayiin.NotificationSound", show_previews: bool, messages_notify_from: "ayiin.ReactionNotificationsFrom" = None, stories_notify_from: "ayiin.ReactionNotificationsFrom" = None) -> None:
        
                self.sound = sound  # NotificationSound
        
                self.show_previews = show_previews  # Bool
        
                self.messages_notify_from = messages_notify_from  # ReactionNotificationsFrom
        
                self.stories_notify_from = stories_notify_from  # ReactionNotificationsFrom

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReactionsNotifySettings":
        
        flags = Int.read(b)
        
        messages_notify_from = Object.read(b) if flags & (1 << 0) else None
        
        stories_notify_from = Object.read(b) if flags & (1 << 1) else None
        
        sound = Object.read(b)
        
        show_previews = Bool.read(b)
        
        return ReactionsNotifySettings(sound=sound, show_previews=show_previews, messages_notify_from=messages_notify_from, stories_notify_from=stories_notify_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.messages_notify_from is not None:
            b.write(self.messages_notify_from.write())
        
        if self.stories_notify_from is not None:
            b.write(self.stories_notify_from.write())
        
        b.write(self.sound.write())
        
        b.write(Bool(self.show_previews))
        
        return b.getvalue()