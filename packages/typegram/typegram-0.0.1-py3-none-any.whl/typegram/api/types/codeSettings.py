
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



class CodeSettings(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.CodeSettings`.

    Details:
        - Layer: ``181``
        - ID: ``AD253D78``

allow_flashcall (``bool``, *optional*):
                    N/A
                
        current_number (``bool``, *optional*):
                    N/A
                
        allow_app_hash (``bool``, *optional*):
                    N/A
                
        allow_missed_call (``bool``, *optional*):
                    N/A
                
        allow_firebase (``bool``, *optional*):
                    N/A
                
        unknown_number (``bool``, *optional*):
                    N/A
                
        logout_tokens (List of ``bytes``, *optional*):
                    N/A
                
        token (``str``, *optional*):
                    N/A
                
        app_sandbox (``bool``, *optional*):
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

    __slots__: List[str] = ["allow_flashcall", "current_number", "allow_app_hash", "allow_missed_call", "allow_firebase", "unknown_number", "logout_tokens", "token", "app_sandbox"]

    ID = 0xad253d78
    QUALNAME = "functions.types.CodeSettings"

    def __init__(self, *, allow_flashcall: Optional[bool] = None, current_number: Optional[bool] = None, allow_app_hash: Optional[bool] = None, allow_missed_call: Optional[bool] = None, allow_firebase: Optional[bool] = None, unknown_number: Optional[bool] = None, logout_tokens: Optional[List[bytes]] = None, token: Optional[str] = None, app_sandbox: Optional[bool] = None) -> None:
        
                self.allow_flashcall = allow_flashcall  # true
        
                self.current_number = current_number  # true
        
                self.allow_app_hash = allow_app_hash  # true
        
                self.allow_missed_call = allow_missed_call  # true
        
                self.allow_firebase = allow_firebase  # true
        
                self.unknown_number = unknown_number  # true
        
                self.logout_tokens = logout_tokens  # bytes
        
                self.token = token  # string
        
                self.app_sandbox = app_sandbox  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CodeSettings":
        
        flags = Int.read(b)
        
        allow_flashcall = True if flags & (1 << 0) else False
        current_number = True if flags & (1 << 1) else False
        allow_app_hash = True if flags & (1 << 4) else False
        allow_missed_call = True if flags & (1 << 5) else False
        allow_firebase = True if flags & (1 << 7) else False
        unknown_number = True if flags & (1 << 9) else False
        logout_tokens = Object.read(b, Bytes) if flags & (1 << 6) else []
        
        token = String.read(b) if flags & (1 << 8) else None
        app_sandbox = Bool.read(b) if flags & (1 << 8) else None
        return CodeSettings(allow_flashcall=allow_flashcall, current_number=current_number, allow_app_hash=allow_app_hash, allow_missed_call=allow_missed_call, allow_firebase=allow_firebase, unknown_number=unknown_number, logout_tokens=logout_tokens, token=token, app_sandbox=app_sandbox)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.logout_tokens is not None:
            b.write(Vector(self.logout_tokens, Bytes))
        
        if self.token is not None:
            b.write(String(self.token))
        
        if self.app_sandbox is not None:
            b.write(Bool(self.app_sandbox))
        
        return b.getvalue()