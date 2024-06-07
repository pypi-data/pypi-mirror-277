
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



class InputMediaWebPage(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``C21B8849``

url (``str``):
                    N/A
                
        force_large_media (``bool``, *optional*):
                    N/A
                
        force_small_media (``bool``, *optional*):
                    N/A
                
        optional (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 11 functions.

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

    __slots__: List[str] = ["url", "force_large_media", "force_small_media", "optional"]

    ID = 0xc21b8849
    QUALNAME = "functions.types.InputMedia"

    def __init__(self, *, url: str, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None) -> None:
        
                self.url = url  # string
        
                self.force_large_media = force_large_media  # true
        
                self.force_small_media = force_small_media  # true
        
                self.optional = optional  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaWebPage":
        
        flags = Int.read(b)
        
        force_large_media = True if flags & (1 << 0) else False
        force_small_media = True if flags & (1 << 1) else False
        optional = True if flags & (1 << 2) else False
        url = String.read(b)
        
        return InputMediaWebPage(url=url, force_large_media=force_large_media, force_small_media=force_small_media, optional=optional)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        return b.getvalue()