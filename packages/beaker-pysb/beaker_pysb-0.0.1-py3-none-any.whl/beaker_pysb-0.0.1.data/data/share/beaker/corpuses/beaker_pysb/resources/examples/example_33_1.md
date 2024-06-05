# Description
Run the Extrinsic Apoptosis Reaction Model (EARM) using BioNetGen's Hybrid-Particle Population (HPP) algorithm. This example showcases setting up the model, defining population maps, running simulations, and plotting results.

# Code
```
from pysb.examples.earm_1_0 import model
from pysb.simulator import BngSimulator
from pysb.simulator.bng import PopulationMap
from pysb import Parameter
import matplotlib.pyplot as plt

PARP, CPARP, Mito, mCytoC = [model.monomers[x] for x in
                             ['PARP', 'CPARP', 'Mito', 'mCytoC']]
klump = Parameter('klump', 10000, _export=False)
model.add_component(klump)

population_maps = [
    PopulationMap(PARP(b=None), klump),
    PopulationMap(CPARP(b=None), klump),
    PopulationMap(Mito(b=None), klump),
    PopulationMap(mCytoC(b=None), klump)
]

sim = BngSimulator(model, tspan=np.linspace(0, 20000, 101))
simres = sim.run(n_runs=20, method='nf', population_maps=population_maps)

trajectories = simres.all
tout = simres.tout

plot_mean_min_max('Bid_unbound')
plot_mean_min_max('PARP_unbound')
plot_mean_min_max('mSmac_unbound')
plot_mean_min_max('tBid_total')
plot_mean_min_max('CPARP_total')
plot_mean_min_max('cSmac_total')


```
