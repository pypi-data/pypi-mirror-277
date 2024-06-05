# Description
EARM 1.3 model simulation and dynamic observable tests

# Code
```
from pysb.simulator import ScipyOdeSimulator
from nose.tools import raises
from pysb.examples import earm_1_3
import numpy as np

class TestSimulationResultEarm13(object):
    def setUp(self):
        self.model = earm_1_3.model
        self.tspan = np.linspace(0, 100, 101)
        self.sim = ScipyOdeSimulator(self.model, tspan=self.tspan)
        self.simres = self.sim.run()

    @raises(ValueError)
    def test_dynamic_observable_nonpattern(self):
        self.simres.observable('cSmac')

    @raises(ValueError)
    def test_match_nonexistent_pattern(self):
        m = self.model.monomers
        self.simres.observable(m.cSmac() % m.Bid())

    def test_on_demand_observable(self):
        m = self.model.monomers

```
