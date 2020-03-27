#!/usr/bin/env python

import pandas as pd

from matplotlib import pylab as plt
plt.ion()
import seaborn as sns

# read data from site
df = pd.read_json('http://covidtracking.com/api/states/daily?state=OH')

# convert date into date format
df['date'] = pd.to_datetime(df['date'],format = '%Y%m%d')

# plot
plt.figure()
sns.lineplot( x=df['date'], y = df['totalTestResults'], data = df )
plt.grid()

plt.figure()
sns.lineplot( x=df['date'], y = df['positive'], data = df )
plt.grid()
