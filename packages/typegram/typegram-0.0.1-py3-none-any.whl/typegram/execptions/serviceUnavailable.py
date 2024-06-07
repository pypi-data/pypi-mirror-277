
# ===========================================================
#             Copyright (C) 2023-present AyiinXd
# ===========================================================
# ||                                                       ||
# ||              _         _ _      __  __   _            ||
# ||             /   _   _(_|_)_ __  / /__| |           ||
# ||            / _ | | | | | | '_     _  | |           ||
# ||           / ___  |_| | | | | | |/   (_| |           ||
# ||          /_/   ___, |_|_|_| |_/_/___,_|           ||
# ||                  |___/                                ||
# ||                                                       ||
# ===========================================================
#  Appreciating the work of others is not detrimental to you
# ===========================================================
# 


from .base import BaseError


class ServiceUnavailable(BaseError):
    """
    ServiceUnavailable Error
    """
    CODE = 503
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiCallError(ServiceUnavailable):
    """Telegram is having internal problems. Please try again later."""
    ID = "API_CALL_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class Timeout(ServiceUnavailable):
    """Telegram is having internal problems. Please try again later."""
    ID = "Timeout"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


