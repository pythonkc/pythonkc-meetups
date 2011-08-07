# -*- coding: utf-8 -*-
"""
Overview
========
Defines exceptions raised by meetupy.

"""


class PythonKCMeetupsException(Exception):
    """
    Indicates a general problem interacting with the Meetup.com API.

    This is meant to be the base type for exceptions that meetupy raises and
    shouldn't itself be raised.

    """
    pass


class PythonKCMeetupsBadResponse(PythonKCMeetupsException):
    """
    Indicates that there was a problem with a response returned by the
    Meetup.com API.

    This may include client-error status codes (i.e., 4XX), but those are not
    expected as this client was coded to the HTTP spec and Meetup.com's API.

    """
    pass


class PythonKCMeetupsNotJson(PythonKCMeetupsBadResponse):
    """
    Indicates that a media type other than JSON was returned where JSON was
    expected. Either ``application/json`` or ``text/javascript`` is expected in
    the ``Content-Type`` header of API HTTP responses.

    """
    pass


class PythonKCMeetupsBadJson(PythonKCMeetupsBadResponse):
    """
    Indicates that the data returned from the server could not be parsed as
    JSON, despite the content type indicating a JSON response.

    """
    pass


class PythonKCMeetupsMeetupDown(PythonKCMeetupsException):
    """
    Indicates that a server error status code (i.e, 5XX) was returned from the
    Meetup.com API.

    """
    pass


class PythonKCMeetupsRateLimitExceeded(PythonKCMeetupsException):
    """
    Indicates that the rate limit has been exceed for the current API key or
    OAuth token.

    """
    pass
