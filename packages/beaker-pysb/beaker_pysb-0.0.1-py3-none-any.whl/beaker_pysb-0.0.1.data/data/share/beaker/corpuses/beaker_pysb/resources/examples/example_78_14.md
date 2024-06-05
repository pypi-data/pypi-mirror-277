# Description
A test to create a PopulationMap and run a simulation with it using the 'nf' method in BngSimulator, then check the observable output.

# Code
```
from pysb.testing import *
import numpy as np
from pysb.simulator.bng import BngSimulator, PopulationMap
from pysb.examples import robertson


def test_hpp():
    model = robertson.model
    # Reset equations from any previous network generation
    model.reset_equations()

    A = robertson.model.monomers['A']
    klump = Parameter('klump', 10000, _export=False)
    model.add_component(klump)

    population_maps = [
        PopulationMap(A(), klump)
    ]

    sim = BngSimulator(model, tspan=np.linspace(0, 1))
    x = sim.run(n_runs=1, method='nf', population_maps=population_maps,
                seed=_BNG_SEED)
    observables = np.array(x.observables)

```
