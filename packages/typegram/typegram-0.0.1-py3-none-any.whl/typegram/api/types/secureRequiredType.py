
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



class SecureRequiredType(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.SecureRequiredType`.

    Details:
        - Layer: ``181``
        - ID: ``829D99DA``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        native_names (``bool``, *optional*):
                    N/A
                
        is_selfie_required (``bool``, *optional*):
                    N/A
                
        translation_required (``bool``, *optional*):
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

    __slots__: List[str] = ["type", "native_names", "is_selfie_required", "translation_required"]

    ID = 0x829d99da
    QUALNAME = "functions.types.SecureRequiredType"

    def __init__(self, *, type: "ayiin.SecureValueType", native_names: Optional[bool] = None, is_selfie_required: Optional[bool] = None, translation_required: Optional[bool] = None) -> None:
        
                self.type = type  # SecureValueType
        
                self.native_names = native_names  # true
        
                self.is_selfie_required = is_selfie_required  # true
        
                self.translation_required = translation_required  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureRequiredType":
        
        flags = Int.read(b)
        
        native_names = True if flags & (1 << 0) else False
        is_selfie_required = True if flags & (1 << 1) else False
        translation_required = True if flags & (1 << 2) else False
        type = Object.read(b)
        
        return SecureRequiredType(type=type, native_names=native_names, is_selfie_required=is_selfie_required, translation_required=translation_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        return b.getvalue()