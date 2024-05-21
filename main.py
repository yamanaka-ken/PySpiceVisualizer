import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from natsort import natsorted
from scipy.signal import windows
import setPyLTSpice
import glob


freq = setPyLTSpice.Initialize_Setting()
out_file = natsorted("./output")
out_file = glob.glob("./output/*.txt")

plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111)

for path in out_file:
    # loading text data
    df = pd.read_table(path)
    time = df.iloc[:,0]
    voltage = df.iloc[:,1]

    # acqire parameter 
    dt = 10**-6
    N = len(time)

    # apply window function
    # hamming = windows.hamming(N)
    # time = df.iloc[:,0]*hamming
    # voltage = df.iloc[:,1]*hamming
    time = df.iloc[:,0]
    voltage = df.iloc[:,1]

    # Fourier transform
    freq = np.fft.rfftfreq(N,d=dt)
    fourier = np.fft.rfft(voltage)
    amplitude = np.abs(fourier/N/2)

    ax.set_xscale('log')
    ax.set_xlim(0.1,10000)
    ax.plot(freq, amplitude)
plt.savefig('./output/FFT.png')