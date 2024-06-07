
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



class ReplyKeyboardMarkup(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``85DD99D1``

rows (List of :obj:`KeyboardButtonRow<typegram.api.ayiin.KeyboardButtonRow>`):
                    N/A
                
        resize (``bool``, *optional*):
                    N/A
                
        single_use (``bool``, *optional*):
                    N/A
                
        selective (``bool``, *optional*):
                    N/A
                
        persistent (``bool``, *optional*):
                    N/A
                
        placeholder (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 12 functions.

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

    __slots__: List[str] = ["rows", "resize", "single_use", "selective", "persistent", "placeholder"]

    ID = 0x85dd99d1
    QUALNAME = "functions.types.ReplyMarkup"

    def __init__(self, *, rows: List["ayiin.KeyboardButtonRow"], resize: Optional[bool] = None, single_use: Optional[bool] = None, selective: Optional[bool] = None, persistent: Optional[bool] = None, placeholder: Optional[str] = None) -> None:
        
                self.rows = rows  # KeyboardButtonRow
        
                self.resize = resize  # true
        
                self.single_use = single_use  # true
        
                self.selective = selective  # true
        
                self.persistent = persistent  # true
        
                self.placeholder = placeholder  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardMarkup":
        
        flags = Int.read(b)
        
        resize = True if flags & (1 << 0) else False
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        persistent = True if flags & (1 << 4) else False
        rows = Object.read(b)
        
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardMarkup(rows=rows, resize=resize, single_use=single_use, selective=selective, persistent=persistent, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.rows))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()