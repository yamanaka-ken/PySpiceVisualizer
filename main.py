from PyLTSpice import SimRunner
from PyLTSpice import SpiceEditor

# change place simulatior location
simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

# select spice model
LTC = SimRunner(output_folder='./output')
LTC.create_netlist('./LTSpice/TEST.asc')
netlist = SpiceEditor('./LTSpice/TEST.net')
netlist.set_component_value('fsig', '500')

for fsig in (500,1000):
    netlist.set_component_value('fsig', fsig)
    print("frequency", fsig)
    LTC.run(netlist)





