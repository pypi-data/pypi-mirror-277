# Description
Simulating and plotting figure 4B from the EARM 1.0 publication.

# Code
```
from __future__ import print_function
from pysb.simulator import ScipyOdeSimulator
import matplotlib.pyplot as plt
from numpy import *
from earm_1_0 import model

L_0_baseline = model.parameters['L_0'].value


def fig_4b():
    print("Simulating model for figure 4B...")

    t = linspace(0, 6*3600, 6*60+1)  # 6 hours
    x = sim.run(tspan=t).all

    x_norm = c_[x['Bid_unbound'], x['PARP_unbound'], x['mSmac_unbound']]
    x_norm = 1 - x_norm / x_norm[0, :]  # gets away without max() since first values are largest

    # this is what I originally thought 4B was plotting. it's actually very close. -JLM
    #x_norm = array([x['tBid_total'], x['CPARP_total'], x['cSmac_total']]).T
    #x_norm /= x_norm.max(0)

    tp = t / 3600  # x axis as hours

    plt.figure("Figure 4B")
    plt.plot(tp, x_norm[:,0], 'b', label='IC substrate (tBid)')
    plt.plot(tp, x_norm[:,1], 'y', label='EC substrate (cPARP)')
    plt.plot(tp, x_norm[:,2], 'r', label='MOMP (cytosolic Smac)')
    plt.legend(loc='upper left', bbox_to_anchor=(0,1)).draw_frame(False)
    plt.xlabel('Time (hr)')
    plt.ylabel('fraction')
    a = plt.gca()

```
