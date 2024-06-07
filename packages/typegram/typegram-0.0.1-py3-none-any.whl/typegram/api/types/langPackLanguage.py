
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



class LangPackLanguage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.LangPackLanguage`.

    Details:
        - Layer: ``181``
        - ID: ``EECA5CE3``

name (``str``):
                    N/A
                
        native_name (``str``):
                    N/A
                
        lang_code (``str``):
                    N/A
                
        plural_code (``str``):
                    N/A
                
        strings_count (``int`` ``32-bit``):
                    N/A
                
        translated_count (``int`` ``32-bit``):
                    N/A
                
        translations_url (``str``):
                    N/A
                
        official (``bool``, *optional*):
                    N/A
                
        rtl (``bool``, *optional*):
                    N/A
                
        beta (``bool``, *optional*):
                    N/A
                
        base_lang_code (``str``, *optional*):
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

    __slots__: List[str] = ["name", "native_name", "lang_code", "plural_code", "strings_count", "translated_count", "translations_url", "official", "rtl", "beta", "base_lang_code"]

    ID = 0xeeca5ce3
    QUALNAME = "functions.types.LangPackLanguage"

    def __init__(self, *, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: Optional[bool] = None, rtl: Optional[bool] = None, beta: Optional[bool] = None, base_lang_code: Optional[str] = None) -> None:
        
                self.name = name  # string
        
                self.native_name = native_name  # string
        
                self.lang_code = lang_code  # string
        
                self.plural_code = plural_code  # string
        
                self.strings_count = strings_count  # int
        
                self.translated_count = translated_count  # int
        
                self.translations_url = translations_url  # string
        
                self.official = official  # true
        
                self.rtl = rtl  # true
        
                self.beta = beta  # true
        
                self.base_lang_code = base_lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackLanguage":
        
        flags = Int.read(b)
        
        official = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 2) else False
        beta = True if flags & (1 << 3) else False
        name = String.read(b)
        
        native_name = String.read(b)
        
        lang_code = String.read(b)
        
        base_lang_code = String.read(b) if flags & (1 << 1) else None
        plural_code = String.read(b)
        
        strings_count = Int.read(b)
        
        translated_count = Int.read(b)
        
        translations_url = String.read(b)
        
        return LangPackLanguage(name=name, native_name=native_name, lang_code=lang_code, plural_code=plural_code, strings_count=strings_count, translated_count=translated_count, translations_url=translations_url, official=official, rtl=rtl, beta=beta, base_lang_code=base_lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(String(self.native_name))
        
        b.write(String(self.lang_code))
        
        if self.base_lang_code is not None:
            b.write(String(self.base_lang_code))
        
        b.write(String(self.plural_code))
        
        b.write(Int(self.strings_count))
        
        b.write(Int(self.translated_count))
        
        b.write(String(self.translations_url))
        
        return b.getvalue()