# Description
A test of running multiple simulations with different initial conditions and parameter values using the 'nf' method in BngSimulator and ensuring the simulation outputs are as expected.

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

def test_nfsim_2initials_2params(self):
    # Test with two initials and two param_values
    A = self.model.monomers['A']
    x = self.sim.run(method='nf',
                     tspan=np.linspace(0, 1),
                     initials={A(): [101, 201]},
                     param_values=[[1, 2, 3, 4, 5, 6],
                                   [7, 8, 9, 10, 11, 12]],
                     seed=_BNG_SEED)
    assert x.nsims == 2
    # Initials for A should be set by initials dict, and from param_values
    # for B and C
    assert np.allclose(x.dataframe.loc[0, 0.0], [101.0, 5.0, 6.0])

```
