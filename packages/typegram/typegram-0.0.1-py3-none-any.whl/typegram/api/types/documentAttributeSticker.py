
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



class DocumentAttributeSticker(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.DocumentAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``6319D612``

alt (``str``):
                    N/A
                
        stickerset (:obj:`InputStickerSet<typegram.api.ayiin.InputStickerSet>`):
                    N/A
                
        mask (``bool``, *optional*):
                    N/A
                
        mask_coords (:obj:`MaskCoords<typegram.api.ayiin.MaskCoords>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 18 functions.

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

    __slots__: List[str] = ["alt", "stickerset", "mask", "mask_coords"]

    ID = 0x6319d612
    QUALNAME = "functions.types.DocumentAttribute"

    def __init__(self, *, alt: str, stickerset: "ayiin.InputStickerSet", mask: Optional[bool] = None, mask_coords: "ayiin.MaskCoords" = None) -> None:
        
                self.alt = alt  # string
        
                self.stickerset = stickerset  # InputStickerSet
        
                self.mask = mask  # true
        
                self.mask_coords = mask_coords  # MaskCoords

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeSticker":
        
        flags = Int.read(b)
        
        mask = True if flags & (1 << 1) else False
        alt = String.read(b)
        
        stickerset = Object.read(b)
        
        mask_coords = Object.read(b) if flags & (1 << 0) else None
        
        return DocumentAttributeSticker(alt=alt, stickerset=stickerset, mask=mask, mask_coords=mask_coords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.alt))
        
        b.write(self.stickerset.write())
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        return b.getvalue()