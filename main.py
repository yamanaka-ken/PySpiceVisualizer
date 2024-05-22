import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from natsort import natsorted
# from scipy.signal import windows
import setPyLTSpice
import glob

# set sampling time
dt = 10**-6
# set measure frequency points
freq_list = [100, 200, 1000]
Setting = setPyLTSpice.Initialize_Setting(dt, freq_list)
out_file = natsorted("./output")
out_file = glob.glob("./output/*.txt")

plt.clf()
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, sharex=ax1)

# do frequency analysis
for path in out_file:
    # loading text data
    df = pd.read_table(path)
    time = df.iloc[:,0]
    voltage = df.iloc[:,1]
    current = df.iloc[:,2]

    # acqire parameter 
    N = len(time)
    # apply window function
    # hamming = windows.hamming(N)
    # time = df.iloc[:,0]*hamming
    # voltage = df.iloc[:,1] *hamming
    # current = df.iloc[:,2] *hamming

    # Fourier transform
    freq = np.fft.rfftfreq(N, d=dt)
    vfourier = np.fft.rfft(voltage)
    cfourier = np.fft.rfft(current)
    vamplitude = np.abs(vfourier/(N/2))
    camplitude = np.abs(cfourier/(N/2))

    ax1.set_xscale('log')
    ax1.set_xlim(0.1,10000)
    ax1.plot(freq[1:int(N/2)], vamplitude[1:int(N/2)])
    ax2.plot(freq[1:int(N/2)], camplitude[1:int(N/2)])

plt.savefig('./output/FFT.png')