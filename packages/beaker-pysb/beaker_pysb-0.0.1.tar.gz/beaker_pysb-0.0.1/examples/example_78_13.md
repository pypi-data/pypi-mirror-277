# Description
A test to verify ValueError is raised when running simulations with mismatching initial conditions and parameter values lengths using the 'nf' method in BngSimulator.

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

    @raises(ValueError)
    def test_nfsim_different_initials_params_lengths(self):
        A = self.model.monomers['A']

        sim = BngSimulator(self.model, tspan=np.linspace(0, 1),
                           initials={A(): [150, 250, 350]},

```
