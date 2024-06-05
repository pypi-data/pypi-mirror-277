# Description
Test the scipy ODE simulator with dynamic species and generated species configuration.

# Code
```
from pysb.simulator import ScipyOdeSimulator
import numpy as np

class TestScipySimulatorBase(object):
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
        self.mon = lambda m: self.model.monomers[m]
        self.time = np.linspace(0, 1)

"""Test y0 with dynamically generated species."""
simres = self.sim.run(initials={self.mon('A')(a=None): 0,
                       self.mon('B')(b=1) % self.mon('A')(a=1): 100,
                       self.mon('B')(b=None): 0})

```
