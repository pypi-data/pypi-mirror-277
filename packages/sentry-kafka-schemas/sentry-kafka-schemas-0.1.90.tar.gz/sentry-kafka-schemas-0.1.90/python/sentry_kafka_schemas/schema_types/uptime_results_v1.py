from typing import Literal, TypedDict, Union, Required


class UptimeResult(TypedDict, total=False):
    """
    uptime_result.

    A message containing the result of the uptime check.
    """

    guid: Required[str]
    """
    Unique identifier of the uptime check

    Required property
    """

    monitor_id: Required[int]
    """
    The identifier of the uptime monitor

    minimum: 0
    maximum: 18446744073709551615

    Required property
    """

    monitor_environment_id: Required[int]
    """
    The identifier of the uptime monitors environment

    minimum: 0
    maximum: 18446744073709551615

    Required property
    """

    status: Required["_UptimeResultStatus"]
    """
    The status of the check

    Required property
    """

    status_reason: Required[Union["_UptimeResultStatusReasonObject", None]]
    """
    Reason for the status, primairly used for failure

    Required property
    """

    trace_id: Required[str]
    """
    Trace ID associated with the check-in made

    Required property
    """

    scheduled_check_time: Required[Union[int, float]]
    """
    Timestamp in milliseconds of when the check was schedule to run

    Required property
    """

    actual_check_time: Required[Union[int, float]]
    """
    Timestamp in milliseconds of when the check was actually ran

    Required property
    """

    duration_ms: Required[Union[Union[int, float], None]]
    """
    Duration of the check in ms. Will be null when the status is missed_window

    Required property
    """

    request_info: Required["_UptimeResultRequestInfo"]
    """
    Duration of the check in ms. Will be null when the status is missed_window

    Required property
    """



class _UptimeResultRequestInfo(TypedDict, total=False):
    """ Duration of the check in ms. Will be null when the status is missed_window """

    request_type: "_UptimeResultRequestInfoRequestType"
    """ The type of HTTP method used for the check """

    http_status_code: Union[int, float]
    """ Status code of the successful check-in """



_UptimeResultRequestInfoRequestType = Union[Literal['HEAD'], Literal['GET']]
""" The type of HTTP method used for the check """
_UPTIMERESULTREQUESTINFOREQUESTTYPE_HEAD: Literal['HEAD'] = "HEAD"
"""The values for the 'The type of HTTP method used for the check' enum"""
_UPTIMERESULTREQUESTINFOREQUESTTYPE_GET: Literal['GET'] = "GET"
"""The values for the 'The type of HTTP method used for the check' enum"""



_UptimeResultStatus = Union[Literal['success'], Literal['failure'], Literal['missed_window']]
""" The status of the check """
_UPTIMERESULTSTATUS_SUCCESS: Literal['success'] = "success"
"""The values for the 'The status of the check' enum"""
_UPTIMERESULTSTATUS_FAILURE: Literal['failure'] = "failure"
"""The values for the 'The status of the check' enum"""
_UPTIMERESULTSTATUS_MISSED_WINDOW: Literal['missed_window'] = "missed_window"
"""The values for the 'The status of the check' enum"""



class _UptimeResultStatusReasonObject(TypedDict, total=False):
    """ Reason for the status, primairly used for failure """

    type: "_UptimeResultStatusReasonObjectType"
    """ The type of the status reason """

    description: str
    """ A human readable description of the status reason """



_UptimeResultStatusReasonObjectType = Union[Literal['timeout'], Literal['dns_error'], Literal['failure']]
""" The type of the status reason """
_UPTIMERESULTSTATUSREASONOBJECTTYPE_TIMEOUT: Literal['timeout'] = "timeout"
"""The values for the 'The type of the status reason' enum"""
_UPTIMERESULTSTATUSREASONOBJECTTYPE_DNS_ERROR: Literal['dns_error'] = "dns_error"
"""The values for the 'The type of the status reason' enum"""
_UPTIMERESULTSTATUSREASONOBJECTTYPE_FAILURE: Literal['failure'] = "failure"
"""The values for the 'The type of the status reason' enum"""

