
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



class TermsOfService(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.help.TermsOfService`.

    Details:
        - Layer: ``181``
        - ID: ``780A0310``

id (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`):
                    N/A
                
        text (``str``):
                    N/A
                
        entities (List of :obj:`MessageEntity<typegram.api.ayiin.MessageEntity>`):
                    N/A
                
        popup (``bool``, *optional*):
                    N/A
                
        min_age_confirm (``int`` ``32-bit``, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 19 functions.

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

    __slots__: List[str] = ["id", "text", "entities", "popup", "min_age_confirm"]

    ID = 0x780a0310
    QUALNAME = "functions.typeshelp.TermsOfService"

    def __init__(self, *, id: "ayiin.DataJSON", text: str, entities: List["ayiin.MessageEntity"], popup: Optional[bool] = None, min_age_confirm: Optional[int] = None) -> None:
        
                self.id = id  # DataJSON
        
                self.text = text  # string
        
                self.entities = entities  # MessageEntity
        
                self.popup = popup  # true
        
                self.min_age_confirm = min_age_confirm  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfService":
        
        flags = Int.read(b)
        
        popup = True if flags & (1 << 0) else False
        id = Object.read(b)
        
        text = String.read(b)
        
        entities = Object.read(b)
        
        min_age_confirm = Int.read(b) if flags & (1 << 1) else None
        return TermsOfService(id=id, text=text, entities=entities, popup=popup, min_age_confirm=min_age_confirm)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        if self.min_age_confirm is not None:
            b.write(Int(self.min_age_confirm))
        
        return b.getvalue()