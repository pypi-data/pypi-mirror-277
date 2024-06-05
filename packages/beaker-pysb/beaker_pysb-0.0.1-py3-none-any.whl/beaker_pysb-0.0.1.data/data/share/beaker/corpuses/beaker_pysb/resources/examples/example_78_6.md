# Description
A test to ensure the simulator outputs expressions and observables correctly with the 'ode' method.

# Code
```
pysb.testing import *
numpy as np
pysb.examples import expression_observables

def test_bng_ode_with_expressions():
    model = expression_observables.model
    model.reset_equations()

    sim = BngSimulator(model, tspan=np.linspace(0, 1))
    x = sim.run(n_runs=1, method='ode')
    assert len(x.expressions) == 50

```
