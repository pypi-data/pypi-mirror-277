
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



class PeerSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PeerSettings`.

    Details:
        - Layer: ``181``
        - ID: ``ACD66C5E``

report_spam (``bool``, *optional*):
                    N/A
                
        add_contact (``bool``, *optional*):
                    N/A
                
        block_contact (``bool``, *optional*):
                    N/A
                
        share_contact (``bool``, *optional*):
                    N/A
                
        need_contacts_exception (``bool``, *optional*):
                    N/A
                
        report_geo (``bool``, *optional*):
                    N/A
                
        autoarchived (``bool``, *optional*):
                    N/A
                
        invite_members (``bool``, *optional*):
                    N/A
                
        request_chat_broadcast (``bool``, *optional*):
                    N/A
                
        business_bot_paused (``bool``, *optional*):
                    N/A
                
        business_bot_can_reply (``bool``, *optional*):
                    N/A
                
        geo_distance (``int`` ``32-bit``, *optional*):
                    N/A
                
        request_chat_title (``str``, *optional*):
                    N/A
                
        request_chat_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        business_bot_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        business_bot_manage_url (``str``, *optional*):
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

    __slots__: List[str] = ["report_spam", "add_contact", "block_contact", "share_contact", "need_contacts_exception", "report_geo", "autoarchived", "invite_members", "request_chat_broadcast", "business_bot_paused", "business_bot_can_reply", "geo_distance", "request_chat_title", "request_chat_date", "business_bot_id", "business_bot_manage_url"]

    ID = 0xacd66c5e
    QUALNAME = "functions.types.PeerSettings"

    def __init__(self, *, report_spam: Optional[bool] = None, add_contact: Optional[bool] = None, block_contact: Optional[bool] = None, share_contact: Optional[bool] = None, need_contacts_exception: Optional[bool] = None, report_geo: Optional[bool] = None, autoarchived: Optional[bool] = None, invite_members: Optional[bool] = None, request_chat_broadcast: Optional[bool] = None, business_bot_paused: Optional[bool] = None, business_bot_can_reply: Optional[bool] = None, geo_distance: Optional[int] = None, request_chat_title: Optional[str] = None, request_chat_date: Optional[int] = None, business_bot_id: Optional[int] = None, business_bot_manage_url: Optional[str] = None) -> None:
        
                self.report_spam = report_spam  # true
        
                self.add_contact = add_contact  # true
        
                self.block_contact = block_contact  # true
        
                self.share_contact = share_contact  # true
        
                self.need_contacts_exception = need_contacts_exception  # true
        
                self.report_geo = report_geo  # true
        
                self.autoarchived = autoarchived  # true
        
                self.invite_members = invite_members  # true
        
                self.request_chat_broadcast = request_chat_broadcast  # true
        
                self.business_bot_paused = business_bot_paused  # true
        
                self.business_bot_can_reply = business_bot_can_reply  # true
        
                self.geo_distance = geo_distance  # int
        
                self.request_chat_title = request_chat_title  # string
        
                self.request_chat_date = request_chat_date  # int
        
                self.business_bot_id = business_bot_id  # long
        
                self.business_bot_manage_url = business_bot_manage_url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSettings":
        
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        add_contact = True if flags & (1 << 1) else False
        block_contact = True if flags & (1 << 2) else False
        share_contact = True if flags & (1 << 3) else False
        need_contacts_exception = True if flags & (1 << 4) else False
        report_geo = True if flags & (1 << 5) else False
        autoarchived = True if flags & (1 << 7) else False
        invite_members = True if flags & (1 << 8) else False
        request_chat_broadcast = True if flags & (1 << 10) else False
        business_bot_paused = True if flags & (1 << 11) else False
        business_bot_can_reply = True if flags & (1 << 12) else False
        geo_distance = Int.read(b) if flags & (1 << 6) else None
        request_chat_title = String.read(b) if flags & (1 << 9) else None
        request_chat_date = Int.read(b) if flags & (1 << 9) else None
        business_bot_id = Long.read(b) if flags & (1 << 13) else None
        business_bot_manage_url = String.read(b) if flags & (1 << 13) else None
        return PeerSettings(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, business_bot_paused=business_bot_paused, business_bot_can_reply=business_bot_can_reply, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date, business_bot_id=business_bot_id, business_bot_manage_url=business_bot_manage_url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.geo_distance is not None:
            b.write(Int(self.geo_distance))
        
        if self.request_chat_title is not None:
            b.write(String(self.request_chat_title))
        
        if self.request_chat_date is not None:
            b.write(Int(self.request_chat_date))
        
        if self.business_bot_id is not None:
            b.write(Long(self.business_bot_id))
        
        if self.business_bot_manage_url is not None:
            b.write(String(self.business_bot_manage_url))
        
        return b.getvalue()