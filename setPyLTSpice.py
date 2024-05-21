from PyLTSpice import SimRunner
from PyLTSpice import SpiceEditor
from PyLTSpice.log.ltsteps import LTSpiceLogReader
from PyLTSpice import RawRead
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np


class Initialize_Setting():
    '''
    This module creates net, log, raw, and png files 
    for multiple frequencies based on a single asc file. 
    Please rewrite the code here for the measurement 
    frequencies, executable file paths, 
    and other configuration details.
    '''
    def __init__(self):
        # change place simulatior location
        simulator = r"C:/Program Files/LTC/LTspiceXVII/XVIIx64.exe"

        # select spice model
        LTC = SimRunner(output_folder='./output')

        LTC.create_netlist('./LTSpice/Draft3.asc')
        netlist = SpiceEditor('./LTSpice/Draft3.net')
        # netlist.set_parameter('fsig', '500')
        # netlist.write_netlist("Draft3_Modified.net")

        dt = 10**-6

        # set measure frequency points
        freq_list = [100, 200, 1000]

        for fsig in freq_list:
            netlist.set_parameter('fsig', fsig)
            # netlist.write_netlist(f"{fsig}_Draft3.net")
            LTC.run(netlist)
        

        i = 1
        for raw,log in LTC:
            # print("Raw file: %s, Log file: %s" % (raw, log))
            LTR = RawRead(raw)
            # print(LTR.get_trace_names())
            steps = LTR.get_steps() 
            time = LTR.get_trace("time")
            Vn002 = LTR.get_trace("V(n002)")

            plt.clf()
            for step in range(len(steps)):
                # print(steps[step])
        
                time_array = time.get_wave(step)
                voltage_array = Vn002.get_wave(step)
                plt.plot(time.get_wave(step), Vn002.get_wave(step))

                f = interpolate.interp1d(time_array, voltage_array)
                with open(f'./output/Draft3_{i}.txt','w') as file:
                    x_ax = np.arange(time_array[0],time_array[-1], dt)
                    y_ax = f(x_ax)  
                    for x,y in zip(x_ax, y_ax):     
                        file.write(f"{x}\t{y}\n")

            plt.savefig(f'./output/Draft3_{i}.png')
            i += 1
        self.falg = True

    def __call__(self):
        if self.flag:
            self.falg = False
            return True
        else:
            return False
        