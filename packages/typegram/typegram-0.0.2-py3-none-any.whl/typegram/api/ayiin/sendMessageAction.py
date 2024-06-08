
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


SendMessageAction = Union[api.types.SendMessageUploadVideoAction, api.types.SendMessageUploadAudioAction, api.types.SendMessageUploadPhotoAction, api.types.SendMessageUploadDocumentAction, api.types.SendMessageUploadRoundAction, api.types.SendMessageHistoryImportAction, api.types.SendMessageEmojiInteraction, api.types.SendMessageEmojiInteractionSeen]


class SendMessageAction(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 8 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            sendMessageUploadVideoAction
            sendMessageUploadAudioAction
            sendMessageUploadPhotoAction
            sendMessageUploadDocumentAction
            sendMessageUploadRoundAction
            sendMessageHistoryImportAction
            sendMessageEmojiInteraction
            sendMessageEmojiInteractionSeen
    """

    QUALNAME = "typegram.api.ayiin.SendMessageAction.SendMessageAction"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/SendMessageAction")