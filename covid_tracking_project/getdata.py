#!/usr/bin/env python

import pandas as pd

from matplotlib import pylab as plt
plt.ion()
import seaborn as sns

import numpy as np
import theano.tensor as tt
import pymc3 as pm

# read data from site
# api change, 
#df = pd.read_json('http://covidtracking.com/api/states/daily?state=OH')
df = pd.read_json('https://covidtracking.com/api/v1/states/daily.json') # gets all states
# dfs = pd.read_json('https://covidtracking.com/api/v1/states/OH/daily.json') # get Ohio

# limited set of counties
# dfc = pd.read_json('https://covidtracking.com/api/v1/counties.json')

# convert date into date format
df['date'] = pd.to_datetime(df['date'],format = '%Y%m%d')

dfs = df[ df['state'] == 'OH' ] 

# plot
plt.figure()
sns.lineplot( x=dfs['date'], y = dfs['totalTestResults'], data = dfs )
plt.grid()

plt.figure()
sns.lineplot( x=dfs['date'], y = dfs['positive'], data = dfs )
plt.grid()

plt.figure()
sns.lineplot( x=dfs['date'], y = dfs['death'], data = dfs )
plt.grid()


