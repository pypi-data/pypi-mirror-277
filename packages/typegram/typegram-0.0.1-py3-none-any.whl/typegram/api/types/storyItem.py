
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



class StoryItem(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StoryItem`.

    Details:
        - Layer: ``181``
        - ID: ``79B26A24``

id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        expire_date (``int`` ``32-bit``):
                    N/A
                
        media (:obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`):
                    N/A
                
        pinned (``bool``, *optional*):
                    N/A
                
        public (``bool``, *optional*):
                    N/A
                
        close_friends (``bool``, *optional*):
                    N/A
                
        min (``bool``, *optional*):
                    N/A
                
        noforwards (``bool``, *optional*):
                    N/A
                
        edited (``bool``, *optional*):
                    N/A
                
        contacts (``bool``, *optional*):
                    N/A
                
        selected_contacts (``bool``, *optional*):
                    N/A
                
        out (``bool``, *optional*):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        fwd_from (:obj:`StoryFwdHeader<typegram.api.ayiin.StoryFwdHeader>`, *optional*):
                    N/A
                
        caption (``str``, *optional*):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        media_areas (List of :obj:`MediaArea<typegram.api.ayiin.MediaArea>`, *optional*):
                    N/A
                
        privacy (List of :obj:`PrivacyRule<typegram.api.ayiin.PrivacyRule>`, *optional*):
                    N/A
                
        views (:obj:`StoryViews<typegram.api.ayiin.StoryViews>`, *optional*):
                    N/A
                
        sent_reaction (:obj:`Reaction<typegram.api.ayiin.Reaction>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

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

    __slots__: List[str] = ["id", "date", "expire_date", "media", "pinned", "public", "close_friends", "min", "noforwards", "edited", "contacts", "selected_contacts", "out", "from_id", "fwd_from", "caption", "entities", "media_areas", "privacy", "views", "sent_reaction"]

    ID = 0x79b26a24
    QUALNAME = "functions.types.StoryItem"

    def __init__(self, *, id: int, date: int, expire_date: int, media: "ayiin.MessageMedia", pinned: Optional[bool] = None, public: Optional[bool] = None, close_friends: Optional[bool] = None, min: Optional[bool] = None, noforwards: Optional[bool] = None, edited: Optional[bool] = None, contacts: Optional[bool] = None, selected_contacts: Optional[bool] = None, out: Optional[bool] = None, from_id: "ayiin.Peer" = None, fwd_from: "ayiin.StoryFwdHeader" = None, caption: Optional[str] = None, entities: Optional[List["ayiin.MessageEntity"]] = None, media_areas: Optional[List["ayiin.MediaArea"]] = None, privacy: Optional[List["ayiin.PrivacyRule"]] = None, views: "ayiin.StoryViews" = None, sent_reaction: "ayiin.Reaction" = None) -> None:
        
                self.id = id  # int
        
                self.date = date  # int
        
                self.expire_date = expire_date  # int
        
                self.media = media  # MessageMedia
        
                self.pinned = pinned  # true
        
                self.public = public  # true
        
                self.close_friends = close_friends  # true
        
                self.min = min  # true
        
                self.noforwards = noforwards  # true
        
                self.edited = edited  # true
        
                self.contacts = contacts  # true
        
                self.selected_contacts = selected_contacts  # true
        
                self.out = out  # true
        
                self.from_id = from_id  # Peer
        
                self.fwd_from = fwd_from  # StoryFwdHeader
        
                self.caption = caption  # string
        
                self.entities = entities  # MessageEntity
        
                self.media_areas = media_areas  # MediaArea
        
                self.privacy = privacy  # PrivacyRule
        
                self.views = views  # StoryViews
        
                self.sent_reaction = sent_reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryItem":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 5) else False
        public = True if flags & (1 << 7) else False
        close_friends = True if flags & (1 << 8) else False
        min = True if flags & (1 << 9) else False
        noforwards = True if flags & (1 << 10) else False
        edited = True if flags & (1 << 11) else False
        contacts = True if flags & (1 << 12) else False
        selected_contacts = True if flags & (1 << 13) else False
        out = True if flags & (1 << 16) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        from_id = Object.read(b) if flags & (1 << 18) else None
        
        fwd_from = Object.read(b) if flags & (1 << 17) else None
        
        expire_date = Int.read(b)
        
        caption = String.read(b) if flags & (1 << 0) else None
        entities = Object.read(b) if flags & (1 << 1) else []
        
        media = Object.read(b)
        
        media_areas = Object.read(b) if flags & (1 << 14) else []
        
        privacy = Object.read(b) if flags & (1 << 2) else []
        
        views = Object.read(b) if flags & (1 << 3) else None
        
        sent_reaction = Object.read(b) if flags & (1 << 15) else None
        
        return StoryItem(id=id, date=date, expire_date=expire_date, media=media, pinned=pinned, public=public, close_friends=close_friends, min=min, noforwards=noforwards, edited=edited, contacts=contacts, selected_contacts=selected_contacts, out=out, from_id=from_id, fwd_from=fwd_from, caption=caption, entities=entities, media_areas=media_areas, privacy=privacy, views=views, sent_reaction=sent_reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.fwd_from is not None:
            b.write(self.fwd_from.write())
        
        b.write(Int(self.expire_date))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.privacy is not None:
            b.write(Vector(self.privacy))
        
        if self.views is not None:
            b.write(self.views.write())
        
        if self.sent_reaction is not None:
            b.write(self.sent_reaction.write())
        
        return b.getvalue()