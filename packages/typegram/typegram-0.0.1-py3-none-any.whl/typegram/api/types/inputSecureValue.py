
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



class InputSecureValue(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.InputSecureValue`.

    Details:
        - Layer: ``181``
        - ID: ``DB21D0A7``

type (:obj:`SecureValueType<typegram.api.ayiin.SecureValueType>`):
                    N/A
                
        data (:obj:`SecureData<typegram.api.ayiin.SecureData>`, *optional*):
                    N/A
                
        front_side (:obj:`InputSecureFile<typegram.api.ayiin.InputSecureFile>`, *optional*):
                    N/A
                
        reverse_side (:obj:`InputSecureFile<typegram.api.ayiin.InputSecureFile>`, *optional*):
                    N/A
                
        is_selfie (:obj:`InputSecureFile<typegram.api.ayiin.InputSecureFile>`, *optional*):
                    N/A
                
        translation (List of :obj:`InputSecureFile<typegram.api.ayiin.InputSecureFile>`, *optional*):
                    N/A
                
        files (List of :obj:`InputSecureFile<typegram.api.ayiin.InputSecureFile>`, *optional*):
                    N/A
                
        plain_data (:obj:`SecurePlainData<typegram.api.ayiin.SecurePlainData>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

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

    __slots__: List[str] = ["type", "data", "front_side", "reverse_side", "is_selfie", "translation", "files", "plain_data"]

    ID = 0xdb21d0a7
    QUALNAME = "functions.types.InputSecureValue"

    def __init__(self, *, type: "ayiin.SecureValueType", data: "ayiin.SecureData" = None, front_side: "ayiin.InputSecureFile" = None, reverse_side: "ayiin.InputSecureFile" = None, is_selfie: "ayiin.InputSecureFile" = None, translation: Optional[List["ayiin.InputSecureFile"]] = None, files: Optional[List["ayiin.InputSecureFile"]] = None, plain_data: "ayiin.SecurePlainData" = None) -> None:
        
                self.type = type  # SecureValueType
        
                self.data = data  # SecureData
        
                self.front_side = front_side  # InputSecureFile
        
                self.reverse_side = reverse_side  # InputSecureFile
        
                self.is_selfie = is_selfie  # InputSecureFile
        
                self.translation = translation  # InputSecureFile
        
                self.files = files  # InputSecureFile
        
                self.plain_data = plain_data  # SecurePlainData

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSecureValue":
        
        flags = Int.read(b)
        
        type = Object.read(b)
        
        data = Object.read(b) if flags & (1 << 0) else None
        
        front_side = Object.read(b) if flags & (1 << 1) else None
        
        reverse_side = Object.read(b) if flags & (1 << 2) else None
        
        is_selfie = Object.read(b) if flags & (1 << 3) else None
        
        translation = Object.read(b) if flags & (1 << 6) else []
        
        files = Object.read(b) if flags & (1 << 4) else []
        
        plain_data = Object.read(b) if flags & (1 << 5) else None
        
        return InputSecureValue(type=type, data=data, front_side=front_side, reverse_side=reverse_side, is_selfie=is_selfie, translation=translation, files=files, plain_data=plain_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        if self.data is not None:
            b.write(self.data.write())
        
        if self.front_side is not None:
            b.write(self.front_side.write())
        
        if self.reverse_side is not None:
            b.write(self.reverse_side.write())
        
        if self.is_selfie is not None:
            b.write(self.is_selfie.write())
        
        if self.translation is not None:
            b.write(Vector(self.translation))
        
        if self.files is not None:
            b.write(Vector(self.files))
        
        if self.plain_data is not None:
            b.write(self.plain_data.write())
        
        return b.getvalue()