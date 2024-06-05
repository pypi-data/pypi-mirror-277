# Description
Run stochastic simulations on the EARM 1.0 model using the SSA and tau-leaping algorithms.

# Code
```
from pysb.simulator import StochKitSimulator
from pysb.examples import earm_1_0
import numpy as np

def test_stochkit_earm():
    tspan = np.linspace(0, 1000, 10)
    sim = StochKitSimulator(earm_1_0.model, tspan=tspan)
    simres = sim.run(n_runs=2, seed=_STOCHKIT_SEED, algorithm="ssa")

```
