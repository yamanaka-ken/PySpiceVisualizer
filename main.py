import matplotlib.pyplot as plt
from PyLTSpice import SimRunner, SpiceEditor, LTspice
# from PyLTSpice import RawRead, SimCommander

# Force another simulatior
simulator = r"C:/Users/ymnk2/Documents/XVIIx64.exe"

LTC = SimRunner(output_folder='./output')
LTC.create_netlist("LTSpice/TEST.asc")



# LTC = SimCommander(r'C:/Users/ymnk2/Documents/GitHub/PySpiceVisualizer/LTSpice/TEST.asc')

