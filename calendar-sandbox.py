#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
# https://developers.google.com/api-client-library/python/start/get_started

json_file = 'secrets/YOUR_GOOGLE__PROJECT.json'
scopes = ['https://www.googleapis.com/auth/calendar.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scopes=scopes)
http_auth = credentials.authorize(Http())
service = build("calendar", "v3", http=http_auth)

calendar_id = 'ja.japanese#holiday@group.v.calendar.google.com'

dtfrom = date(year=2016, month=1, day=1).isoformat() + "T00:00:00.000000Z"
dtto = date(year=2016, month=12, day=31).isoformat() + "T00:00:00.000000Z"

events_results = service.events().list(
        calendarId=calendar_id,
        timeMin=dtfrom,
        timeMax=dtto,
        maxResults=50,
        singleEvents=True,
        orderBy="startTime"
        ).execute()
events = events_results.get('items', [])
for event in events:
    print("%s\t%s" % (event["start"]["date"], event["summary"]))
