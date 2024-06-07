
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



class DocumentAttributeAudio(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DocumentAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``9852F9C6``

duration (``int`` ``32-bit``):
                    N/A
                
        voice (``bool``, *optional*):
                    N/A
                
        title (``str``, *optional*):
                    N/A
                
        performer (``str``, *optional*):
                    N/A
                
        waveform (``bytes``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["duration", "voice", "title", "performer", "waveform"]

    ID = 0x9852f9c6
    QUALNAME = "functions.types.DocumentAttribute"

    def __init__(self, *, duration: int, voice: Optional[bool] = None, title: Optional[str] = None, performer: Optional[str] = None, waveform: Optional[bytes] = None) -> None:
        
                self.duration = duration  # int
        
                self.voice = voice  # true
        
                self.title = title  # string
        
                self.performer = performer  # string
        
                self.waveform = waveform  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeAudio":
        
        flags = Int.read(b)
        
        voice = True if flags & (1 << 10) else False
        duration = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        performer = String.read(b) if flags & (1 << 1) else None
        waveform = Bytes.read(b) if flags & (1 << 2) else None
        return DocumentAttributeAudio(duration=duration, voice=voice, title=title, performer=performer, waveform=waveform)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.duration))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.performer is not None:
            b.write(String(self.performer))
        
        if self.waveform is not None:
            b.write(Bytes(self.waveform))
        
        return b.getvalue()