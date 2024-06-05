# Description
A test of running multiple simulations with different initial conditions using the 'nf' method in BngSimulator.

# Code
```
from pysb.testing import *
import numpy as np
from pysb.simulator.bng import BngSimulator
from pysb.examples import robertson

BNG_SEED = 123

class TestNfSim(object):
    def setUp(self):
        self.model = robertson.model
        self.model.reset_equations()
        self.sim = BngSimulator(self.model, tspan=np.linspace(0, 1))

A = self.model.monomers['A']
x = self.sim.run(n_runs=2, method='nf', tspan=np.linspace(0, 1),
            initials={A(): 100}, seed=_BNG_SEED)
assert (x.nsims == 2)

```
