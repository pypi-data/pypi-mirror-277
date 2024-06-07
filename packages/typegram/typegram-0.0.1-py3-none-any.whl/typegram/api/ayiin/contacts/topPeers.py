
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


TopPeers = Union[api.types.contacts.Contacts, api.types.contacts.ImportedContacts, api.types.contacts.Blocked, api.types.contacts.Found, api.types.contacts.ResolvedPeer, api.types.contacts.TopPeers, api.types.contacts.ContactBirthdays]


class TopPeers(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            contacts.Contacts
            contacts.ImportedContacts
            contacts.Blocked
            contacts.Found
            contacts.ResolvedPeer
            contacts.TopPeers
            contacts.ContactBirthdays
    """

    QUALNAME = "typegram.api.ayiin.topPeers.TopPeers"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/topPeers")