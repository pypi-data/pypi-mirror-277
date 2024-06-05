# Description
A test of running multiple simulations with different parameter values using the 'nf' method in BngSimulator and ensuring the parameter values are as expected.

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

def test_nfsim_2params(self):
    # Test with two param_values
    x3 = self.sim.run(method='nf', tspan=np.linspace(0, 1),
                      param_values=self.param_values_2sets, seed=_BNG_SEED)
    assert x3.nsims == 2

```
