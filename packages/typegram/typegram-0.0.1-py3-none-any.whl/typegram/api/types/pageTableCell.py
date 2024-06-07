
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



class PageTableCell(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.PageTableCell`.

    Details:
        - Layer: ``181``
        - ID: ``34566B6A``

header (``bool``, *optional*):
                    N/A
                
        align_center (``bool``, *optional*):
                    N/A
                
        align_right (``bool``, *optional*):
                    N/A
                
        valign_middle (``bool``, *optional*):
                    N/A
                
        valign_bottom (``bool``, *optional*):
                    N/A
                
        text (:obj:`RichText<typegram.api.ayiin.RichText>`, *optional*):
                    N/A
                
        colspan (``int`` ``32-bit``, *optional*):
                    N/A
                
        rowspan (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 14 functions.

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

    __slots__: List[str] = ["header", "align_center", "align_right", "valign_middle", "valign_bottom", "text", "colspan", "rowspan"]

    ID = 0x34566b6a
    QUALNAME = "functions.types.PageTableCell"

    def __init__(self, *, header: Optional[bool] = None, align_center: Optional[bool] = None, align_right: Optional[bool] = None, valign_middle: Optional[bool] = None, valign_bottom: Optional[bool] = None, text: "ayiin.RichText" = None, colspan: Optional[int] = None, rowspan: Optional[int] = None) -> None:
        
                self.header = header  # true
        
                self.align_center = align_center  # true
        
                self.align_right = align_right  # true
        
                self.valign_middle = valign_middle  # true
        
                self.valign_bottom = valign_bottom  # true
        
                self.text = text  # RichText
        
                self.colspan = colspan  # int
        
                self.rowspan = rowspan  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageTableCell":
        
        flags = Int.read(b)
        
        header = True if flags & (1 << 0) else False
        align_center = True if flags & (1 << 3) else False
        align_right = True if flags & (1 << 4) else False
        valign_middle = True if flags & (1 << 5) else False
        valign_bottom = True if flags & (1 << 6) else False
        text = Object.read(b) if flags & (1 << 7) else None
        
        colspan = Int.read(b) if flags & (1 << 1) else None
        rowspan = Int.read(b) if flags & (1 << 2) else None
        return PageTableCell(header=header, align_center=align_center, align_right=align_right, valign_middle=valign_middle, valign_bottom=valign_bottom, text=text, colspan=colspan, rowspan=rowspan)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.text is not None:
            b.write(self.text.write())
        
        if self.colspan is not None:
            b.write(Int(self.colspan))
        
        if self.rowspan is not None:
            b.write(Int(self.rowspan))
        
        return b.getvalue()