from PyLTSpice import SimRunner
from PyLTSpice import SpiceEditor
from PyLTSpice.log.ltsteps import LTSpiceLogReader
import pathlib

# change place simulatior location
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# select spice model
LTC = SimRunner(output_folder='./output')
LTC.create_netlist('./LTSpice/Draft3.asc')
netlist = SpiceEditor('./LTSpice/Draft3.net')
netlist.set_component_value('fsig', '500')

for fsig in (500,1000):
    netlist.set_component_value('fsig', fsig)
    print("frequency", fsig)
    LTC.run(netlist)

for raw,log in LTC:
    print("Raw file: %s, Log file: %s" % (raw, log))
    # path =pathlib.Path(log)






