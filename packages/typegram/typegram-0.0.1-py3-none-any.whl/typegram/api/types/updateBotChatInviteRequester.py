
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



class UpdateBotChatInviteRequester(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``11DFA986``

peer (:obj:`Peer<typegram.api.ayiin.Peer>`):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        about (``str``):
                    N/A
                
        invite (:obj:`ExportedChatInvite<typegram.api.ayiin.ExportedChatInvite>`):
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

    __slots__: List[str] = ["peer", "date", "user_id", "about", "invite", "qts"]

    ID = 0x11dfa986
    QUALNAME = "functions.types.Update"

    def __init__(self, *, peer: "ayiin.Peer", date: int, user_id: int, about: str, invite: "ayiin.ExportedChatInvite", qts: int) -> None:
        
                self.peer = peer  # Peer
        
                self.date = date  # int
        
                self.user_id = user_id  # long
        
                self.about = about  # string
        
                self.invite = invite  # ExportedChatInvite
        
                self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotChatInviteRequester":
        # No flags
        
        peer = Object.read(b)
        
        date = Int.read(b)
        
        user_id = Long.read(b)
        
        about = String.read(b)
        
        invite = Object.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotChatInviteRequester(peer=peer, date=date, user_id=user_id, about=about, invite=invite, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.date))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.about))
        
        b.write(self.invite.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()