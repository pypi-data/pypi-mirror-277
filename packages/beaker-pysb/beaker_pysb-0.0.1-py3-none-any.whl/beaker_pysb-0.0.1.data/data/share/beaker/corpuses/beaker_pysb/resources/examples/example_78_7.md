# Description
A test of using 'nf' method in BngSimulator and checking observable length.

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

def test_nfsim_2runs(self):
    x = self.sim.run(n_runs=1, method='nf', seed=_BNG_SEED)
    observables = np.array(x.observables)

```
