# -*- coding: utf-8 -*-
"""
Provides functions for converting Meetup.com API response data into the types
returned by the PythonKC meetup client.

"""


from dateutil.tz import tzoffset
from dateutil.tz import tzutc
from pythonkc_meetups.types import MeetupEvent
from pythonkc_meetups.types import MeetupMember
from pythonkc_meetups.types import MeetupPhoto
from pythonkc_meetups.types import MeetupVenue
import datetime


def parse_event(data, attendees=None, photos=None):
    """
    Parse a ``MeetupEvent`` from the given response data.

    Returns
    -------
    A ``pythonkc_meetups.types.MeetupEvent``.

    """
    return MeetupEvent(
        id=data.get('id', None),
        name=data.get('name', None),
        description=data.get('description', None),
        time=parse_datetime(data.get('time', None),
                            data.get('utc_offset', None)),
        status=data.get('status', None),
        yes_rsvp_count=data.get('yes_rsvp_count', None),
        maybe_rsvp_count=data.get('maybe_rsvp_count', None),
        event_url=data.get('event_url', None),
        photo_url=data.get('photo_url', None),
        venue=parse_venue(data['venue']) if 'venue' in data else None,
        attendees=attendees,
        photos=photos
    )


def parse_venue(data):
    """
    Parse a ``MeetupVenue`` from the given response data.

    Returns
    -------
    A `pythonkc_meetups.types.`MeetupVenue``.

    """
    return MeetupVenue(
        id=data.get('id', None),
        name=data.get('name', None),
        address_1=data.get('address_1', None),
        address_2=data.get('address_2', None),
        address_3=data.get('address_3', None),
        city=data.get('city', None),
        state=data.get('state', None),
        zip=data.get('zip', None),
        country=data.get('country', None),
        lat=data.get('lat', None),
        lon=data.get('lon', None)
    )


def parse_member_from_rsvp(data):
    """
    Parse a ``MeetupMember`` from the given RSVP response data.

    Returns
    -------
    A ``pythonkc_meetups.types.MeetupMember``.

    """
    return MeetupMember(
        id=data['member'].get('member_id', None),
        name=data['member'].get('name', None),
        photo=(parse_photo(data['member_photo'])
               if 'member_photo' in data else None)
    )


def parse_photo(data):
    """
    Parse a ``MeetupPhoto`` from the given response data.

    Returns
    -------
    A `pythonkc_meetups.types.`MeetupPhoto``.

    """
    return MeetupPhoto(
        id=data.get('photo_id', data.get('id', None)),
        url=data.get('photo_link', None),
        highres_url=data.get('highres_link', None),
        thumb_url=data.get('thumb_link', None)
    )


def parse_datetime(utc_timestamp_ms, utc_offset_ms):
    """
    Create a timezone-aware ``datetime.datetime`` from the given UTC timestamp
    (in milliseconds), if provided. If an offest it given, it is applied to the
    datetime returned.

    Parameters
    ----------
    utc_timestamp_ms
        UTC timestamp in milliseconds.
    utc_offset_ms
        Offset from UTC, in milliseconds, to apply to the time.

    Returns
    -------
    A ``datetime.datetime`` if a timestamp is given, otherwise ``None``.

    """
    if utc_timestamp_ms:
        utc_timestamp_s = utc_timestamp_ms / 1000
        dt = datetime.datetime.fromtimestamp(utc_timestamp_s, tzutc())

        if utc_offset_ms:
            utc_offset_s = utc_offset_ms / 1000
            tz_offset = tzoffset(None, utc_offset_s)
            dt = dt.astimezone(tz_offset)

        return dt
