# -*- coding: utf-8 -*-
"""
Provides the PythonKC Meetup.com API client implementation.

"""


from pythonkc_meetups.exceptions import PythonKCMeetupsBadJson
from pythonkc_meetups.exceptions import PythonKCMeetupsBadResponse
from pythonkc_meetups.exceptions import PythonKCMeetupsMeetupDown
from pythonkc_meetups.exceptions import PythonKCMeetupsNotJson
from pythonkc_meetups.exceptions import PythonKCMeetupsRateLimitExceeded
from pythonkc_meetups.parsers import parse_event
from pythonkc_meetups.parsers import parse_member_from_rsvp
import httplib2
import json
import mimeparse
import urllib


MEETUP_API_HOST = 'https://api.meetup.com'
EVENTS_URL = MEETUP_API_HOST + '/2/events.json'
RSVPS_URL = MEETUP_API_HOST + '/2/rsvps.json'
GROUP_URLNAME = 'pythonkc'


class PythonKCMeetups(object):

    """
    Retrieves information about PythonKC meetups.

    """

    def __init__(self, api_key, http_timeout=1, http_retries=2):
        """
        Create a new instance.

        Parameters
        ----------
        api_key
            The Meetup.com API consumer key to make requests with.
        http_timeout
            Time, in seconds, to give HTTP requests to complete.
        http_retries
            The number of times to retry requests when it is appropriate to do
            so.

        """
        self._api_key = api_key
        self._http_timeout = http_timeout
        self._http_retries = http_retries

    def get_upcoming_events(self):
        """
        Get upcoming PythonKC meetup events.

        Returns
        -------
        List of ``pythonkc_meetups.types.MeetupEvent``, ordered by event time,
        ascending.

        Exceptions
        ----------
        * PythonKCMeetupsBadJson
        * PythonKCMeetupsBadResponse
        * PythonKCMeetupsMeetupDown
        * PythonKCMeetupsNotJson
        * PythonKCMeetupsRateLimitExceeded

        """

        query = urllib.urlencode({'key': self._api_key,
                                  'group_urlname': GROUP_URLNAME})
        url = '{0}?{1}'.format(EVENTS_URL, query)
        data = self._http_get_json(url)
        events = data['results']
        return [parse_event(event) for event in events]

    def get_past_events(self):
        """
        Get past PythonKC meetup events.

        Returns
        -------
        List of ``pythonkc_meetups.types.MeetupEvent``, ordered by event time,
        descending.

        Exceptions
        ----------
        * PythonKCMeetupsBadJson
        * PythonKCMeetupsBadResponse
        * PythonKCMeetupsMeetupDown
        * PythonKCMeetupsNotJson
        * PythonKCMeetupsRateLimitExceeded

        """

        def get_attendees(event):
            return (self.get_event_attendees(event['id']) 
                    if 'id' in event else None)

        query = urllib.urlencode({'key': self._api_key,
                                  'group_urlname': GROUP_URLNAME,
                                  'status': 'past',
                                  'desc': 'true'})
        url = '{0}?{1}'.format(EVENTS_URL, query)
        data = self._http_get_json(url)
        events = data['results']
        return [parse_event(event, get_attendees(event)) for event in events]

    def get_event_attendees(self, event_id):
        """
        Get the attendees of the identified event.

        Parameters
        ----------
        event_id
            ID of the event to get attendees for.

        Returns
        -------
        List of ``pythonkc_meetups.types.MeetupMember``.

        Exceptions
        ----------
        * PythonKCMeetupsBadJson
        * PythonKCMeetupsBadResponse
        * PythonKCMeetupsMeetupDown
        * PythonKCMeetupsNotJson
        * PythonKCMeetupsRateLimitExceeded

        """
        query = urllib.urlencode({'key': self._api_key,
                                  'event_id': event_id})
        url = '{0}?{1}'.format(RSVPS_URL, query)
        data = self._http_get_json(url)
        rsvps = data['results']
        return [parse_member_from_rsvp(rsvp) for rsvp in rsvps]

    def _http_get_json(self, url):
        """
        Make an HTTP GET request to the specified URL, check that it returned a
        JSON response, and returned the data parsed from that response.

        Parameters
        ----------
        url
            The URL to GET.

        Returns
        -------
        Dictionary of data parsed from a JSON HTTP response.

        Exceptions
        ----------
        * PythonKCMeetupsBadJson
        * PythonKCMeetupsBadResponse
        * PythonKCMeetupsMeetupDown
        * PythonKCMeetupsNotJson
        * PythonKCMeetupsRateLimitExceeded

        """
        response, content = self._http_get(url)

        content_type = response['content-type']
        parsed_mimetype = mimeparse.parse_mime_type(content_type)
        if parsed_mimetype[1] not in ('json', 'javascript'):
            raise PythonKCMeetupsNotJson(content_type)

        try:
            return json.loads(content)
        except ValueError as e:
            raise PythonKCMeetupsBadJson(e)

    def _http_get(self, url):
        """
        Make an HTTP GET request to the specified URL and return the response.

        Retries
        -------
        The constructor of this class takes an argument specifying the number
        of times to retry a GET. The statuses which are retried on are: 408,
        500, 502, 503, and 504.

        Returns
        -------
        A tuple of response, content, where response is a dictionary of
        response metadata (headers), and content is the entity body returned.

        Exceptions
        ----------
        * PythonKCMeetupsBadResponse
        * PythonKCMeetupsMeetupDown
        * PythonKCMeetupsRateLimitExceeded

        """
        for try_number in range(self._http_retries + 1):
            client = httplib2.Http(timeout=self._http_timeout)
            response, content = client.request(url, 'GET')
            if response.status == 200:
                return response, content

            if (try_number >= self._http_retries or
                response.status not in (408, 500, 502, 503, 504)):

                if response.status >= 500:
                    raise PythonKCMeetupsMeetupDown(response, content)
                if response.status == 400:
                    try:
                        data = json.loads(content)
                        if data.get('code', None) == 'limit':
                            raise PythonKCMeetupsRateLimitExceeded
                    except:  # Don't lose original error when JSON is bad
                        pass
                raise PythonKCMeetupsBadResponse(response, content)
