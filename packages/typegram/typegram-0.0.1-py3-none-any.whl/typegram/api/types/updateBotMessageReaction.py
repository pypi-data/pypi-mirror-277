
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



class UpdateBotMessageReaction(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``AC21D3CE``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        msg_id (``int`` ``32-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        actor (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        old_reactions (List of :obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        new_reactions (List of :obj:`Reaction<typegram.api.ayiin.Reaction>`):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
    Functions:
        This object can be returned by 7 functions.

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

    __slots__: List[str] = ["peer", "msg_id", "date", "actor", "old_reactions", "new_reactions", "qts"]

    ID = 0xac21d3ce
    QUALNAME = "functions.types.Update"

    def __init__(self, *, peer: "ayiin.Peer", msg_id: int, date: int, actor: "ayiin.Peer", old_reactions: List["ayiin.Reaction"], new_reactions: List["ayiin.Reaction"], qts: int) -> None:
        
                self.peer = peer  # Peer
        
                self.msg_id = msg_id  # int
        
                self.date = date  # int
        
                self.actor = actor  # Peer
        
                self.old_reactions = old_reactions  # Reaction
        
                self.new_reactions = new_reactions  # Reaction
        
                self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotMessageReaction":
        # No flags
        
        peer = Object.read(b)
        
        msg_id = Int.read(b)
        
        date = Int.read(b)
        
        actor = Object.read(b)
        
        old_reactions = Object.read(b)
        
        new_reactions = Object.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotMessageReaction(peer=peer, msg_id=msg_id, date=date, actor=actor, old_reactions=old_reactions, new_reactions=new_reactions, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.date))
        
        b.write(self.actor.write())
        
        b.write(Vector(self.old_reactions))
        
        b.write(Vector(self.new_reactions))
        
        b.write(Int(self.qts))
        
        return b.getvalue()