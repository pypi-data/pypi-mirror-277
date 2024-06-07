
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



class InputReplyToMessage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputReplyTo`.

    Details:
        - Layer: ``181``
        - ID: ``22C0F6D5``

reply_to_msg_id (``int`` ``32-bit``):
                    N/A
                
        top_msg_id (``int`` ``32-bit``, *optional*):
                    N/A
                
        reply_to_peer_id (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        quote_text (``str``, *optional*):
                    N/A
                
        quote_entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`, *optional*):
                    N/A
                
        quote_offset (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["reply_to_msg_id", "top_msg_id", "reply_to_peer_id", "quote_text", "quote_entities", "quote_offset"]

    ID = 0x22c0f6d5
    QUALNAME = "functions.types.InputReplyTo"

    def __init__(self, *, reply_to_msg_id: int, top_msg_id: Optional[int] = None, reply_to_peer_id: "ayiin.InputPeer" = None, quote_text: Optional[str] = None, quote_entities: Optional[List["ayiin.MessageEntity"]] = None, quote_offset: Optional[int] = None) -> None:
        
                self.reply_to_msg_id = reply_to_msg_id  # int
        
                self.top_msg_id = top_msg_id  # int
        
                self.reply_to_peer_id = reply_to_peer_id  # InputPeer
        
                self.quote_text = quote_text  # string
        
                self.quote_entities = quote_entities  # MessageEntity
        
                self.quote_offset = quote_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToMessage":
        
        flags = Int.read(b)
        
        reply_to_msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reply_to_peer_id = Object.read(b) if flags & (1 << 1) else None
        
        quote_text = String.read(b) if flags & (1 << 2) else None
        quote_entities = Object.read(b) if flags & (1 << 3) else []
        
        quote_offset = Int.read(b) if flags & (1 << 4) else None
        return InputReplyToMessage(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.reply_to_msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())
        
        if self.quote_text is not None:
            b.write(String(self.quote_text))
        
        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))
        
        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))
        
        return b.getvalue()