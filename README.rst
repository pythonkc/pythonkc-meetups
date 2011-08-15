PythonKC Meetup.com API Client
==============================

A clean, minimal client to the Meetup.com API for retrieving Meetup events for
the `PythonKC group <http://www.meetup.com/pythonkc/>`_.

Example Usage
-------------

::

    >>> from pythonkc_meetups import PythonKCMeetups
    >>> meetups = PythonKCMeetups(api_key='<your API key here>')
    >>> next_meetup = meetups.get_upcoming_events()[0]
    >>> next_meetup.name
    u'Hackathon!'
    >>> next_meetup.time
    datetime.datetime(2011, 8, 13, 10, 0, tzinfo=tzoffset(None, -18000))
    >>> next_meetup.venue.name
    u"Salva O'Renick"
    >>> next_meetup.venue.lat, next_meetup.venue.lon
    (39.091053, -94.576996)
    >>> next_meetup.yes_rsvp_count
    9
    >>> next_meetup.event_url
    u'http://www.meetup.com/pythonkc/events/25940081/'
    >>> last_meetup = meetups.get_past_events()[0]
    >>> last_meetup.name
    u'Monthly Meetup: Google App Engine'
    >>> last_meetup.time
    datetime.datetime(2011, 7, 9, 14, 0, tzinfo=tzoffset(None, -18000))
    >>> an_attendee = last_meetup.attendees[0]
    >>> an_attendee.name
    u'Steven Cummings'
    >>> an_attendee.photo.thumb_url
    u'http://photos1.meetupstatic.com/photos/member/2/e/f/5/thumb_16212021.jpeg'
