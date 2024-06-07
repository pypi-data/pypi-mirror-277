
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


class TooMuchRequests(BaseError):
    """
    TooMuchRequests Error
    """
    CODE = 420
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class F2aConfirmWaitX(TooMuchRequests):
    """A wait of {value} seconds is required because this account is active and protected by a F2A password"""
    ID = "F2A_CONFIRM_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodTestPhoneWaitX(TooMuchRequests):
    """A wait of {value} seconds is required in the test servers"""
    ID = "FLOOD_TEST_PHONE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FloodWaitX(TooMuchRequests):
    """A wait of {value} seconds is required"""
    ID = "FLOOD_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SlowmodeWaitX(TooMuchRequests):
    """A wait of {value} seconds is required to send messages in this chat."""
    ID = "SLOWMODE_WAIT_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInitDelayX(TooMuchRequests):
    """You have to confirm the data export request using one of your mobile devices or wait {value} seconds"""
    ID = "TAKEOUT_INIT_DELAY_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


