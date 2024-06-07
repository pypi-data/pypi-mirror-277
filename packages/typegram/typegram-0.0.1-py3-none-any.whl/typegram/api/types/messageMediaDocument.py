
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



class MessageMediaDocument(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``4CF4D72D``

nopremium (``bool``, *optional*):
                    N/A
                
        spoiler (``bool``, *optional*):
                    N/A
                
        video (``bool``, *optional*):
                    N/A
                
        round (``bool``, *optional*):
                    N/A
                
        voice (``bool``, *optional*):
                    N/A
                
        document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        alt_document (:obj:`Document<typegram.api.ayiin.Document>`, *optional*):
                    N/A
                
        ttl_seconds (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["nopremium", "spoiler", "video", "round", "voice", "document", "alt_document", "ttl_seconds"]

    ID = 0x4cf4d72d
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, nopremium: Optional[bool] = None, spoiler: Optional[bool] = None, video: Optional[bool] = None, round: Optional[bool] = None, voice: Optional[bool] = None, document: "ayiin.Document" = None, alt_document: "ayiin.Document" = None, ttl_seconds: Optional[int] = None) -> None:
        
                self.nopremium = nopremium  # true
        
                self.spoiler = spoiler  # true
        
                self.video = video  # true
        
                self.round = round  # true
        
                self.voice = voice  # true
        
                self.document = document  # Document
        
                self.alt_document = alt_document  # Document
        
                self.ttl_seconds = ttl_seconds  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDocument":
        
        flags = Int.read(b)
        
        nopremium = True if flags & (1 << 3) else False
        spoiler = True if flags & (1 << 4) else False
        video = True if flags & (1 << 6) else False
        round = True if flags & (1 << 7) else False
        voice = True if flags & (1 << 8) else False
        document = Object.read(b) if flags & (1 << 0) else None
        
        alt_document = Object.read(b) if flags & (1 << 5) else None
        
        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        return MessageMediaDocument(nopremium=nopremium, spoiler=spoiler, video=video, round=round, voice=voice, document=document, alt_document=alt_document, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.alt_document is not None:
            b.write(self.alt_document.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()