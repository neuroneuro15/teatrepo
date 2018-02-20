import sys
sys.path.append('../src')
from meetup import get_meetup_events, events_to_csv

from glob import glob
import pandas as pd


print('Collecting Data...', end='')

# Collect, Clean Data
for group in ['SuperPythonTalks', 'PyData-Munchen']:
    events = get_meetup_events(group)
    events_to_csv(events, fname='../data/raw'  + group + '_events.csv')
    
# Merge Data
df = pd.DataFrame()
for csv_fname in glob('../data/raw/*.csv'):
    dd = pd.read_csv(csv_fname)
    df = df.append(dd)
df.to_csv('../data/final/all_group_events.csv')
    
    
print('...done!')
