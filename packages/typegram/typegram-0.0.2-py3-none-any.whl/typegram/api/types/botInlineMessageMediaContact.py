
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



class BotInlineMessageMediaContact(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.BotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``18D1CDC2``

phone_number (``str``):
                    N/A
                
        first_name (``str``):
                    N/A
                
        last_name (``str``):
                    N/A
                
        vcard (``str``):
                    N/A
                
        reply_markup (:obj:`ReplyMarkup<typegram.api.ayiin.ReplyMarkup>`, *optional*):
                    N/A
                
    """

    __slots__: List[str] = ["phone_number", "first_name", "last_name", "vcard", "reply_markup"]

    ID = 0x18d1cdc2
    QUALNAME = "types.botInlineMessageMediaContact"

    def __init__(self, *, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: "api.ayiin.ReplyMarkup" = None) -> None:
        
                self.phone_number = phone_number  # string
        
                self.first_name = first_name  # string
        
                self.last_name = last_name  # string
        
                self.vcard = vcard  # string
        
                self.reply_markup = reply_markup  # ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaContact":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        vcard = String.read(b)
        
        reply_markup = Object.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaContact(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.vcard))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()