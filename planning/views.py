from django.shortcuts import render
from pyicloud import PyiCloudService
import datetime
import os

def get_events():
    api = PyiCloudService(os.environ['APPLE_MAIL'], os.environ['APPLE_PASSWORD'])
    date = datetime.datetime.now()
    from_dt = datetime.datetime(date.year, date.month, date.day)
    to_dt = datetime.datetime(date.year, date.month, date.day, 23, 59, 59, 999)
    raw_events = api.calendar.events(from_dt, to_dt)

    f = lambda date: f"{str(date[4]).zfill(2)}:{str(date[5]).zfill(2)}"
    events = []
    for raw_event in raw_events:
        if date.day < raw_event['startDate'][3]:
            continue
        event = dict(
            title = raw_event['title'],
            start = f(raw_event['startDate']),
            end = f(raw_event['endDate']),
            guid = raw_event['guid'],
        )
        events.append(event)
    events.sort(key = lambda e:e['start'])
    return events

def planning(request):
    events = get_events()
    context=dict(title='planning', events=events)
    return render(request, 'planning/planning.html', context)
