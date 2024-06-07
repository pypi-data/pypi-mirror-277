
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



class UpdateInlineBotCallbackQuery(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Update`.

    Details:
        - Layer: ``181``
        - ID: ``691E9052``

query_id (``int`` ``64-bit``):
                    N/A
                
        user_id (``int`` ``64-bit``):
                    N/A
                
        msg_id (:obj:`InputBotInlineMessageID<typegram.api.ayiin.InputBotInlineMessageID>`):
                    N/A
                
        chat_instance (``int`` ``64-bit``):
                    N/A
                
        data (``bytes``, *optional*):
                    N/A
                
        game_short_name (``str``, *optional*):
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

    __slots__: List[str] = ["query_id", "user_id", "msg_id", "chat_instance", "data", "game_short_name"]

    ID = 0x691e9052
    QUALNAME = "functions.types.Update"

    def __init__(self, *, query_id: int, user_id: int, msg_id: "ayiin.InputBotInlineMessageID", chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None) -> None:
        
                self.query_id = query_id  # long
        
                self.user_id = user_id  # long
        
                self.msg_id = msg_id  # InputBotInlineMessageID
        
                self.chat_instance = chat_instance  # long
        
                self.data = data  # bytes
        
                self.game_short_name = game_short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateInlineBotCallbackQuery":
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        msg_id = Object.read(b)
        
        chat_instance = Long.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        game_short_name = String.read(b) if flags & (1 << 1) else None
        return UpdateInlineBotCallbackQuery(query_id=query_id, user_id=user_id, msg_id=msg_id, chat_instance=chat_instance, data=data, game_short_name=game_short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        b.write(self.msg_id.write())
        
        b.write(Long(self.chat_instance))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.game_short_name is not None:
            b.write(String(self.game_short_name))
        
        return b.getvalue()