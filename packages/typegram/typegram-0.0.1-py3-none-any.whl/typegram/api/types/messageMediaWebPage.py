
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



class MessageMediaWebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``DDF10C3B``

webpage (:obj:`WebPage<typegram.api.ayiin.WebPage>`):
                    N/A
                
        force_large_media (``bool``, *optional*):
                    N/A
                
        force_small_media (``bool``, *optional*):
                    N/A
                
        manual (``bool``, *optional*):
                    N/A
                
        safe (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 13 functions.

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

    __slots__: List[str] = ["webpage", "force_large_media", "force_small_media", "manual", "safe"]

    ID = 0xddf10c3b
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, webpage: "ayiin.WebPage", force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None) -> None:
        
                self.webpage = webpage  # WebPage
        
                self.force_large_media = force_large_media  # true
        
                self.force_small_media = force_small_media  # true
        
                self.manual = manual  # true
        
                self.safe = safe  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaWebPage":
        
        flags = Int.read(b)
        
        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        manual = True if flags & (1 << 3) else False
        safe = True if flags & (1 << 4) else False
        webpage = Object.read(b)
        
        return MessageMediaWebPage(webpage=webpage, force_large_media=force_large_media, force_small_media=force_small_media, manual=manual, safe=safe)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.webpage.write())
        
        return b.getvalue()