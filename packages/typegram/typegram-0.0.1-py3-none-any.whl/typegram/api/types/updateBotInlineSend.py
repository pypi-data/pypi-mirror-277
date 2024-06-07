
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



class UpdateBotInlineSend(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``12F12A07``

user_id (``int`` ``64-bit``):
                    N/A
                
        query (``str``):
                    N/A
                
        id (``str``):
                    N/A
                
        geo (:obj:`GeoPoint<typegram.api.ayiin.GeoPoint>`, *optional*):
                    N/A
                
        msg_id (:obj:`InputBotInlineMessageID<typegram.api.ayiin.InputBotInlineMessageID>`, *optional*):
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

    __slots__: List[str] = ["user_id", "query", "id", "geo", "msg_id"]

    ID = 0x12f12a07
    QUALNAME = "functions.types.Update"

    def __init__(self, *, user_id: int, query: str, id: str, geo: "ayiin.GeoPoint" = None, msg_id: "ayiin.InputBotInlineMessageID" = None) -> None:
        
                self.user_id = user_id  # long
        
                self.query = query  # string
        
                self.id = id  # string
        
                self.geo = geo  # GeoPoint
        
                self.msg_id = msg_id  # InputBotInlineMessageID

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotInlineSend":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        query = String.read(b)
        
        geo = Object.read(b) if flags & (1 << 0) else None
        
        id = String.read(b)
        
        msg_id = Object.read(b) if flags & (1 << 1) else None
        
        return UpdateBotInlineSend(user_id=user_id, query=query, id=id, geo=geo, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.query))
        
        if self.geo is not None:
            b.write(self.geo.write())
        
        b.write(String(self.id))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()