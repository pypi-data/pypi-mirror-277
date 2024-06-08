
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



class Document(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.Document`.

    Details:
        - Layer: ``181``
        - ID: ``8FD4C4D8``

id (``int`` ``64-bit``):
                    N/A
                
        access_hash (``int`` ``64-bit``):
                    N/A
                
        file_reference (``bytes``):
                    N/A
                
        date (``int`` ``32-bit``):
                    N/A
                
        mime_type (``str``):
                    N/A
                
        size (``int`` ``64-bit``):
                    N/A
                
        dc_id (``int`` ``32-bit``):
                    N/A
                
        attributes (List of :obj:`DocumentAttribute<typegram.api.ayiin.DocumentAttribute>`):
                    N/A
                
        thumbs (List of :obj:`PhotoSize<typegram.api.ayiin.PhotoSize>`, *optional*):
                    N/A
                
        video_thumbs (List of :obj:`VideoSize<typegram.api.ayiin.VideoSize>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 8 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            account.uploadTheme
            account.uploadRingtone
            messages.getDocumentByHash
            messages.getCustomEmojiDocuments
    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "date", "mime_type", "size", "dc_id", "attributes", "thumbs", "video_thumbs"]

    ID = 0x8fd4c4d8
    QUALNAME = "types.document"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int, mime_type: str, size: int, dc_id: int, attributes: List["api.ayiin.DocumentAttribute"], thumbs: Optional[List["api.ayiin.PhotoSize"]] = None, video_thumbs: Optional[List["api.ayiin.VideoSize"]] = None) -> None:
        
                self.id = id  # long
        
                self.access_hash = access_hash  # long
        
                self.file_reference = file_reference  # bytes
        
                self.date = date  # int
        
                self.mime_type = mime_type  # string
        
                self.size = size  # long
        
                self.dc_id = dc_id  # int
        
                self.attributes = attributes  # DocumentAttribute
        
                self.thumbs = thumbs  # PhotoSize
        
                self.video_thumbs = video_thumbs  # VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Document":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        date = Int.read(b)
        
        mime_type = String.read(b)
        
        size = Long.read(b)
        
        thumbs = Object.read(b) if flags & (1 << 0) else []
        
        video_thumbs = Object.read(b) if flags & (1 << 1) else []
        
        dc_id = Int.read(b)
        
        attributes = Object.read(b)
        
        return Document(id=id, access_hash=access_hash, file_reference=file_reference, date=date, mime_type=mime_type, size=size, dc_id=dc_id, attributes=attributes, thumbs=thumbs, video_thumbs=video_thumbs)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(Int(self.date))
        
        b.write(String(self.mime_type))
        
        b.write(Long(self.size))
        
        if self.thumbs is not None:
            b.write(Vector(self.thumbs))
        
        if self.video_thumbs is not None:
            b.write(Vector(self.video_thumbs))
        
        b.write(Int(self.dc_id))
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()