
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


PageBlock = Union[api.types.PageBlockTitle, api.types.PageBlockSubtitle, api.types.PageBlockAuthorDate, api.types.PageBlockHeader, api.types.PageBlockSubheader, api.types.PageBlockParagraph, api.types.PageBlockPreformatted, api.types.PageBlockFooter, api.types.PageBlockAnchor, api.types.PageBlockList, api.types.PageBlockBlockquote, api.types.PageBlockPullquote, api.types.PageBlockPhoto, api.types.PageBlockVideo, api.types.PageBlockCover, api.types.PageBlockEmbed, api.types.PageBlockEmbedPost, api.types.PageBlockCollage, api.types.PageBlockSlideshow, api.types.PageBlockChannel, api.types.PageBlockAudio, api.types.PageBlockKicker, api.types.PageBlockTable, api.types.PageBlockOrderedList, api.types.PageBlockDetails, api.types.PageBlockRelatedArticles, api.types.PageBlockMap]


class PageBlock(Object):
    """
    Telegram API base type.

    Constructors:
        This base type has 27 constructors available.

        .. currentmodule:: typegram.api.types

        .. autosummary::
            :nosignatures:

            pageBlockTitle
            pageBlockSubtitle
            pageBlockAuthorDate
            pageBlockHeader
            pageBlockSubheader
            pageBlockParagraph
            pageBlockPreformatted
            pageBlockFooter
            pageBlockAnchor
            pageBlockList
            pageBlockBlockquote
            pageBlockPullquote
            pageBlockPhoto
            pageBlockVideo
            pageBlockCover
            pageBlockEmbed
            pageBlockEmbedPost
            pageBlockCollage
            pageBlockSlideshow
            pageBlockChannel
            pageBlockAudio
            pageBlockKicker
            pageBlockTable
            pageBlockOrderedList
            pageBlockDetails
            pageBlockRelatedArticles
            pageBlockMap
    """

    QUALNAME = "typegram.api.ayiin.PageBlock.PageBlock"

    def __init__(self):
        raise TypeError("Base ayiin can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/PageBlock")