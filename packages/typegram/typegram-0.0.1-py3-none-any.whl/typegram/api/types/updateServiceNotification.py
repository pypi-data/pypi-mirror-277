
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



class UpdateServiceNotification(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``EBE46819``

type (``str``):
                    N/A
                
        message (``str``):
                    N/A
                
        media (:obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
        popup (``bool``, *optional*):
                    N/A
                
        invert_media (``bool``, *optional*):
                    N/A
                
        inbox_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 7 functions.

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

    __slots__: List[str] = ["type", "message", "media", "entities", "popup", "invert_media", "inbox_date"]

    ID = 0xebe46819
    QUALNAME = "functions.types.Update"

    def __init__(self, *, type: str, message: str, media: "ayiin.MessageMedia", entities: List["ayiin.MessageEntity"], popup: Optional[bool] = None, invert_media: Optional[bool] = None, inbox_date: Optional[int] = None) -> None:
        
                self.type = type  # string
        
                self.message = message  # string
        
                self.media = media  # MessageMedia
        
                self.entities = entities  # MessageEntity
        
                self.popup = popup  # true
        
                self.invert_media = invert_media  # true
        
                self.inbox_date = inbox_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateServiceNotification":
        
        flags = Int.read(b)
        
        popup = True if flags & (1 << 0) else False
        invert_media = True if flags & (1 << 2) else False
        inbox_date = Int.read(b) if flags & (1 << 1) else None
        type = String.read(b)
        
        message = String.read(b)
        
        media = Object.read(b)
        
        entities = Object.read(b)
        
        return UpdateServiceNotification(type=type, message=message, media=media, entities=entities, popup=popup, invert_media=invert_media, inbox_date=inbox_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.inbox_date is not None:
            b.write(Int(self.inbox_date))
        
        b.write(String(self.type))
        
        b.write(String(self.message))
        
        b.write(self.media.write())
        
        b.write(Vector(self.entities))
        
        return b.getvalue()