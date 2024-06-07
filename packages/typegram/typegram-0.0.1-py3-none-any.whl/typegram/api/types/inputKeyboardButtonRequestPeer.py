
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



class InputKeyboardButtonRequestPeer(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``C9662D05``

text (``str``):
                    N/A
                
        button_id (``int`` ``32-bit``):
                    N/A
                
        peer_type (:obj:`RequestPeerType<typegram.api.ayiin.RequestPeerType>`):
                    N/A
                
        max_quantity (``int`` ``32-bit``):
                    N/A
                
        name_requested (``bool``, *optional*):
                    N/A
                
        username_requested (``bool``, *optional*):
                    N/A
                
        photo_requested (``bool``, *optional*):
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

    __slots__: List[str] = ["text", "button_id", "peer_type", "max_quantity", "name_requested", "username_requested", "photo_requested"]

    ID = 0xc9662d05
    QUALNAME = "functions.types.KeyboardButton"

    def __init__(self, *, text: str, button_id: int, peer_type: "ayiin.RequestPeerType", max_quantity: int, name_requested: Optional[bool] = None, username_requested: Optional[bool] = None, photo_requested: Optional[bool] = None) -> None:
        
                self.text = text  # string
        
                self.button_id = button_id  # int
        
                self.peer_type = peer_type  # RequestPeerType
        
                self.max_quantity = max_quantity  # int
        
                self.name_requested = name_requested  # true
        
                self.username_requested = username_requested  # true
        
                self.photo_requested = photo_requested  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonRequestPeer":
        
        flags = Int.read(b)
        
        name_requested = True if flags & (1 << 0) else False
        username_requested = True if flags & (1 << 1) else False
        photo_requested = True if flags & (1 << 2) else False
        text = String.read(b)
        
        button_id = Int.read(b)
        
        peer_type = Object.read(b)
        
        max_quantity = Int.read(b)
        
        return InputKeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity, name_requested=name_requested, username_requested=username_requested, photo_requested=photo_requested)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()