from obspy.core import read, UTCDateTime
from obspy.clients.fdsn import Client
import numpy as np
import os
client=Client('IRIS')
network='C1'
station='VA04'
channel='BH*'
k=1
day=range(1,2,1)
for i in day:
    time=(UTCDateTime(year=2015, julday=i))
    file=str(time)[0:10]+'.mseed'
    data=client.get_waveforms(network,station,'*',channel,time
    ,time+24*60*60).write(file,format='MSEED')
    !mkdir $file | mv $file $file/