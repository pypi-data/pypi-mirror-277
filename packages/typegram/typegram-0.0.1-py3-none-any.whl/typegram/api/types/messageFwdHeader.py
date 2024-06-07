
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



class MessageFwdHeader(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageFwdHeader`.

    Details:
        - Layer: ``181``
        - ID: ``4E4DF4BB``

date (``int`` ``32-bit``):
                    N/A
                
        imported (``bool``, *optional*):
                    N/A
                
        saved_out (``bool``, *optional*):
                    N/A
                
        from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        from_name (``str``, *optional*):
                    N/A
                
        channel_post (``int`` ``32-bit``, *optional*):
                    N/A
                
        post_author (``str``, *optional*):
                    N/A
                
        saved_from_peer (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        saved_from_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        saved_from_id (:obj:`Peer<typegram.api.ayiin.Peer>`, *optional*):
                    N/A
                
        saved_from_name (``str``, *optional*):
                    N/A
                
        saved_date (``int`` ``32-bit``, *optional*):
                    N/A
                
        psa_type (``str``, *optional*):
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

    __slots__: List[str] = ["date", "imported", "saved_out", "from_id", "from_name", "channel_post", "post_author", "saved_from_peer", "saved_from_msg_id", "saved_from_id", "saved_from_name", "saved_date", "psa_type"]

    ID = 0x4e4df4bb
    QUALNAME = "functions.types.MessageFwdHeader"

    def __init__(self, *, date: int, imported: Optional[bool] = None, saved_out: Optional[bool] = None, from_id: "ayiin.Peer" = None, from_name: Optional[str] = None, channel_post: Optional[int] = None, post_author: Optional[str] = None, saved_from_peer: "ayiin.Peer" = None, saved_from_msg_id: Optional[int] = None, saved_from_id: "ayiin.Peer" = None, saved_from_name: Optional[str] = None, saved_date: Optional[int] = None, psa_type: Optional[str] = None) -> None:
        
                self.date = date  # int
        
                self.imported = imported  # true
        
                self.saved_out = saved_out  # true
        
                self.from_id = from_id  # Peer
        
                self.from_name = from_name  # string
        
                self.channel_post = channel_post  # int
        
                self.post_author = post_author  # string
        
                self.saved_from_peer = saved_from_peer  # Peer
        
                self.saved_from_msg_id = saved_from_msg_id  # int
        
                self.saved_from_id = saved_from_id  # Peer
        
                self.saved_from_name = saved_from_name  # string
        
                self.saved_date = saved_date  # int
        
                self.psa_type = psa_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageFwdHeader":
        
        flags = Int.read(b)
        
        imported = True if flags & (1 << 7) else False
        saved_out = True if flags & (1 << 11) else False
        from_id = Object.read(b) if flags & (1 << 0) else None
        
        from_name = String.read(b) if flags & (1 << 5) else None
        date = Int.read(b)
        
        channel_post = Int.read(b) if flags & (1 << 2) else None
        post_author = String.read(b) if flags & (1 << 3) else None
        saved_from_peer = Object.read(b) if flags & (1 << 4) else None
        
        saved_from_msg_id = Int.read(b) if flags & (1 << 4) else None
        saved_from_id = Object.read(b) if flags & (1 << 8) else None
        
        saved_from_name = String.read(b) if flags & (1 << 9) else None
        saved_date = Int.read(b) if flags & (1 << 10) else None
        psa_type = String.read(b) if flags & (1 << 6) else None
        return MessageFwdHeader(date=date, imported=imported, saved_out=saved_out, from_id=from_id, from_name=from_name, channel_post=channel_post, post_author=post_author, saved_from_peer=saved_from_peer, saved_from_msg_id=saved_from_msg_id, saved_from_id=saved_from_id, saved_from_name=saved_from_name, saved_date=saved_date, psa_type=psa_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.from_name is not None:
            b.write(String(self.from_name))
        
        b.write(Int(self.date))
        
        if self.channel_post is not None:
            b.write(Int(self.channel_post))
        
        if self.post_author is not None:
            b.write(String(self.post_author))
        
        if self.saved_from_peer is not None:
            b.write(self.saved_from_peer.write())
        
        if self.saved_from_msg_id is not None:
            b.write(Int(self.saved_from_msg_id))
        
        if self.saved_from_id is not None:
            b.write(self.saved_from_id.write())
        
        if self.saved_from_name is not None:
            b.write(String(self.saved_from_name))
        
        if self.saved_date is not None:
            b.write(Int(self.saved_date))
        
        if self.psa_type is not None:
            b.write(String(self.psa_type))
        
        return b.getvalue()