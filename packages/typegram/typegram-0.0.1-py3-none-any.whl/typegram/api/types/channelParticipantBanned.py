
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



class ChannelParticipantBanned(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChannelParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``6DF8014E``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        kicked_by (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        banned_rights (:obj:`ChatBannedRights<typegram.api.ayiin.ChatBannedRights>`):
                    N/A
                
        left (``bool``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["peer", "kicked_by", "date", "banned_rights", "left"]

    ID = 0x6df8014e
    QUALNAME = "functions.types.ChannelParticipant"

    def __init__(self, *, peer: "ayiin.Peer", kicked_by: int, date: int, banned_rights: "ayiin.ChatBannedRights", left: Optional[bool] = None) -> None:
        
                self.peer = peer  # Peer
        
                self.kicked_by = kicked_by  # long
        
                self.date = date  # int
        
                self.banned_rights = banned_rights  # ChatBannedRights
        
                self.left = left  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantBanned":
        
        flags = Int.read(b)
        
        left = True if flags & (1 << 0) else False
        peer = Object.read(b)
        
        kicked_by = Long.read(b)
        
        date = Int.read(b)
        
        banned_rights = Object.read(b)
        
        return ChannelParticipantBanned(peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, left=left)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.kicked_by))
        
        b.write(Int(self.date))
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()