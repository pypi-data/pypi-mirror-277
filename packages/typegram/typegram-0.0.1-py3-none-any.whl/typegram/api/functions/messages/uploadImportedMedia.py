
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



class UploadImportedMedia(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``2A862092``

peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`):
                    N/A
                
        import_id (``int`` ``64-bit``):
                    N/A
                
        file_name (``str``):
                    N/A
                
        media (:obj:`InputMedia<typegram.api.ayiin.InputMedia>`):
                    N/A
                
    Returns:
        :obj:`MessageMedia<typegram.api.ayiin.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "import_id", "file_name", "media"]

    ID = 0x2a862092
    QUALNAME = "functions.functions.MessageMedia"

    def __init__(self, *, peer: "ayiin.InputPeer", import_id: int, file_name: str, media: "ayiin.InputMedia") -> None:
        
                self.peer = peer  # InputPeer
        
                self.import_id = import_id  # long
        
                self.file_name = file_name  # string
        
                self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadImportedMedia":
        # No flags
        
        peer = Object.read(b)
        
        import_id = Long.read(b)
        
        file_name = String.read(b)
        
        media = Object.read(b)
        
        return UploadImportedMedia(peer=peer, import_id=import_id, file_name=file_name, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        b.write(String(self.file_name))
        
        b.write(self.media.write())
        
        return b.getvalue()