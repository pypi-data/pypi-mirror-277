
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



class StickerSetFullCovered(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.StickerSetCovered`.

    Details:
        - Layer: ``181``
        - ID: ``40D13C0E``

set (:obj:`StickerSet<typegram.api.ayiin.StickerSet>`):
                    N/A
                
        packs (List of :obj:`StickerPack<typegram.api.ayiin.StickerPack>`):
                    N/A
                
        keywords (List of :obj:`StickerKeyword<typegram.api.ayiin.StickerKeyword>`):
                    N/A
                
        documents (List of :obj:`Document<typegram.api.ayiin.Document>`):
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

    __slots__: List[str] = ["set", "packs", "keywords", "documents"]

    ID = 0x40d13c0e
    QUALNAME = "functions.types.StickerSetCovered"

    def __init__(self, *, set: "ayiin.StickerSet", packs: List["ayiin.StickerPack"], keywords: List["ayiin.StickerKeyword"], documents: List["ayiin.Document"]) -> None:
        
                self.set = set  # StickerSet
        
                self.packs = packs  # StickerPack
        
                self.keywords = keywords  # StickerKeyword
        
                self.documents = documents  # Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSetFullCovered":
        # No flags
        
        set = Object.read(b)
        
        packs = Object.read(b)
        
        keywords = Object.read(b)
        
        documents = Object.read(b)
        
        return StickerSetFullCovered(set=set, packs=packs, keywords=keywords, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.keywords))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()