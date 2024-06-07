
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



class TranslateText(Object):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``181``
        - ID: ``63183030``

to_lang (``str``):
                    N/A
                
        peer (:obj:`InputPeer<typegram.api.ayiin.InputPeer>`, *optional*):
                    N/A
                
        id (List of ``int`` ``32-bit``, *optional*):
                    N/A
                
        text (List of :obj:`TextWithEntities<typegram.api.ayiin.TextWithEntities>`, *optional*):
                    N/A
                
    Returns:
        :obj:`messages.TranslatedText<typegram.api.ayiin.messages.TranslatedText>`
    """

    __slots__: List[str] = ["to_lang", "peer", "id", "text"]

    ID = 0x63183030
    QUALNAME = "functions.functionsmessages.TranslatedText"

    def __init__(self, *, to_lang: str, peer: "ayiin.InputPeer" = None, id: Optional[List[int]] = None, text: Optional[List["ayiin.TextWithEntities"]] = None) -> None:
        
                self.to_lang = to_lang  # string
        
                self.peer = peer  # InputPeer
        
                self.id = id  # int
        
                self.text = text  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateText":
        
        flags = Int.read(b)
        
        peer = Object.read(b) if flags & (1 << 0) else None
        
        id = Object.read(b, Int) if flags & (1 << 0) else []
        
        text = Object.read(b) if flags & (1 << 1) else []
        
        to_lang = String.read(b)
        
        return TranslateText(to_lang=to_lang, peer=peer, id=id, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.id is not None:
            b.write(Vector(self.id, Int))
        
        if self.text is not None:
            b.write(Vector(self.text))
        
        b.write(String(self.to_lang))
        
        return b.getvalue()