
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



class ChannelForbidden(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Chat`.

    Details:
        - Layer: ``181``
        - ID: ``17D493D5``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        broadcast (``bool``, *optional*):
                    N/A
                
        megagroup (``bool``, *optional*):
                    N/A
                
        until_date (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 5 functions.

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

    __slots__: List[str] = ["id", "access_hash", "title", "broadcast", "megagroup", "until_date"]

    ID = 0x17d493d5
    QUALNAME = "functions.types.Chat"

    def __init__(self, *, id: int, access_hash: int, title: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, until_date: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.title = title  # string
        
                self.broadcast = broadcast  # true
        
                self.megagroup = megagroup  # true
        
                self.until_date = until_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelForbidden":
        
        flags = Int.read(b)
        
        broadcast = True if flags & (1 << 5) else False
        megagroup = True if flags & (1 << 8) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        title = String.read(b)
        
        until_date = Int.read(b) if flags & (1 << 16) else None
        return ChannelForbidden(id=id, access_hash=access_hash, title=title, broadcast=broadcast, megagroup=megagroup, until_date=until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.title))
        
        if self.until_date is not None:
            b.write(Int(self.until_date))
        
        return b.getvalue()