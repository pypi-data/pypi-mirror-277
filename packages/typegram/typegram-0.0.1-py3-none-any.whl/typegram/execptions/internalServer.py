
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


class InternalServer(BaseError):
    """
    InternalServer Error
    """
    CODE = 500
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiCallError(InternalServer):
    """API call error due to Telegram having internal problems. Please try again later"""
    ID = "API_CALL_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthRestart(InternalServer):
    """User authorization has restarted"""
    ID = "AUTH_RESTART"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallOccupyFailed(InternalServer):
    """The call failed because the user is already making another call"""
    ID = "CALL_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatIdGenerateFailed(InternalServer):
    """Failure while generating the chat ID due to Telegram having internal problems. Please try again later"""
    ID = "CHAT_ID_GENERATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatOccupyLocFailed(InternalServer):
    """An internal error occurred while creating the chat"""
    ID = "CHAT_OCCUPY_LOC_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatOccupyUsernameFailed(InternalServer):
    """Failure to occupy chat username due to Telegram having internal problems. Please try again later"""
    ID = "CHAT_OCCUPY_USERNAME_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChpCallFail(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "CHP_CALL_FAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionOccupyAdminFailed(InternalServer):
    """Failed occupying memory for admin info due to Telegram having internal problems. Please try again later"""
    ID = "ENCRYPTION_OCCUPY_ADMIN_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionOccupyFailed(InternalServer):
    """Internal server error while accepting secret chat"""
    ID = "ENCRYPTION_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FolderDeacAutofixAll(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "FOLDER_DEAC_AUTOFIX_ALL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupcallAddParticipantsFailed(InternalServer):
    """Failure while adding voice chat member due to Telegram having internal problems. Please try again later"""
    ID = "GROUPCALL_ADD_PARTICIPANTS_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupedIdOccupyFailed(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "GROUPED_ID_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class HistoryGetFailed(InternalServer):
    """The chat history couldn't be retrieved due to Telegram having internal problems. Please try again later"""
    ID = "HISTORY_GET_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImageEngineDown(InternalServer):
    """Image engine down due to Telegram having internal problems. Please try again later"""
    ID = "IMAGE_ENGINE_DOWN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InterdcXCallError(InternalServer):
    """An error occurred while Telegram was intercommunicating with DC{value}. Please try again later"""
    ID = "INTERDC_X_CALL_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InterdcXCallRichError(InternalServer):
    """A rich error occurred while Telegram was intercommunicating with DC{value}. Please try again later"""
    ID = "INTERDC_X_CALL_RICH_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MemberFetchFailed(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "MEMBER_FETCH_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MemberNoLocation(InternalServer):
    """Couldn't find the member's location due to Telegram having internal problems. Please try again later"""
    ID = "MEMBER_NO_LOCATION"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MemberOccupyPrimaryLocFailed(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "MEMBER_OCCUPY_PRIMARY_LOC_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MemberOccupyUsernameFailed(InternalServer):
    """Failure to occupy member username due to Telegram having internal problems. Please try again later"""
    ID = "MEMBER_OCCUPY_USERNAME_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MsgidDecreaseRetry(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "MSGID_DECREASE_RETRY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MsgRangeUnsync(InternalServer):
    """Message range unsynchronized due to Telegram having internal problems. Please try again later"""
    ID = "MSG_RANGE_UNSYNC"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MtSendQueueTooLong(InternalServer):
    """The MTProto send queue has grown too much due to Telegram having internal problems. Please try again later"""
    ID = "MT_SEND_QUEUE_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NeedChatInvalid(InternalServer):
    """The provided chat is invalid"""
    ID = "NEED_CHAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NeedMemberInvalid(InternalServer):
    """The provided member is invalid or does not exist"""
    ID = "NEED_MEMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NoWorkersRunning(InternalServer):
    """The Telegram server is restarting its workers. Try again later."""
    ID = "NO_WORKERS_RUNNING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ParticipantCallFailed(InternalServer):
    """Failure while making call due to Telegram having internal problems. Please try again later"""
    ID = "PARTICIPANT_CALL_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PersistentTimestampOutdated(InternalServer):
    """The persistent timestamp is outdated due to Telegram having internal problems. Please try again later"""
    ID = "PERSISTENT_TIMESTAMP_OUTDATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoCreateFailed(InternalServer):
    """The creation of the photo failed due to Telegram having internal problems. Please try again later"""
    ID = "PHOTO_CREATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PostponedTimeout(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "POSTPONED_TIMEOUT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PtsChangeEmpty(InternalServer):
    """No PTS change"""
    ID = "PTS_CHANGE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RandomIdDuplicate(InternalServer):
    """You provided a random ID that was already used"""
    ID = "RANDOM_ID_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RegIdGenerateFailed(InternalServer):
    """The registration id failed to generate due to Telegram having internal problems. Please try again later"""
    ID = "REG_ID_GENERATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RpcCallFail(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "RPC_CALL_FAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RpcConnectFailed(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "RPC_CONNECT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RpcMcgetFail(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "RPC_MCGET_FAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SignInFailed(InternalServer):
    """Failure while signing in due to Telegram having internal problems. Please try again later"""
    ID = "SIGN_IN_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StorageCheckFailed(InternalServer):
    """Server storage check failed due to Telegram having internal problems. Please try again later"""
    ID = "STORAGE_CHECK_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StoreInvalidScalarType(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "STORE_INVALID_SCALAR_TYPE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UnknownMethod(InternalServer):
    """The method you tried to call cannot be called on non-CDN DCs"""
    ID = "UNKNOWN_METHOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UploadNoVolume(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "UPLOAD_NO_VOLUME"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VolumeLocNotFound(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "VOLUME_LOC_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WorkerBusyTooLongRetry(InternalServer):
    """Server workers are too busy right now due to Telegram having internal problems. Please try again later"""
    ID = "WORKER_BUSY_TOO_LONG_RETRY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WpIdGenerateFailed(InternalServer):
    """Telegram is having internal problems. Please try again later"""
    ID = "WP_ID_GENERATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


