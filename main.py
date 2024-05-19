import matplotlib.pyplot as plt
from PyLTSpice import RawRead
import math

#.rawファイルを読み込む。
LTR = RawRead(r'./LTSpice/TEST.raw')

# #LTspiceで使っているラベル類を抜きだす。
# print(LTR.get_trace_names())

# #.rawファイルの上のほうの情報を抜き出す。
# print(LTR.get_raw_property())

# print(LTR.get_trace_names())
# print(LTR.get_raw_property())

fig = plt.figure()
ax2 = fig.add_subplot(212)
ax = fig.add_subplot(211, sharex=ax2)


V4 = LTR.get_trace("V(N004)")
V6 = LTR.get_trace("V(N006)")
IR10 = LTR.get_trace("I(R10)")
x = LTR.get_trace('time')  # Gets the time axis
steps = LTR.get_steps()
li = ['10kHz','50kHz','100kHz']
for step in range(len(steps)):
    ax.plot(x.get_wave(step), V4.get_wave(step)-V6.get_wave(step), label=li[steps[step]])
    ax.set_ylabel('Voltage[V]')
    ax2.plot(x.get_wave(step), IR10.get_wave(step), label=li[steps[step]])
    ax2.set_ylabel('Current[A]')
    ax2.set_xlabel('Time[s]')

ax.legend()  # order a legend
ax2.legend()  # order a legend

plt.show()
