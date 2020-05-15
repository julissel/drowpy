'''
Group strings from file:
1. Group by api-methods (Including IP). Find min, max and avg duration.
2. Group by time by level (up to 1 sec, 1-5 sec, 5-10 sec, 10-30 sec, more than 30 sec).
   Count the elements in each group. Including api-methods.

Example of string:
'000.000.000.000 - - [01/May/2020:23:00:00 +0000] "POST //server.module:00000/api/module/method HTTP/1.0" 200 10000  100'
Where:
000.000.000.000 - IP
01/May/2020:23:00:00 - Date

POST //server.module:00000/api/module/method HTTP/1.0 - api-method
200 - status code
10000 - size
100 - duration (in milliseconds)
'''

import pandas as pd
import numpy as np
from datetime import datetime


# Create DataFrame from file
df_old = pd.read_table('some.log', delim_whitespace=True,
                    names=('IP', 'tmp1', 'tmp2', 'Date', 'tmp3', 'ApiMethod', 'StatusCode', 'Len', 'Duration'))

# delete '[' in "Date" column
df_old['Date'] = df_old['Date'].str.strip('[') # or if you need del symbol not only in borders use replace('[','') instead strip

# save only a part of the string, before we find '?'
df_old['ApiMethod'] = df_old['ApiMethod'].apply(lambda x: x.split('?')[0])

# save only a part of the string, before we find 'HTTP/1.'
df_old['ApiMethod'] = df_old['ApiMethod'].apply(lambda x: x.split('HTTP/1.')[0])


# 1.1
# group by ApiMethod
df_api_method = df_old[['ApiMethod', 'Len', 'Duration']]
df_api_method.groupby(['ApiMethod']).agg(['count', 'min', 'mean', 'max']).to_csv('api_method.csv')


# 1.2
# group by ApiMethod and IP
df_api_ip = df_old[['ApiMethod', 'IP', 'Len', 'Duration']]
df_api_ip.groupby(['ApiMethod', 'IP']).agg(['count', 'min', 'mean', 'max']).to_csv('api_ip.csv')


# 2
# 1 sec = 1 000 ms
df_times = df_old[['Duration', 'ApiMethod']]

# set the points at which the boundaries of the categories will be located
bins = [-np.inf, 1000, 5000, 10000, 30000, np.inf]
# name the intervals (bins)
group_names = ['1 - Less 1 sec', '2 - Betw 1 and 5 sec', '3 - Betw 5 and 10 sec', '4 - Betw 10 and 30 sec', '5 - More 30 sec']
# create a new column with values ​​from 'group_names' depending on belonging to the interval
df_times['Groups'] = pd.cut(df_times['Duration'], bins, labels=group_names)

# 2.1
# Count the elements in each time-group
df_times.groupby(['Groups']).count().to_csv('time_groups.csv')

# 2.2
# Count the elements in each time-group? including api-method
df_times.groupby(['ApiMethod', 'Groups']).count().to_csv('time_groups_api.csv')
