import matplotlib.pyplot as plt
import pandas as pd

print('Analyzing data...', end='')

## Get Data
df = pd.read_csv('../data/all_group_events.csv')
    
## Analyze Data
df.set_index('local_date', inplace=True)

# Plot Attendance by Group
fig, ax = plt.subplots()
groups = df.groupby('Group')
groups.plot(ax=ax)
plt.legend(groups.groups.keys())
fig.savefig('../figures/Meetup_Attendance_by_group.png')

# Plot Total Attendance
df.reset_index().groupby('local_date').sum().plot()
plt.gcf().savefig('../figures/Total_Meetup_Attendance.png')

print('done!')