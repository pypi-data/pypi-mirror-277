
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



class LangPackStringPluralized(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.LangPackString`.

    Details:
        - Layer: ``181``
        - ID: ``6C47AC9F``

key (``str``):
                    N/A
                
        other_value (``str``):
                    N/A
                
        zero_value (``str``, *optional*):
                    N/A
                
        one_value (``str``, *optional*):
                    N/A
                
        two_value (``str``, *optional*):
                    N/A
                
        few_value (``str``, *optional*):
                    N/A
                
        many_value (``str``, *optional*):
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

    __slots__: List[str] = ["key", "other_value", "zero_value", "one_value", "two_value", "few_value", "many_value"]

    ID = 0x6c47ac9f
    QUALNAME = "functions.types.LangPackString"

    def __init__(self, *, key: str, other_value: str, zero_value: Optional[str] = None, one_value: Optional[str] = None, two_value: Optional[str] = None, few_value: Optional[str] = None, many_value: Optional[str] = None) -> None:
        
                self.key = key  # string
        
                self.other_value = other_value  # string
        
                self.zero_value = zero_value  # string
        
                self.one_value = one_value  # string
        
                self.two_value = two_value  # string
        
                self.few_value = few_value  # string
        
                self.many_value = many_value  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackStringPluralized":
        
        flags = Int.read(b)
        
        key = String.read(b)
        
        zero_value = String.read(b) if flags & (1 << 0) else None
        one_value = String.read(b) if flags & (1 << 1) else None
        two_value = String.read(b) if flags & (1 << 2) else None
        few_value = String.read(b) if flags & (1 << 3) else None
        many_value = String.read(b) if flags & (1 << 4) else None
        other_value = String.read(b)
        
        return LangPackStringPluralized(key=key, other_value=other_value, zero_value=zero_value, one_value=one_value, two_value=two_value, few_value=few_value, many_value=many_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.key))
        
        if self.zero_value is not None:
            b.write(String(self.zero_value))
        
        if self.one_value is not None:
            b.write(String(self.one_value))
        
        if self.two_value is not None:
            b.write(String(self.two_value))
        
        if self.few_value is not None:
            b.write(String(self.few_value))
        
        if self.many_value is not None:
            b.write(String(self.many_value))
        
        b.write(String(self.other_value))
        
        return b.getvalue()