
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

from typing import Union, List, Optional

from typegram import api
from typegram.api.object import Object


GiveawayInfo = Union[api.types.payments.PaymentForm, api.types.payments.ValidatedRequestedInfo, api.types.payments.PaymentResult, api.types.payments.PaymentReceipt, api.types.payments.SavedInfo, api.types.payments.BankCardData, api.types.payments.ExportedInvoice, api.types.payments.CheckedGiftCode, api.types.payments.GiveawayInfo, api.types.payments.StarsStatus]


class GiveawayInfo(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            payments.PaymentForm
            payments.ValidatedRequestedInfo
            payments.PaymentResult
            payments.PaymentReceipt
            payments.SavedInfo
            payments.BankCardData
            payments.ExportedInvoice
            payments.CheckedGiftCode
            payments.GiveawayInfo
            payments.StarsStatus
    """

    QUALNAME = "typegram.api.ayiin.giveawayInfo.GiveawayInfo"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/giveawayInfo")