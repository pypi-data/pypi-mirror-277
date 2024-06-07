
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



class MessageMediaGiveaway(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``DAAD85B0``

channels (List of ``int`` ``64-bit``):
                    N/A
                
        quantity (``int`` ``32-bit``):
                    N/A
                
        months (``int`` ``32-bit``):
                    N/A
                
        until_date (``int`` ``32-bit``):
                    N/A
                
        only_new_subscribers (``bool``, *optional*):
                    N/A
                
        winners_are_visible (``bool``, *optional*):
                    N/A
                
        countries_iso2 (List of ``str``, *optional*):
                    N/A
                
        prize_description (``str``, *optional*):
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

    __slots__: List[str] = ["channels", "quantity", "months", "until_date", "only_new_subscribers", "winners_are_visible", "countries_iso2", "prize_description"]

    ID = 0xdaad85b0
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, channels: List[int], quantity: int, months: int, until_date: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None) -> None:
        
                self.channels = channels  # long
        
                self.quantity = quantity  # int
        
                self.months = months  # int
        
                self.until_date = until_date  # int
        
                self.only_new_subscribers = only_new_subscribers  # true
        
                self.winners_are_visible = winners_are_visible  # true
        
                self.countries_iso2 = countries_iso2  # string
        
                self.prize_description = prize_description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGiveaway":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 2) else False
        channels = Object.read(b, Long)
        
        countries_iso2 = Object.read(b, String) if flags & (1 << 1) else []
        
        prize_description = String.read(b) if flags & (1 << 3) else None
        quantity = Int.read(b)
        
        months = Int.read(b)
        
        until_date = Int.read(b)
        
        return MessageMediaGiveaway(channels=channels, quantity=quantity, months=months, until_date=until_date, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, countries_iso2=countries_iso2, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Vector(self.channels, Long))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Int(self.quantity))
        
        b.write(Int(self.months))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()