# -*- coding: utf-8 -*-
"""
Overview
========
Defines the types and structures returned from the PythonKC Meetup.com API
client.

Types
=====

MeetupEvent
-----------
id
    Meetup.com ID for the event.
name
    Name of the event.
description
    Description of the event. May include markup.
time
    Date & time (``datetime.datetime``) that the event starts at.
status
    Status of the event, e.g., ``upcoming``.
venue
    A ``MeetupVenue`` describing the location of the event.
yes_rsvp_count
    The number of "yes" RSVPs.
maybe_rsvp_count
    The number of "maybe" RSVPs.
event_url
    URL of the Meetup event page.
photo_url
    URL of the event photo.
attendees
    List of ``MeetupMember`` that attended this event if it was in the past.
photos
    List of ``MeetupPhoto`` from the event if it was in the past.

MeetupVenue
-----------
id
    Meetup.com ID for the venue.
name
    Name of the venue.
address_1
    Address of the venue, line 1.
address_2
    Address of the venue, line 2.
address_3
    Address of the venue, line 3.
city
    City of the venue.
state
    State or region of the venue.
zip
    Postal-code of the venue.
country
    Country of the venue.
lat
    Geographical latitude.
lon
    Geographical longitude.

MeetupMember
------------
id
    Meetup.com ID for the member.
name
    Full name (first & last) of the member.
photo
    A ``MeetupPhoto`` containing URLs to this member's photo resources.

MeetupPhoto
-----------
id
    Meetup.com ID for the photo.
url
    URL of the photo resource.
highres_url
    URL of the high-resolution version of the photo.
thumb_url
    URL of the thumbnail version of the photo.

"""


from collections import namedtuple


MeetupEvent = namedtuple('MeetupEvent',
        ['id', 'name', 'description', 'time', 'status', 'venue',
         'yes_rsvp_count', 'maybe_rsvp_count', 'event_url', 'photo_url',
         'attendees', 'photos'])

MeetupVenue = namedtuple('MeetupVenue',
        ['id', 'name', 'address_1', 'address_2', 'address_3', 'city', 'state',
         'zip', 'country', 'lat', 'lon'])

MeetupMember = namedtuple('MeetupMember', ['id', 'name', 'photo'])

MeetupPhoto = namedtuple('MeetupPhoto', 
        ['id', 'url', 'highres_url', 'thumb_url'])
