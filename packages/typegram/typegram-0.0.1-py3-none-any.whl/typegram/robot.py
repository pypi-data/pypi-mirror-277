# ? ===========================================================
# ? Copyright (C) 2023-present AyiinXd
# ? ===========================================================
# ? ||                                                       ||
# ? ||              _         _ _      __  __   _            ||
# ? ||             / \  _   _(_|_)_ __ \ \/ /__| |           ||
# ? ||            / _ \| | | | | | '_ \ \   _  | |           ||
# ? ||           / ___ \ |_| | | | | | |/  \ (_| |           ||
# ? ||          /_/   \_\__, |_|_|_| |_/_/\_\__,_|           ||
# ? ||                  |___/                                ||
# ? ||                                                       ||
# ? ===========================================================
# ? Appreciating the work of others is not detrimental to you
# ? ===========================================================


from typing import List, Optional, Union


from .api.types import User


class Robot():
    def __init__(
        self,
        apiId: int,
        apiHash: str,
        *,
        botToken: Optional[str] = None,
        deviceModel: Optional[str] = None,
        systemVersion: Optional[str] = None,
        appVersion: Optional[str] = None,
        langCode: Optional[str] = None,
        proxy: Union[tuple, dict] = None,
        systemLangCode: Optional[str] = None
    ):
        super().__init__()
        self.apiId = apiId
        self.apiHash = apiHash
        self.botToken = botToken
        self.deviceModel = deviceModel
        self.systemVersion = systemVersion
        self.appVersion = appVersion
        self.langCode = langCode
        self.proxy = proxy
        self.systemLangCode = systemLangCode

        self.me: Optional[User] = None
