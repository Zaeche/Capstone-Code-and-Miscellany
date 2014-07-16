#!/usr/bin/env python2.7

#Import from relevant header files and libraries
import serial, string
import time, sys, datetime
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylplot as plt
import pasdas as pd

# We begin by accessing and storing the temperature data:
data = np.loadtxt('tempData.csv', delimiter=',', skiprows=1)

# Define the time axis:
time = [datetime.datetime.fromtimestamp(t/1000) for t in temp]

n = 100
idx = pd.date_range( start=dt.datetime.now( ), periods=n, freq='S' )
ts1= pd.Series( np.sin( np.linspace( 0, 4 * np.pi, n ) ), index=idx)
ts2= pd.Series( np.cos( np.linspace( 0, 4 * np.pi, n ) ), index=idx)

fig = plt.figure( figsize=(8, 6) )
ax = fig.add_axes( [.05, .05, .9, .9] )

ts1.plot( ax )
ts2.plot( ax )
(ts1 - ts2).plot( ax )


