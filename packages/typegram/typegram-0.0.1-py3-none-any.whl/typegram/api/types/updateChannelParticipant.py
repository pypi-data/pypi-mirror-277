
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



class UpdateChannelParticipant(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``985D3ABB``

channel_id (``int`` ``64-bit``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        actor_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        qts (``int`` ``32-bit``):
                    N/A
                
        via_chatlist (``bool``, *optional*):
                    N/A
                
        prev_participant (:obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`, *optional*):
                    N/A
                
        new_participant (:obj:`ChannelParticipant<typegram.api.ayiin.ChannelParticipant>`, *optional*):
                    N/A
                
        invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`, *optional*):
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

    __slots__: List[str] = ["channel_id", "date", "actor_id", "user_id", "qts", "via_chatlist", "prev_participant", "new_participant", "invite"]

    ID = 0x985d3abb
    QUALNAME = "functions.types.Update"

    def __init__(self, *, channel_id: int, date: int, actor_id: int, user_id: int, qts: int, via_chatlist: Optional[bool] = None, prev_participant: "ayiin.ChannelParticipant" = None, new_participant: "ayiin.ChannelParticipant" = None, invite: "ayiin.ExportedChatInvite" = None) -> None:
        
                self.channel_id = channel_id  # long
        
                self.date = date  # int
        
                self.actor_id = actor_id  # long
        
                self.user_id = user_id  # long
        
                self.qts = qts  # int
        
                self.via_chatlist = via_chatlist  # true
        
                self.prev_participant = prev_participant  # ChannelParticipant
        
                self.new_participant = new_participant  # ChannelParticipant
        
                self.invite = invite  # ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelParticipant":
        
        flags = Int.read(b)
        
        via_chatlist = True if flags & (1 << 3) else False
        channel_id = Long.read(b)
        
        date = Int.read(b)
        
        actor_id = Long.read(b)
        
        user_id = Long.read(b)
        
        prev_participant = Object.read(b) if flags & (1 << 0) else None
        
        new_participant = Object.read(b) if flags & (1 << 1) else None
        
        invite = Object.read(b) if flags & (1 << 2) else None
        
        qts = Int.read(b)
        
        return UpdateChannelParticipant(channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, via_chatlist=via_chatlist, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.actor_id))
        
        b.write(Long(self.user_id))
        
        if self.prev_participant is not None:
            b.write(self.prev_participant.write())
        
        if self.new_participant is not None:
            b.write(self.new_participant.write())
        
        if self.invite is not None:
            b.write(self.invite.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()