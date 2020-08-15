from django.shortcuts import render
from pyicloud import PyiCloudService
import datetime
import os

def duration_printer(duration):
    d = int(duration/24/60)
    h = int(duration%(24*60)/60)
    m = duration%60 
    out = []
    if duration >= 24 * 60 and d != 0:
        if d >= 2:
            out.append(f"{d} days")
        else:
            out.append(f"{d} day")
    if duration >= 60 and h != 0:
        if h >= 2:
            out.append(f"{h} hours")
        else:
            out.append(f"{h} hour")
    if m != 0:
        if m >= 2:
            out.append(f"{m} minutes")
        else:
            out.append(f"{m} minute")
    return ' '.join(out)

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
            duration = duration_printer(raw_event['duration']),
        )
        events.append(event)
    events.sort(key = lambda e:e['start'])
    return events
        

def planning(request):
    events = get_events()
    context=dict(title='planning', events=events)
    return render(request, 'planning/planning.html', context)
