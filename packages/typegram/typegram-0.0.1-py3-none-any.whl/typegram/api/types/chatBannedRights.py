
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



class ChatBannedRights(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.ChatBannedRights`.

    Details:
        - Layer: ``181``
        - ID: ``9F120418``

until_date (``int`` ``32-bit``):
                    N/A
                
        view_messages (``bool``, *optional*):
                    N/A
                
        send_messages (``bool``, *optional*):
                    N/A
                
        send_media (``bool``, *optional*):
                    N/A
                
        send_stickers (``bool``, *optional*):
                    N/A
                
        send_gifs (``bool``, *optional*):
                    N/A
                
        send_games (``bool``, *optional*):
                    N/A
                
        send_inline (``bool``, *optional*):
                    N/A
                
        embed_links (``bool``, *optional*):
                    N/A
                
        send_polls (``bool``, *optional*):
                    N/A
                
        change_info (``bool``, *optional*):
                    N/A
                
        invite_users (``bool``, *optional*):
                    N/A
                
        pin_messages (``bool``, *optional*):
                    N/A
                
        manage_topics (``bool``, *optional*):
                    N/A
                
        send_photos (``bool``, *optional*):
                    N/A
                
        send_videos (``bool``, *optional*):
                    N/A
                
        send_roundvideos (``bool``, *optional*):
                    N/A
                
        send_audios (``bool``, *optional*):
                    N/A
                
        send_voices (``bool``, *optional*):
                    N/A
                
        send_docs (``bool``, *optional*):
                    N/A
                
        send_plain (``bool``, *optional*):
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

    __slots__: List[str] = ["until_date", "view_messages", "send_messages", "send_media", "send_stickers", "send_gifs", "send_games", "send_inline", "embed_links", "send_polls", "change_info", "invite_users", "pin_messages", "manage_topics", "send_photos", "send_videos", "send_roundvideos", "send_audios", "send_voices", "send_docs", "send_plain"]

    ID = 0x9f120418
    QUALNAME = "functions.types.ChatBannedRights"

    def __init__(self, *, until_date: int, view_messages: Optional[bool] = None, send_messages: Optional[bool] = None, send_media: Optional[bool] = None, send_stickers: Optional[bool] = None, send_gifs: Optional[bool] = None, send_games: Optional[bool] = None, send_inline: Optional[bool] = None, embed_links: Optional[bool] = None, send_polls: Optional[bool] = None, change_info: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, manage_topics: Optional[bool] = None, send_photos: Optional[bool] = None, send_videos: Optional[bool] = None, send_roundvideos: Optional[bool] = None, send_audios: Optional[bool] = None, send_voices: Optional[bool] = None, send_docs: Optional[bool] = None, send_plain: Optional[bool] = None) -> None:
        
                self.until_date = until_date  # int
        
                self.view_messages = view_messages  # true
        
                self.send_messages = send_messages  # true
        
                self.send_media = send_media  # true
        
                self.send_stickers = send_stickers  # true
        
                self.send_gifs = send_gifs  # true
        
                self.send_games = send_games  # true
        
                self.send_inline = send_inline  # true
        
                self.embed_links = embed_links  # true
        
                self.send_polls = send_polls  # true
        
                self.change_info = change_info  # true
        
                self.invite_users = invite_users  # true
        
                self.pin_messages = pin_messages  # true
        
                self.manage_topics = manage_topics  # true
        
                self.send_photos = send_photos  # true
        
                self.send_videos = send_videos  # true
        
                self.send_roundvideos = send_roundvideos  # true
        
                self.send_audios = send_audios  # true
        
                self.send_voices = send_voices  # true
        
                self.send_docs = send_docs  # true
        
                self.send_plain = send_plain  # true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatBannedRights":
        
        flags = Int.read(b)
        
        view_messages = True if flags & (1 << 0) else False
        send_messages = True if flags & (1 << 1) else False
        send_media = True if flags & (1 << 2) else False
        send_stickers = True if flags & (1 << 3) else False
        send_gifs = True if flags & (1 << 4) else False
        send_games = True if flags & (1 << 5) else False
        send_inline = True if flags & (1 << 6) else False
        embed_links = True if flags & (1 << 7) else False
        send_polls = True if flags & (1 << 8) else False
        change_info = True if flags & (1 << 10) else False
        invite_users = True if flags & (1 << 15) else False
        pin_messages = True if flags & (1 << 17) else False
        manage_topics = True if flags & (1 << 18) else False
        send_photos = True if flags & (1 << 19) else False
        send_videos = True if flags & (1 << 20) else False
        send_roundvideos = True if flags & (1 << 21) else False
        send_audios = True if flags & (1 << 22) else False
        send_voices = True if flags & (1 << 23) else False
        send_docs = True if flags & (1 << 24) else False
        send_plain = True if flags & (1 << 25) else False
        until_date = Int.read(b)
        
        return ChatBannedRights(until_date=until_date, view_messages=view_messages, send_messages=send_messages, send_media=send_media, send_stickers=send_stickers, send_gifs=send_gifs, send_games=send_games, send_inline=send_inline, embed_links=embed_links, send_polls=send_polls, change_info=change_info, invite_users=invite_users, pin_messages=pin_messages, manage_topics=manage_topics, send_photos=send_photos, send_videos=send_videos, send_roundvideos=send_roundvideos, send_audios=send_audios, send_voices=send_voices, send_docs=send_docs, send_plain=send_plain)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()