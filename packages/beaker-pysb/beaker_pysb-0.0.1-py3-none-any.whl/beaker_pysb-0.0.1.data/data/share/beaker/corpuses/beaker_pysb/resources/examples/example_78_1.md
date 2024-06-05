# Description
A simple test of simulating a model using BngSimulator and retrieving the output.

# Code
```
from pysb.testing import *
import numpy as np
from pysb import Monomer, Parameter, Initial, Observable, Rule
from pysb.simulator.bng import BngSimulator
from pysb.bng import generate_equations

BNG_SEED = 123

class TestBngSimulator(object):
    @with_model
    def setUp(self):
        Monomer('A', ['a'])
        Monomer('B', ['b'])
        Parameter('ksynthA', 100)
        Parameter('ksynthB', 100)
        Parameter('kbindAB', 100)
        Parameter('A_init', 0)
        Parameter('B_init', 0)
        Initial(A(a=None), A_init)
        Initial(B(b=None), B_init)
        Observable('A_free', A(a=None))
        Observable('B_free', B(b=None))
        Observable('AB_complex', A(a=1) % B(b=1))
        Rule('A_synth', None >> A(a=None), ksynthA)
        Rule('B_synth', None >> B(b=None), ksynthB)
        Rule('AB_bind', A(a=None) + B(b=None) >> A(a=1) % B(b=1), kbindAB)
        self.model = model
        generate_equations(self.model)
        self.mon = lambda m: self.model.monomers[m]
        self.time = np.linspace(0, 1)

def test_1_simulation(self):
    x = self.sim.run()

```
