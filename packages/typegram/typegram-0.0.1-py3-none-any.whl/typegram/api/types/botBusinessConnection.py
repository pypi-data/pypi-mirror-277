
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



class BotBusinessConnection(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotBusinessConnection`.

    Details:
        - Layer: ``181``
        - ID: ``896433B4``

connection_id (``str``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        dc_id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        can_reply (``bool``, *optional*):
                    N/A
                
        disabled (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 22 functions.

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

    __slots__: List[str] = ["connection_id", "user_id", "dc_id", "date", "can_reply", "disabled"]

    ID = 0x896433b4
    QUALNAME = "functions.types.BotBusinessConnection"

    def __init__(self, *, connection_id: str, user_id: int, dc_id: int, date: int, can_reply: Optional[bool] = None, disabled: Optional[bool] = None) -> None:
        
                self.connection_id = connection_id  # string
        
                self.user_id = user_id  # long
        
                self.dc_id = dc_id  # int
        
                self.date = date  # int
        
                self.can_reply = can_reply  # true
        
                self.disabled = disabled  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotBusinessConnection":
        
        flags = Int.read(b)
        
        can_reply = True if flags & (1 << 0) else False
        disabled = True if flags & (1 << 1) else False
        connection_id = String.read(b)
        
        user_id = Long.read(b)
        
        dc_id = Int.read(b)
        
        date = Int.read(b)
        
        return BotBusinessConnection(connection_id=connection_id, user_id=user_id, dc_id=dc_id, date=date, can_reply=can_reply, disabled=disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.connection_id))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.dc_id))
        
        b.write(Int(self.date))
        
        return b.getvalue()