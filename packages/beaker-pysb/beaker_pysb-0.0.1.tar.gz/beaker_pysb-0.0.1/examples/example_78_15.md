# Description
A test to ensure the BngSimulator stops at a condition using the 'stop_if' parameter.

# Code
```
from pysb.testing import *
import numpy as np
from pysb import Model, Parameter, Monomer, Rule, Observable, Expression
from pysb.simulator.bng import BngSimulator


def test_stop_if():
    Model()
    Monomer('A')
    Rule('A_synth', None >> A(), Parameter('k', 1))
    Observable('Atot', A())
    Expression('exp_const', k + 1)
    Expression('exp_dyn', Atot + 1)
    sim = BngSimulator(model, verbose=5)
    tspan = np.linspace(0, 100, 101)
    x = sim.run(tspan, stop_if='Atot>9', seed=_BNG_SEED)
    # All except the last Atot value should be <=9
    assert all(x.observables['Atot'][:-1] <= 9)
    assert x.observables['Atot'][-1] > 9
    # Starting with Atot > 9 should terminate simulation immediately
    y = sim.run(tspan, initials=x.species[-1], stop_if='Atot>9')

```
