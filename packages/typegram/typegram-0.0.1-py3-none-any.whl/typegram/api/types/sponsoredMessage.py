
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



class SponsoredMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SponsoredMessage`.

    Details:
        - Layer: ``181``
        - ID: ``BDEDF566``

random_id (``bytes``):
                    N/A
                
        url (``str``):
                    N/A
                
        title (``str``):
                    N/A
                
        message (``str``):
                    N/A
                
        button_text (``str``):
                    N/A
                
        recommended (``bool``, *optional*):
                    N/A
                
        can_report (``bool``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        photo (:obj:`Photo<typegram.api.ayiin.Photo>`, *optional*):
                    N/A
                
        color (:obj:`PeerColor<typegram.api.ayiin.PeerColor>`, *optional*):
                    N/A
                
        sponsor_info (``str``, *optional*):
                    N/A
                
        additional_info (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["random_id", "url", "title", "message", "button_text", "recommended", "can_report", "entities", "photo", "color", "sponsor_info", "additional_info"]

    ID = 0xbdedf566
    QUALNAME = "functions.types.SponsoredMessage"

    def __init__(self, *, random_id: bytes, url: str, title: str, message: str, button_text: str, recommended: Optional[bool] = None, can_report: Optional[bool] = None, entities: Optional[List["ayiin.MessageEntity"]] = None, photo: "ayiin.Photo" = None, color: "ayiin.PeerColor" = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None) -> None:
        
                self.random_id = random_id  # bytes
        
                self.url = url  # string
        
                self.title = title  # string
        
                self.message = message  # string
        
                self.button_text = button_text  # string
        
                self.recommended = recommended  # true
        
                self.can_report = can_report  # true
        
                self.entities = entities  # MessageEntity
        
                self.photo = photo  # Photo
        
                self.color = color  # PeerColor
        
                self.sponsor_info = sponsor_info  # string
        
                self.additional_info = additional_info  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessage":
        
        flags = Int.read(b)
        
        recommended = True if flags & (1 << 5) else False
        can_report = True if flags & (1 << 12) else False
        random_id = Bytes.read(b)
        
        url = String.read(b)
        
        title = String.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 1) else []
        
        photo = Object.read(b) if flags & (1 << 6) else None
        
        color = Object.read(b) if flags & (1 << 13) else None
        
        button_text = String.read(b)
        
        sponsor_info = String.read(b) if flags & (1 << 7) else None
        additional_info = String.read(b) if flags & (1 << 8) else None
        return SponsoredMessage(random_id=random_id, url=url, title=title, message=message, button_text=button_text, recommended=recommended, can_report=can_report, entities=entities, photo=photo, color=color, sponsor_info=sponsor_info, additional_info=additional_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Bytes(self.random_id))
        
        b.write(String(self.url))
        
        b.write(String(self.title))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.color is not None:
            b.write(self.color.write())
        
        b.write(String(self.button_text))
        
        if self.sponsor_info is not None:
            b.write(String(self.sponsor_info))
        
        if self.additional_info is not None:
            b.write(String(self.additional_info))
        
        return b.getvalue()