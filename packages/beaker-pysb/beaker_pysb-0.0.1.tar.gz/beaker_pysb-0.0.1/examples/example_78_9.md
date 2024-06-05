# Description
A test of running multiple simulations with different initial conditions using the 'nf' method in BngSimulator and ensuring the simulation outputs are as expected.

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

def test_nfsim_2initials(self):
    # Test with two initials
    A = self.model.monomers['A']
    x2 = self.sim.run(method='nf', tspan=np.linspace(0, 1),
                 initials={A(): [100, 200]}, seed=_BNG_SEED)
    assert x2.nsims == 2
    assert np.allclose(x2.dataframe.loc[0, 0.0], [100.0, 0.0, 0.0])

```
