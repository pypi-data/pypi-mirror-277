
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



class InputKeyboardButtonUrlAuth(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``D02E7FD4``

text (``str``):
                    N/A
                
        url (``str``):
                    N/A
                
        bot (:obj:`InputUser<typegram.api.ayiin.InputUser>`):
                    N/A
                
        request_write_access (``bool``, *optional*):
                    N/A
                
        fwd_text (``str``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["text", "url", "bot", "request_write_access", "fwd_text"]

    ID = 0xd02e7fd4
    QUALNAME = "functions.types.KeyboardButton"

    def __init__(self, *, text: str, url: str, bot: "ayiin.InputUser", request_write_access: Optional[bool] = None, fwd_text: Optional[str] = None) -> None:
        
                self.text = text  # string
        
                self.url = url  # string
        
                self.bot = bot  # InputUser
        
                self.request_write_access = request_write_access  # true
        
                self.fwd_text = fwd_text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = Object.read(b)
        
        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(self.bot.write())
        
        return b.getvalue()