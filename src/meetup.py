import requests
import bs4
import pandas as pd

def get_meetup_events(group):
    """Returns a list of events and their details for a given meetup group."""
    url = 'https://api.meetup.com/{group}/events?&sign=true&photo-host=public&page=200&status=past'.format(group=group)
    r = requests.get(url)
    events = r.json()
    return events



def events_to_csv(events, fname):
    dd = pd.DataFrame(events)
    dd = dd[['yes_rsvp_count', 'name', 'local_date']]
    dd['Group'] = events[0]['group']['name']
    dd['local_date'] = pd.to_datetime(dd.local_date)
    dd.to_csv(fname, index=False)
    
