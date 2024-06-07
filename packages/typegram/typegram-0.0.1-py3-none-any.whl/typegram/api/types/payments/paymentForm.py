
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



class PaymentForm(Object):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~typegram.api.ayiin.payments.PaymentForm`.

    Details:
        - Layer: ``181``
        - ID: ``A0058751``

form_id (``int`` ``64-bit``):
                    N/A
                
        bot_id (``int`` ``64-bit``):
                    N/A
                
        title (``str``):
                    N/A
                
        description (``str``):
                    N/A
                
        invoice (:obj:`Invoice<typegram.api.ayiin.Invoice>`):
                    N/A
                
        provider_id (``int`` ``64-bit``):
                    N/A
                
        url (``str``):
                    N/A
                
        users (List of :obj:`User<typegram.api.ayiin.User>`):
                    N/A
                
        can_save_credentials (``bool``, *optional*):
                    N/A
                
        password_missing (``bool``, *optional*):
                    N/A
                
        photo (:obj:`WebDocument<typegram.api.ayiin.WebDocument>`, *optional*):
                    N/A
                
        native_provider (``str``, *optional*):
                    N/A
                
        native_params (:obj:`DataJSON<typegram.api.ayiin.DataJSON>`, *optional*):
                    N/A
                
        additional_methods (List of :obj:`PaymentFormMethod<typegram.api.ayiin.PaymentFormMethod>`, *optional*):
                    N/A
                
        saved_info (:obj:`PaymentRequestedInfo<typegram.api.ayiin.PaymentRequestedInfo>`, *optional*):
                    N/A
                
        saved_credentials (List of :obj:`PaymentSavedCredentials<typegram.api.ayiin.PaymentSavedCredentials>`, *optional*):
                    N/A
                
    Functions:
        This object can be returned by 20 functions.

        .. currentmodule:: typegram.api.functions

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.PaymentReceipt
            payments.ValidatedRequestedInfo
            payments.PaymentResult
            payments.BankCardData
            payments.ExportedInvoice
            payments.CheckedGiftCode
            payments.GiveawayInfo
            payments.StarsStatus
    """

    __slots__: List[str] = ["form_id", "bot_id", "title", "description", "invoice", "provider_id", "url", "users", "can_save_credentials", "password_missing", "photo", "native_provider", "native_params", "additional_methods", "saved_info", "saved_credentials"]

    ID = 0xa0058751
    QUALNAME = "functions.typespayments.PaymentForm"

    def __init__(self, *, form_id: int, bot_id: int, title: str, description: str, invoice: "ayiin.Invoice", provider_id: int, url: str, users: List["ayiin.User"], can_save_credentials: Optional[bool] = None, password_missing: Optional[bool] = None, photo: "ayiin.WebDocument" = None, native_provider: Optional[str] = None, native_params: "ayiin.DataJSON" = None, additional_methods: Optional[List["ayiin.PaymentFormMethod"]] = None, saved_info: "ayiin.PaymentRequestedInfo" = None, saved_credentials: Optional[List["ayiin.PaymentSavedCredentials"]] = None) -> None:
        
                self.form_id = form_id  # long
        
                self.bot_id = bot_id  # long
        
                self.title = title  # string
        
                self.description = description  # string
        
                self.invoice = invoice  # Invoice
        
                self.provider_id = provider_id  # long
        
                self.url = url  # string
        
                self.users = users  # User
        
                self.can_save_credentials = can_save_credentials  # true
        
                self.password_missing = password_missing  # true
        
                self.photo = photo  # WebDocument
        
                self.native_provider = native_provider  # string
        
                self.native_params = native_params  # DataJSON
        
                self.additional_methods = additional_methods  # PaymentFormMethod
        
                self.saved_info = saved_info  # PaymentRequestedInfo
        
                self.saved_credentials = saved_credentials  # PaymentSavedCredentials

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentForm":
        
        flags = Int.read(b)
        
        can_save_credentials = True if flags & (1 << 2) else False
        password_missing = True if flags & (1 << 3) else False
        form_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = Object.read(b) if flags & (1 << 5) else None
        
        invoice = Object.read(b)
        
        provider_id = Long.read(b)
        
        url = String.read(b)
        
        native_provider = String.read(b) if flags & (1 << 4) else None
        native_params = Object.read(b) if flags & (1 << 4) else None
        
        additional_methods = Object.read(b) if flags & (1 << 6) else []
        
        saved_info = Object.read(b) if flags & (1 << 0) else None
        
        saved_credentials = Object.read(b) if flags & (1 << 1) else []
        
        users = Object.read(b)
        
        return PaymentForm(form_id=form_id, bot_id=bot_id, title=title, description=description, invoice=invoice, provider_id=provider_id, url=url, users=users, can_save_credentials=can_save_credentials, password_missing=password_missing, photo=photo, native_provider=native_provider, native_params=native_params, additional_methods=additional_methods, saved_info=saved_info, saved_credentials=saved_credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Long(self.provider_id))
        
        b.write(String(self.url))
        
        if self.native_provider is not None:
            b.write(String(self.native_provider))
        
        if self.native_params is not None:
            b.write(self.native_params.write())
        
        if self.additional_methods is not None:
            b.write(Vector(self.additional_methods))
        
        if self.saved_info is not None:
            b.write(self.saved_info.write())
        
        if self.saved_credentials is not None:
            b.write(Vector(self.saved_credentials))
        
        b.write(Vector(self.users))
        
        return b.getvalue()