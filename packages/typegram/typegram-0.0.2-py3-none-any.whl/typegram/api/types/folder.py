
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

from typegram import api
from typegram.api.object import Object
from typegram.api.utils import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector



class Folder(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Folder`.

    Details:
        - Layer: ``181``
        - ID: ``FF544E65``

id (``int`` ``32-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        autofill_new_broadcasts (``bool``, *optional*):
                    N/A
                
        autofill_public_groups (``bool``, *optional*):
                    N/A
                
        autofill_new_correspondents (``bool``, *optional*):
                    N/A
                
        photo (:obj:`ChatPhoto<typegram.api.ayiin.ChatPhoto>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups", "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: Optional[bool] = None, autofill_public_groups: Optional[bool] = None, autofill_new_correspondents: Optional[bool] = None, photo: "api.ayiin.ChatPhoto" = None) -> None:
        
                self.id = id  # int
        
                self.title = title  # string
        
                self.autofill_new_broadcasts = autofill_new_broadcasts  # true
        
                self.autofill_public_groups = autofill_public_groups  # true
        
                self.autofill_new_correspondents = autofill_new_correspondents  # true
        
                self.photo = photo  # ChatPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Folder":
        
        flags = Int.read(b)
        
        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 3) else None
        
        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()