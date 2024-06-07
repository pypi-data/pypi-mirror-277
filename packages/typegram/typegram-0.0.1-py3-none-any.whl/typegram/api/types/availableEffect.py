
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



class AvailableEffect(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.AvailableEffect`.

    Details:
        - Layer: ``181``
        - ID: ``93C3E27E``

id (``int`` ``64-bit``):
                    N/A
                
        emoticon (``str``):
                    N/A
                
        effect_sticker_id (``int`` ``64-bit``):
                    N/A
                
        premium_required (``bool``, *optional*):
                    N/A
                
        static_icon_id (``int`` ``64-bit``, *optional*):
                    N/A
                
        effect_animation_id (``int`` ``64-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 16 functions.

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

    __slots__: List[str] = ["id", "emoticon", "effect_sticker_id", "premium_required", "static_icon_id", "effect_animation_id"]

    ID = 0x93c3e27e
    QUALNAME = "functions.types.AvailableEffect"

    def __init__(self, *, id: int, emoticon: str, effect_sticker_id: int, premium_required: Optional[bool] = None, static_icon_id: Optional[int] = None, effect_animation_id: Optional[int] = None) -> None:
        
                self.id = id  # long
        
                self.emoticon = emoticon  # string
        
                self.effect_sticker_id = effect_sticker_id  # long
        
                self.premium_required = premium_required  # true
        
                self.static_icon_id = static_icon_id  # long
        
                self.effect_animation_id = effect_animation_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableEffect":
        
        flags = Int.read(b)
        
        premium_required = True if flags & (1 << 2) else False
        id = Long.read(b)
        
        emoticon = String.read(b)
        
        static_icon_id = Long.read(b) if flags & (1 << 0) else None
        effect_sticker_id = Long.read(b)
        
        effect_animation_id = Long.read(b) if flags & (1 << 1) else None
        return AvailableEffect(id=id, emoticon=emoticon, effect_sticker_id=effect_sticker_id, premium_required=premium_required, static_icon_id=static_icon_id, effect_animation_id=effect_animation_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.emoticon))
        
        if self.static_icon_id is not None:
            b.write(Long(self.static_icon_id))
        
        b.write(Long(self.effect_sticker_id))
        
        if self.effect_animation_id is not None:
            b.write(Long(self.effect_animation_id))
        
        return b.getvalue()