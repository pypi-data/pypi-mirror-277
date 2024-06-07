
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



class PremiumPromo(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.PremiumPromo`.

    Details:
        - Layer: ``181``
        - ID: ``5334759C``

status_text (``str``):
                    N/A
                
        status_entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
        video_sections (List of ``str``):
                    N/A
                
        videos (List of :obj:`Document<typegram.api.ayiin.Document>`):
                    N/A
                
        period_options (List of :obj:`PremiumSubscriptionOption<typegram.api.ayiin.PremiumSubscriptionOption>`):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
    Functions:
        This object can be returned by 17 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            help.AppUpdate
            help.RecentMeUrls
            help.DeepLinkInfo
            help.AppConfig
            help.PassportConfig
            help.UserInfo
            help.CountriesList
            help.PeerColors
            help.TimezonesList
    """

    __slots__: List[str] = ["status_text", "status_entities", "video_sections", "videos", "period_options", "users"]

    ID = 0x5334759c
    QUALNAME = "functions.typeshelp.PremiumPromo"

    def __init__(self, *, status_text: str, status_entities: List["ayiin.MessageEntity"], video_sections: List[str], videos: List["ayiin.Document"], period_options: List["ayiin.PremiumSubscriptionOption"], users: List["ayiin.User"]) -> None:
        
                self.status_text = status_text  # string
        
                self.status_entities = status_entities  # MessageEntity
        
                self.video_sections = video_sections  # string
        
                self.videos = videos  # Document
        
                self.period_options = period_options  # PremiumSubscriptionOption
        
                self.users = users  # User

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumPromo":
        # No flags
        
        status_text = String.read(b)
        
        status_entities = Object.read(b)
        
        video_sections = Object.read(b, String)
        
        videos = Object.read(b)
        
        period_options = Object.read(b)
        
        users = Object.read(b)
        
        return PremiumPromo(status_text=status_text, status_entities=status_entities, video_sections=video_sections, videos=videos, period_options=period_options, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.status_text))
        
        b.write(Vector(self.status_entities))
        
        b.write(Vector(self.video_sections, String))
        
        b.write(Vector(self.videos))
        
        b.write(Vector(self.period_options))
        
        b.write(Vector(self.users))
        
        return b.getvalue()