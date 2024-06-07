
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



class WallPaperNoFile(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.WallPaper`.

    Details:
        - Layer: ``181``
        - ID: ``E0804116``

id (``int`` ``64-bit``):
                    N/A
                
        default (``bool``, *optional*):
                    N/A
                
        dark (``bool``, *optional*):
                    N/A
                
        settings (:obj:`WallPaperSettings<typegram.api.ayiin.WallPaperSettings>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 10 functions.

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

    __slots__: List[str] = ["id", "default", "dark", "settings"]

    ID = 0xe0804116
    QUALNAME = "functions.types.WallPaper"

    def __init__(self, *, id: int, default: Optional[bool] = None, dark: Optional[bool] = None, settings: "ayiin.WallPaperSettings" = None) -> None:
        
                self.id = id  # long
        
                self.default = default  # true
        
                self.dark = dark  # true
        
                self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaperNoFile":
        
        id = Long.read(b)
        
        flags = Int.read(b)
        
        default = True if flags & (1 << 1) else False
        dark = True if flags & (1 << 4) else False
        settings = Object.read(b) if flags & (1 << 2) else None
        
        return WallPaperNoFile(id=id, default=default, dark=dark, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        
        b.write(Int(flags))
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()