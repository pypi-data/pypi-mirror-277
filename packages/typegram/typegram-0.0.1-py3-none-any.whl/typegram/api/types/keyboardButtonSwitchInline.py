
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



class KeyboardButtonSwitchInline(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``93B9FBB5``

text (``str``):
                    N/A
                
        query (``str``):
                    N/A
                
        same_peer (``bool``, *optional*):
                    N/A
                
        peer_types (List of :obj:`InlineQueryPeerType<typegram.api.ayiin.InlineQueryPeerType>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 15 functions.

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

    __slots__: List[str] = ["text", "query", "same_peer", "peer_types"]

    ID = 0x93b9fbb5
    QUALNAME = "functions.types.KeyboardButton"

    def __init__(self, *, text: str, query: str, same_peer: Optional[bool] = None, peer_types: Optional[List["ayiin.InlineQueryPeerType"]] = None) -> None:
        
                self.text = text  # string
        
                self.query = query  # string
        
                self.same_peer = same_peer  # true
        
                self.peer_types = peer_types  # InlineQueryPeerType

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonSwitchInline":
        
        flags = Int.read(b)
        
        same_peer = True if flags & (1 << 0) else False
        text = String.read(b)
        
        query = String.read(b)
        
        peer_types = Object.read(b) if flags & (1 << 1) else []
        
        return KeyboardButtonSwitchInline(text=text, query=query, same_peer=same_peer, peer_types=peer_types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        b.write(String(self.query))
        
        if self.peer_types is not None:
            b.write(Vector(self.peer_types))
        
        return b.getvalue()