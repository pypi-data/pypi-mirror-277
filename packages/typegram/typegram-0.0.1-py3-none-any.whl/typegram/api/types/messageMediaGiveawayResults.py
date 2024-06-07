
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



class MessageMediaGiveawayResults(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``C6991068``

channel_id (``int`` ``64-bit``):
                    N/A
                
        launch_msg_id (``int`` ``32-bit``):
                    N/A
                
        winners_count (``int`` ``32-bit``):
                    N/A
                
        unclaimed_count (``int`` ``32-bit``):
                    N/A
                
        winners (List of ``int`` ``64-bit``):
                    N/A
                
        months (``int`` ``32-bit``):
                    N/A
                
        until_date (``int`` ``32-bit``):
                    N/A
                
        only_new_subscribers (``bool``, *optional*):
                    N/A
                
        refunded (``bool``, *optional*):
                    N/A
                
        additional_peers_count (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["channel_id", "launch_msg_id", "winners_count", "unclaimed_count", "winners", "months", "until_date", "only_new_subscribers", "refunded", "additional_peers_count", "prize_description"]

    ID = 0xc6991068
    QUALNAME = "functions.types.MessageMedia"

    def __init__(self, *, channel_id: int, launch_msg_id: int, winners_count: int, unclaimed_count: int, winners: List[int], months: int, until_date: int, only_new_subscribers: Optional[bool] = None, refunded: Optional[bool] = None, additional_peers_count: Optional[int] = None, prize_description: Optional[str] = None) -> None:
        
                self.channel_id = channel_id  # long
        
                self.launch_msg_id = launch_msg_id  # int
        
                self.winners_count = winners_count  # int
        
                self.unclaimed_count = unclaimed_count  # int
        
                self.winners = winners  # long
        
                self.months = months  # int
        
                self.until_date = until_date  # int
        
                self.only_new_subscribers = only_new_subscribers  # true
        
                self.refunded = refunded  # true
        
                self.additional_peers_count = additional_peers_count  # int
        
                self.prize_description = prize_description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGiveawayResults":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        refunded = True if flags & (1 << 2) else False
        channel_id = Long.read(b)
        
        additional_peers_count = Int.read(b) if flags & (1 << 3) else None
        launch_msg_id = Int.read(b)
        
        winners_count = Int.read(b)
        
        unclaimed_count = Int.read(b)
        
        winners = Object.read(b, Long)
        
        months = Int.read(b)
        
        prize_description = String.read(b) if flags & (1 << 1) else None
        until_date = Int.read(b)
        
        return MessageMediaGiveawayResults(channel_id=channel_id, launch_msg_id=launch_msg_id, winners_count=winners_count, unclaimed_count=unclaimed_count, winners=winners, months=months, until_date=until_date, only_new_subscribers=only_new_subscribers, refunded=refunded, additional_peers_count=additional_peers_count, prize_description=prize_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.additional_peers_count is not None:
            b.write(Int(self.additional_peers_count))
        
        b.write(Int(self.launch_msg_id))
        
        b.write(Int(self.winners_count))
        
        b.write(Int(self.unclaimed_count))
        
        b.write(Vector(self.winners, Long))
        
        b.write(Int(self.months))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()